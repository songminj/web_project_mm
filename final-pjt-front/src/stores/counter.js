import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const router = useRouter()
  const auth = ref({})
  const comments = ref([])
  const error = ref(null)
  const bankList = ref([])
  const deposits = ref([])
  const myDeposits = ref([])
  const filteredDeposit = ref(null)
  const liked = ref(false)

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })


  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
        error.value = null
      })
      .catch(err => {
        if (err.response && err.response.status === 404) {
          articles.value = []
          error.value = 'No articles found'
        } else {
          error.value = 'An error occurred while fetching articles'
        }
      })
  }


  const getComments = function (articleId) {
    axios({
      method: 'get',
      url: `${API_URL}/articles/${articleId}/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        comments.value = response.data
      })
      .catch(err => {
        error.value = 'An error occurred while fetching comments'
      })
  }

  const createComment = async function (content, articleId) {
    try {
      await axios({
        method: 'post',
        url: `${API_URL}/articles/${articleId}/comments/`,
        data: {
          content: content,
          user_id:auth.value.id,
          nickname: auth.value.nickname
        },
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      await getComments(articleId)
    } catch (error) {
    }
  }

  const getAuth = function () {
    axios({
      method: 'get',
      url: `${API_URL}/account/user_profile/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
      .then(response => {
        auth.value = response.data
      })
      .catch(error => {
      })
  }

  const changeAuth = function () {
    axios({
      method: 'put',
      url: `${API_URL}/account/user_profile/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data : {
        nickname : auth.value.nickname, 
        email : auth.value.email, 
        finance_goal : auth.value.finance_goal, 
        assets : auth.value.assets, 
        age: auth.value.age, 
        salary : auth.value.salary,
      }
    })
      .then(response => {
        // auth.value = response.data
        router.push({ name : 'ProfileView' })
      })
      .catch(error => {
      })
  }

  const getDetailArticle = function (id) {
    return articles.value.find(article => article.id === id)
  }
  

  const signUp = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    const email = payload.email
    const finance_goal = payload.finance_goal
    const assets = payload.assets
    const age = payload.age
    const salary =payload.salary
    const nickname = payload.nickname

    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, password1, password2, email, finance_goal, age, salary, assets, nickname
      }
    })
     .then((response) => {
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
     })
  }

  const logOut = function () {
    token.value = null
    auth.value = []
    router.push({name : 'MainView'})
  }
  
  const logIn = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        token.value = response.data.key
        router.push({ name : 'ProfileView' })
      })
      .catch((error) => {
      })
  }

  const deleteArticle = function(id) {
    axios({
      method: 'delete',
      url: `${API_URL}/articles/${id}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      router.push({ name: 'ArticleListView' })
    })
    .catch((error) => {
    })
  }

  const updateArticle = async function(id, title, content) {
    try {
      const response = await axios({
        method: 'put',
        url: `${API_URL}/articles/${id}/`,
        headers: {
          Authorization: `Token ${token.value}`
        },
        data: {
          title: title,
          content: content
        },
      })
    const updatedArticle = response.data
    const articleIndex = articles.value.findIndex(article => article.id === id)
    if (articleIndex !== -1) {
      articles.value[articleIndex] = updatedArticle
    }
    } catch (error) {
    }
  }

  const deleteComment = function (articleId, commentId) {
    axios({
      method: 'delete',
      url: `${API_URL}/articles/comments/${commentId}/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      getComments(articleId)
      router.push({ name: 'ArticleDetailView', params : {articleId} })
    })
    .catch((error) => {
    })
  }

  const updateComment = async function (articleId, commentId, content) {
    try {
      await axios({
        method: 'put',
        url: `${API_URL}/articles/comments/${commentId}/`,
        headers: {
          Authorization: `Token ${token.value}`
        },
        data: {
          content:content
        },
      })
      await getComments(articleId)
    } catch (error) {
    }
  }

  // 예금 그래프 가져오기
  const getDepositGraphs = async function () {
    try {
      const response = await axios.get(`${API_URL}/deposits/deposit_cart_option/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      return response.data.graphs;
    } catch (error) {
      return [];
    }
  }



  const getDeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/deposit_options/`,
    })
      .then(response => {
        deposits.value = response.data
      })
      .catch(error => {
      })
  }


  const getBank = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finances/bank/`,
    })
      .then(response => {
        bankList.value = response.data
      })
      .catch(error => {
      })
  } 

  const filterDeposit = function (fin_id) {
    filteredDeposit.value = deposits.value.find(deposit => deposit.fin_prdt_cd === fin_id)
  }

  const getMyDeposit = async () => {
    try {
      const response = await axios.get(`${API_URL}/deposits/deposit_cart/`, {
        headers: {
          Authorization: `Token ${token.value}`
        }
      });
      myDeposits.value = response.data
      return myDeposits.value
    } catch (error) {
    }
  };

  // 장바구니 담기 
  const selectMyDeposit = async (productId) => {
    try {
      await axios.post(`${API_URL}/deposits/update_deposit_cart/${productId}/`, {}, {
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      await getMyDeposit()
  } catch (error) {
      }
  }

  // 장바구니 취소 
  const deleteMyDeposit = async (productId) => {
    try {
      await axios.delete(`${API_URL}/deposits/update_deposit_cart/${productId}/`, {
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      await getMyDeposit()
  } catch (error) {
      }
  }


  return {
    articles,
    auth,
    API_URL,
    comments,
    changeAuth,
    getAuth,
    getComments,
    deleteComment,
    updateComment,
    createComment,
    getArticles,
    getDetailArticle,
    signUp,
    logIn,
    logOut,
    deleteArticle,
    updateArticle,
    token,
    isLogin,
    getDepositGraphs,
    deposits,
    myDeposits,
    bankList,
    filteredDeposit,
    getBank,
    getDeposit,
    filterDeposit,
    getMyDeposit,
    selectMyDeposit,
    deleteMyDeposit
  }
}, { persist: true })

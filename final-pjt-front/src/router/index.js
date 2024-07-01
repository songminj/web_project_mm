import { createRouter, createWebHistory } from 'vue-router'
import ProfileView from '@/views/ProfileView.vue'
import SigninView from '@/views/SigninView.vue'
import MainView from '@/views/MainView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import DepositListView from '@/views/DepositListView.vue'
import DepositDetailView from '@/views/DepositDetailView.vue'
import ArticleListView from '@/views/ArticleListView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import SignupView from '@/views/SignupView.vue'
import BankView from '@/views/BankView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import { useCounterStore } from '@/stores/counter'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView
    },
    {
      path: '/signin/',
      name: 'SigninView',
      component: SigninView
    },
    {
      path: '/signup/',
      name: 'SignupView',
      component: SignupView
    },
    {
      path: '/profile/',
      name: 'ProfileView',
      component: ProfileView
    },
    {
      path: '/exchange/',
      name: 'ExchangeView',
      component: ExchangeView
    },
    {
      path: '/bank/',
      name: 'BankView',
      component: BankView
    },
    {
      path: '/deposit/',
      name: 'DepositView',
      component: DepositListView
    },
    {
      path: '/deposit/:fin_prdt_cd',
      name: 'DepositDetailView',
      component: DepositDetailView
    },
    {
      path: '/articles/',
      name: 'ArticleListView',
      component: ArticleListView
    },
    {
      path: '/articles/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    },
    {
      path: '/articles/create/',
      name: 'ArticleCreateView',
      component: ArticleCreateView
    },
    {
      path: '/articles/update/:id',
      name: 'ArticleUpdateView',
      component: ArticleUpdateView
    },
  ]
})
router.beforeEach((to, from) => {
  const store = useCounterStore()
  if (to.name === 'ArticleListView' && !store.isLogin) {
    window.alert('로그인이 필요합니다')
    return { name : 'SigninView'}
  }
  if ((to.name === 'SignupView' || to.name === 'SigninView') && (store.isLogin)) {
    window.alert('이미 로그인되어있습니다.')
    return { name:'MainView'}
  }
  if (to.name === 'ProfileView' && !store.isLogin) {
    window.alert('로그인이 필요합니다')
    return { name : 'SigninView'}
  }
})

export default router

import { ref } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useDepositStore = defineStore('deposit', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const bankList = ref([])
  const deposits = ref([])
  const myDeposits = ref([])
  const filteredDeposit = ref([])
  const liked = ref(false)

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

  const getMyDeposit = function () {
    axios({
      method: 'get',
      url: `${API_URL}/deposits/deposit_cart/`,
    })
      .then(response => {
        myDeposits.value = response.data
      })
      .catch(error => {
      })
  }

  // 장바구니 담기 
  const selectMyDeposit = function (productId) {
    axios({
      method: 'post',
      url: `${API_URL}/deposits/update_deposit_cart/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        user:auth.user.id,

      },
    })
      .then(response => {
      })
      .catch(error => {
      })
  }

  // 장바구니 취소 
  const deleteMyDeposit = function (productId) {
    axios({
      method: 'delete',
      url: `${API_URL}/deposits/update_deposit_cart/${productId}/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
    })
      .then(response => {
      })
      .catch(error => {
      })
  }

  return { deposits, myDeposits, bankList, filteredDeposit, getBank, getDeposit, filterDeposit, getMyDeposit, selectMyDeposit, deleteMyDeposit }
}, { persist: true })

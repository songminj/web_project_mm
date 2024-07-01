import { ref, watch } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useBankMapStore = defineStore('bankmap', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const bankList = ref([])
  const addressList = ref([])
  const sidoList = ref([])
  const sigunguList = ref([])
  const sido = ref('')
  const sigungu = ref('')
  const bank = ref('')
  
  const getSigungu = function () {
    axios({
      method: 'get',
      url: `${API_URL}/finances/address/`,
    })
    .then(response => {
        addressList.value = response.data
        uniqueSido()
      })
      .catch(error => {
      })
  }

  const uniqueSido = function () {
    const sidoSet = new Set()
    addressList.value.forEach(address => {
      sidoSet.add(address.sido)
    })
    sidoList.value = Array.from(sidoSet)
  }

  const uniqueSigungu = function (sido) {
    const sigunguSet = new Set()
    addressList.value.forEach(address => {
      if (address.sido === sido && address.sigungu !== 'nan') {
        sigunguSet.add(address.sigungu)
      }
    })
    sigunguList.value = Array.from(sigunguSet)
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

  const resetValues = function () {
    sido.value = ''
    sigungu.value = ''
    bank.value = ''
  }

  watch(sido, (newSido) => {
    uniqueSigungu(newSido)
  })
  
  return { API_URL, sido, sigungu, addressList, sidoList, sigunguList, bank, 
    getSigungu, uniqueSido, uniqueSigungu, getBank, resetValues, bankList }
}, { persist: true })

import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeStore = defineStore('exchange', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const exchangeData = ref([])
  const fromCountry = ref(null)
  const toCountry = ref(null)

  const getExchange = async function () {
    try {
      const response = await axios.get(`${API_URL}/finances/exchange_rate/`)
      exchangeData.value = response.data
    } catch (error) {
    }
  }

  const clearExchange = function () {
    fromCountry.value = null
    toCountry.value = null
  }

  return { API_URL, exchangeData, getExchange, clearExchange, fromCountry, toCountry }
}, { persist: true })

<template>
  <div class="container">
    <h1>환율 계산기</h1>
    <div class="form-group">
      <label for="fromCountry">기준 통화 국가</label>
      <select class="form-control" v-model="fromCountry" id="fromCountry">
        <option value="">기준 통화 국가</option>
        <option v-for="country in store.exchangeData" :key="country.cur_unit" :value="country">
          {{ country.cur_nm }}
        </option>
      </select>
    </div>
    <div class="form-group">
      <label for="fromAmount">금액을 입력하세요</label>
      <input type="number" class="form-control" id="fromAmount" v-model="fromAmount">
    </div>
    <div class="form-group">
      <label for="toCountry">환전 통화 국가</label>
      <select class="form-control" v-model="toCountry" id="toCountry">
        <option value="">환전 통화 국가</option>
        <option v-for="country in store.exchangeData" :key="country.cur_unit" :value="country">
          {{ country.cur_nm }}
        </option>
      </select>
    </div>
    <div class="form-group">
      <label for="calculatedAmount">환전된 금액입니다</label>
      <input type="text" class="form-control" id="calculatedAmount" :value="calculatedAmount" readonly>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useExchangeStore } from '@/stores/exchange'

const store = useExchangeStore()
const fromAmount = ref(1000)
const fromCountry = ref(null)
const toCountry = ref(null)

const parseRate = (rateString) => {
  return parseFloat(rateString.replace(/,/g, ''))
}

const calculatedAmount = computed(() => {
  if (!fromCountry.value || !toCountry.value || fromAmount.value === 0) {
    return 0;
  }

  let fromRate = parseRate(fromCountry.value.deal_bas_r);
  let toRate = parseRate(toCountry.value.deal_bas_r);
  
  if (fromCountry.value.cur_unit.includes('(100)')) {
    fromRate /= 100;
  }
  if (toCountry.value.cur_unit.includes('(100)')) {
    toRate /= 100;
  }

  const amountInKRW = fromAmount.value * fromRate
  const convertedAmount = amountInKRW / toRate

  return convertedAmount.toFixed(2)
})

onMounted(async () => {
  try {
    await store.getExchange()
    store.clearExchange()
    fromAmount.value = 1000
  } catch (error) {
  }
});
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #007bff;
}

.form-group {
  margin-bottom: 20px;
}

.form-control {
  border: 1px solid #007bff;
  border-radius: 4px;
  padding: 8px;
  font-size: 16px;
  width: 100%;
  box-sizing: border-box;
}

.form-control:focus {
  border-color: #0056b3;
  box-shadow: 0 0 8px rgba(0, 123, 255, 0.25);
}

label {
  margin-bottom: 5px;
  font-weight: bold;
  color: #007bff;
  display: block;
}


button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #0056b3;
}
</style>

<template>
  <div class="deposit-list">
    <h3>예적금 상품 정보</h3>
    <p>* 예치 기간의 이자율이 0이면 존재하지 않는 상품입니다.</p>
    <p>* 상품 정보를 클릭하면 상세 페이지로 이동합니다.</p>

    <div>
      <div v-for="(deposit, index) in filteredDeposits" :key="index" class="deposit-item" @click="goDetail(deposit.fin_prdt_cd)">
        <h2 class="deposit-name">{{ deposit.fin_prdt_nm }}</h2>
        <p class="deposit-details">은행: {{ deposit.kor_co_nm }}</p>
        <p class="deposit-details">공시 월: {{ deposit.dcls_month }}</p>
        <div class="interest-rates">
          <p v-if="props.period === 'total' || props.period === '6'">6개월: {{ deposit.intr_rate_06_1 ?? 'N/A' }} %</p>
          <p v-if="props.period === 'total' || props.period === '12'">12개월: {{ deposit.intr_rate_12_1 ?? 'N/A' }} %</p>
          <p v-if="props.period === 'total' || props.period === '24'">24개월: {{ deposit.intr_rate_24_1 ?? 'N/A' }} %</p>
          <p v-if="props.period === 'total' || props.period === '36'">36개월: {{ deposit.intr_rate_36_1 ?? 'N/A' }} %</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed, onMounted, watchEffect } from 'vue'
import { useDepositStore } from '@/stores/deposit'
import { useRouter } from 'vue-router'

const store = useDepositStore()
const router = useRouter()

const props = defineProps({
  bank: String,
  period: String,
})

const goDetail = (fin_prdt_cd) => {
  router.push({ name: 'DepositDetailView', params: { fin_prdt_cd } })
}

const filteredDeposits = computed(() => {
  return store.deposits.filter(deposit => {
    const matchesBank = !props.bank || deposit.kor_co_nm === props.bank
    let matchesPeriod = true

    if (props.period !== 'total') {
      const periodInMonths = parseInt(props.period, 10)
      const interestRateKey = `intr_rate_${String(periodInMonths).padStart(2, '0')}_1`
      matchesPeriod = deposit.hasOwnProperty(interestRateKey) && deposit[interestRateKey] > 0
    }

    return matchesBank && matchesPeriod
  })
})

onMounted(() => {
  store.getDeposit()
  store.getBank()
})
</script>

<style scoped>
.deposit-list {
  padding: 20px;
}

.deposit-item {
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.deposit-item:hover {
  background-color: #f9f9f9;
}

.deposit-name {
  margin: 0 0 10px;
  font-size: 20px;
  color: #007bff;
}

.deposit-details {
  margin: 0;
  font-size: 16px;
  color: #555;
}

.interest-rates {
  margin-top: 10px;
}

.interest-rates p {
  margin: 5px 0;
}
</style>

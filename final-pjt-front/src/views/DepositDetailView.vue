<template>
  <div class="container">
    <h1>예적금 상세페이지</h1>

    <div class="detail-box">
      <h2 class="deposit-name">{{ store.filteredDeposit?.fin_prdt_nm }}</h2>
      <p class="deposit-details">상품 코드: {{ store.filteredDeposit?.fin_prdt_cd }}</p>
      <p class="deposit-details">공시 월: {{ store.filteredDeposit?.dcls_month }}</p>
      <p class="deposit-details">은행: {{ store.filteredDeposit?.kor_co_nm }}</p>
      <div class="interest-rates">
        <p>6개월: {{ store.filteredDeposit?.intr_rate_06_1 ?? 'N/A' }}%</p>
        <p>12개월: {{ store.filteredDeposit?.intr_rate_12_1 ?? 'N/A' }}%</p>
        <p>24개월: {{ store.filteredDeposit?.intr_rate_24_1 ?? 'N/A' }}%</p>
        <p>36개월: {{ store.filteredDeposit?.intr_rate_36_1 ?? 'N/A' }}%</p>
      </div>
      <p class="deposit-details">특별 조건: {{ store.filteredDeposit?.spcl_cnd }}</p>
      <p class="deposit-details">가입 대상: {{ store.filteredDeposit?.join_member }}</p>
      <p class="deposit-details">가입 방법: {{ store.filteredDeposit?.join_way }}</p>
    </div>
    <div class="button-group">
      <button
        v-if="!isInMyDeposits"
        class="btn btn-primary"
        @click="handleSelectMyDeposit"
      >
        ❤ 추가하기
      </button>
      <button
        v-else
        class="btn btn-secondary"
        @click="handleDeleteMyDeposit"
      >
        🤍 삭제하기
      </button>
      <button class="btn btn-secondary" @click="handleGoBack">뒤로가기</button>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter.js'

const route = useRoute()
const router = useRouter()
const store = useCounterStore()

onMounted(async () => {
  const fin_id = route.params.fin_prdt_cd
  await store.filterDeposit(fin_id)
  await store.getMyDeposit()
})

const isInMyDeposits = computed(() => {
  return store.myDeposits.some(deposit => deposit.product.id === store.filteredDeposit?.id)
})

const handleSelectMyDeposit = async () => {
  await store.selectMyDeposit(store.filteredDeposit.id)
}

const handleDeleteMyDeposit = async () => {
  await store.deleteMyDeposit(store.filteredDeposit.id)
}

const handleGoBack = () => {
  router.push({ name: 'DepositView' })
}
</script>

<style scoped>
.container {
  padding: 20px;
  max-width: 800px;
  margin: auto;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  font-size: 24px;
  color: #007bff;
}

.detail-box {
  border: 1px solid #ddd;
  padding: 20px;
  border-radius: 8px;
  background-color: #fff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.deposit-name {
  margin: 0 0 20px;
  font-size: 20px;
  color: #007bff;
}

.deposit-details {
  margin: 10px 0;
  font-size: 16px;
  color: #555;
}

.interest-rates {
  margin-top: 10px;
}

.interest-rates p {
  margin: 5px 0;
}

.button-group {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.btn {
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  color: white;
}

.btn-secondary {
  background-color: #6c757d;
  border-color: #6c757d;
  color: white;
}

.btn:hover {
  opacity: 0.9;
}
</style>

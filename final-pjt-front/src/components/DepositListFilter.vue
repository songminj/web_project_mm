<template>
  <div>
    <h3>예적금 상품 정보</h3>
    <table>
      <colgroup>
        <!-- Define column widths if needed -->
      </colgroup>
      <thead>
        <tr>
          <th scope="col">id</th>
          <th scope="col">공시제출월</th>
          <th scope="col">상품명</th>
          <th scope="col">은행명</th>
          <th scope="col">{{ period }}개월</th>
          <th scope="col">상품 상세정보</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(deposit, index) in store.deposits" :key="index">
          <td>{{ deposit.fin_prdt_cd }}</td>
          <td>{{ deposit.dcls_month }}</td>
          <td>{{ deposit.fin_prdt_nm }}</td>
          <td>{{ deposit.kor_co_nm }}</td>
          <td>{{ deposit.intr_rate_06_1 }}</td>
          <td>{{ deposit.spcl_cnd }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useDepositStore } from '@/stores/deposit'
const store = useDepositStore()

const data = defineProps({
  period:String,
})

onMounted(() => {
  store.getDeposit()  // 컴포넌트가 마운트될 때 데이터 가져오기
  store.getBank()
})
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

thead th {
  background-color: #f2f2f2; /* Light gray header */
  border: 1px solid #ddd; /* Border for the header */
  padding: 8px;
}

tbody td {
  border: 1px solid #ddd; /* Border for the cells */
  padding: 8px;
}

tbody tr:nth-child(even) {
  background-color: #f9f9f9; /* Alternate row color */
}

tbody tr:hover {
  background-color: #f1f1f1; /* Hover effect */
}
</style>

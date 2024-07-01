<template>
  <div class="container">
    <h1>예적금 페이지 입니다</h1>
    <div class="row">
      <div class="col-md-3">
        <form @submit.prevent="changeType">
          <div class="form-group">
            <label for="bank-list">은행명을 선택하세요</label>
            <select class="form-control" id="bank-list" v-model="bankType">
              <option value="">전체은행</option>
              <option v-for="bank in store.bankList" :key="bank.kor_co_nm" :value="bank.kor_co_nm">
                {{ bank.kor_co_nm }}
              </option>
            </select>
          </div>
          <div class="form-group">
            <label for="period-list">예치기간</label>
            <select class="form-control" id="period-list" v-model="periodType">
              <option value="total">전체기간</option>
              <option value="6">6개월</option>
              <option value="12">12개월</option>
              <option value="24">24개월</option>
              <option value="36">36개월</option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary btn-block">확인</button>
        </form>
      </div>
      <div class="col-md-9">
        <DepositList
          :bank="bankType"
          :period="periodType"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import DepositList from '@/components/DepositList.vue'
import { useCounterStore } from '@/stores/counter'
import { ref , onMounted } from 'vue'

const store = useCounterStore()
const bankType = ref('')
const periodType = ref('total')

onMounted(() => {
  store.getDeposit()
  store.getBank()
})

const changeType = function () {
  // 필요한 로직을 여기에 추가하세요
}
</script>

<style scoped>
.container {
  padding: 20px;
  max-width: 1200px;
  margin: auto;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  font-size: 24px;
  color: #007bff;
}

.form-group {
  margin-bottom: 20px;
}

label {
  font-weight: bold;
}

.form-control {
  height: 45px;
  font-size: 16px;
  border-radius: 5px;
  border: 1px solid #ddd;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.form-control:focus {
  border-color: #007bff;
  box-shadow: 0 0 8px rgba(0, 123, 255, 0.25);
}

.btn {
  padding: 10px 20px;
  font-size: 16px;
  border-radius: 5px;
}

.btn-block {
  width: 100%;
}

.row {
  display: flex;
  justify-content: space-between;
}

@media (max-width: 768px) {
  .row {
    flex-direction: column;
  }

  .col-md-3, .col-md-9 {
    width: 100%;
  }

  .btn-block {
    width: 100%;
  }
}
</style>

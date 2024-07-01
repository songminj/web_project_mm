<template>
  <div class="container">
    <h1>내 주변 은행 찾기</h1>
    <div class="select-type">
      <div class="dropdown ddcustom">
        <select class="dropdown" v-model="store.sido" @change="changeSido">
          <option value="">--시도명--</option>
          <option v-for="sido in store.sidoList" :key="sido" :value="sido">
            {{ sido }}
          </option>
        </select>
      </div>
      <div class="dropdown ddcustom">
        <select class="dropdown" v-model="store.sigungu" @change="changeSigungu">
          <option value="">--시군구명--</option>
          <option v-for="sigungu in store.sigunguList" :key="sigungu" :value="sigungu">
            {{ sigungu }}
          </option>
        </select>
      </div>
      <div class="dropdown ddcustom">
        <select class="dropdown" v-model="store.bank" @change="changeBank">
          <option value="">--은행명--</option>
          <option v-for="bank in store.bankList" :key="bank.kor_co_nm" :value="bank.kor_co_nm">
            {{ bank.kor_co_nm }}
          </option>
        </select>
      </div>
    </div>
    
    <div class="map-container">
      <BankMap
        :county="store.sido"
        :city="store.sigungu"
        :bank="store.bank"
      />
    </div>
  </div>
</template>

<script setup>
import BankMap from '@/components/BankMap.vue'
import { useBankMapStore } from '@/stores/bankmap';
import { onMounted } from 'vue'

const store = useBankMapStore()

const changeSido = function(event) {
   store.sido = event.target.value
   store.uniqueSigungu(store.sido)
}

const changeSigungu = function(event) {
   store.sigungu = event.target.value
}

const changeBank = function(event) {
   store.bank = event.target.value
}

onMounted(() => {
  store.getSigungu()
  if (!store.bankList.length) {
    store.getBank()
  }
  store.resetValues()
})
</script>

<style scoped>
html, body, #app {
  height: 100%;
  margin: 0;
  padding: 0;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
  height: 100%;
}

h1 {
  color: #007bff;
  margin-bottom: 20px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.select-type {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  width: 100%;
  max-width: 600px;
}

.ddcustom {
  flex: 1;
  margin-right: 10px;
}

.ddcustom:last-child {
  margin-right: 0;
}

.dropdown {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  background-color: #f8f9fa;
  font-size: 16px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

.dropdown:focus {
  border-color: #007bff;
  box-shadow: 0 0 8px rgba(0, 123, 255, 0.25);
}

.map-container {
  flex: 1;
  width: 100%;
  max-width: 40rem; /* 지도의 최대 너비를 40rem으로 설정 */
  height: calc(100% - 150px); /* 부모 요소의 나머지 높이 사용 */
  border: 2px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-top: 20px;
}

@media (max-width: 768px) {
  .select-type {
    flex-direction: column;
    align-items: stretch;
  }
  .ddcustom {
    margin-right: 0;
    margin-bottom: 10px;
  }
  .map-container {
    height: 50vh; /* 모바일 화면에서는 높이를 조금 줄임 */
  }
}
</style>

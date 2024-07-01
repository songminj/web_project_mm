<template>
  <div class="container-fluid main-content">
    <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="@/assets/carousel-1.jpg" class="d-block w-100" alt="main1">
        </div>
        <div class="carousel-item">
          <img src="@/assets/carousel-2.jpg" class="d-block w-100" alt="main2">
        </div>
        <div class="carousel-item">
          <img src="@/assets/carousel-3.jpg" class="d-block w-100" alt="main3">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <div class="profile-recommend">
      <div class="row">
        <!-- Profile Section -->
        <div class="col-md-3 profile-section d-flex align-items-center" :class="{'d-none d-lg-flex': !isLgScreen}">
          <div v-if="store.isLogin">
            <img :src="userImage || defaultImage" alt="프로필 사진" class="profile-image">
            <div class="ms-3 profile-details">
              <p>닉네임: {{ store.auth?.nickname }}</p>
              <p>내 목표: {{ store.auth?.finance_goal }}</p>
              <p>내 자산: {{ store.auth?.assets }}</p>
              <router-link :to="{ name: 'ProfileView' }" class="btn btn-primary mt-2">프로필 페이지</router-link>
            </div>
          </div>
          <div v-else>
            <img :src="defaultImage" alt="기본 프로필 사진" class="profile-image">
            <div class="ms-3 profile-details">
              <p>안녕하세요!</p>
              <p>회원가입을 하고 더 많은 금융 서비스를 이용하세요!</p>
            </div>
          </div>
        </div>
        <!-- Main Section -->
        <div class="col-md-9 main-section">
          <div class="content">
            <h3>추천 예금 상품</h3>
            <div v-if="recommendedDeposit" class="product-card">
              <h2>{{ recommendedDeposit.fin_prdt_nm }} ({{ recommendedDeposit.kor_co_nm }})</h2>
              <div class="product-details">
                <p><strong class="type">상품명:</strong> {{ recommendedDeposit.fin_prdt_nm }}</p>
                <p><strong class="type">은행명:</strong> {{ recommendedDeposit.kor_co_nm }}</p>
                <p><strong class="type">가입 방법:</strong> {{ recommendedDeposit.join_way }}</p>
                <p><strong class="type">특별 조건:</strong> {{ recommendedDeposit.spcl_cnd }}</p>
                <p><strong class="type">가입 거부:</strong> {{ recommendedDeposit.join_deny }}</p>
                <p><strong class="type">가입 대상:</strong> {{ recommendedDeposit.join_member }}</p>
                <p><strong class="type">최대 한도:</strong> {{ recommendedDeposit.max_limit }}</p>
                <p><strong class="type">이자율(6개월):</strong> {{ recommendedDeposit.intr_rate_06_1 }}%</p>
                <p><strong class="type">이자율(12개월):</strong> {{ recommendedDeposit.intr_rate_12_1 }}%</p>
                <p><strong class="type">이자율(24개월):</strong> {{ recommendedDeposit.intr_rate_24_1 }}%</p>
                <p><strong class="type">이자율(36개월):</strong> {{ recommendedDeposit.intr_rate_36_1 }}%</p>
              </div>
            </div>
            <p v-else>추천 예금 상품을 불러오는 중입니다...</p>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import UserImagePath from '@/assets/default.jpg'
import DefaultImagePath from '@/assets/default_profile.png'

const store = useCounterStore()
const defaultImage = DefaultImagePath
const userImage = UserImagePath
const isLgScreen = ref(true)
const recommendedDeposit = ref(null)

const handleResize = () => {
  isLgScreen.value = window.innerWidth >= 992
}

onMounted(async () => {
  handleResize()
  window.addEventListener('resize', handleResize)

  await store.getDeposit()
  if (store.deposits.length > 0) {
    recommendedDeposit.value = store.deposits[0]  // 첫 번째 상품을 추천 상품으로 선택
  }
})

onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})
</script>

<style scoped>
.profile-section {
  background-color: #f8f9fa;
  padding: 20px;
  border-right: 1px solid #dee2e6;
  display: flex;
  align-items: center;
  width: 100%;
  max-width: 250px; /* 원하는 정사각형 크기로 설정 */
  height: 250px; /* 원하는 정사각형 크기로 설정 */
  border-radius: 8px; /* 약간의 둥근 모서리 추가 */
}

.profile-image {
  width: 80px; /* 프로필 이미지 크기 조정 */
  height: 80px; /* 프로필 이미지 크기 조정 */
  border-radius: 50%;
  object-fit: cover;
  margin-right: 10px; /* 이미지와 텍스트 사이의 간격 */
}

.profile-recommend {
  margin-top: 40px;
}

.type {
  width: 100px;
}

.ms-3 {
  margin-left: 0;
  text-align: left;
}

.profile-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

h2, h4 {
  margin: 5px 0;
  color: #333;
}

h1 {
  color: #333;
  margin-bottom: 10px;
}

.btn-primary {
  margin-top: 10px;
  font-size: 14px;
  padding: 5px 10px;
}

.main-section .content {
  padding: 20px;
}

.product-card {
  border: 1px solid #007bff;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  background-color: #f9f9f9;
}

.product-card h2 {
  margin-top: 0;
  color: #007bff;
}

.product-details p {
  margin: 8px 0;
}

.product-details strong {
  display: inline-block;
  width: 100px;
  color: #333;
}
</style>

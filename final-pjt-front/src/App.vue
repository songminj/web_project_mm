<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useCounterStore } from '@/stores/counter'
import ChatBot from './components/ChatBot.vue'

const store = useCounterStore()
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom border-body" style="background-color: #e3f2fd;">
      <div class="container-fluid">
        <RouterLink class="navbar-brand text-green" :to="{name:'MainView'}" style="font-weight: bold;">Home</RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <RouterLink v-if="!store.isLogin" class="nav-link text-blue" :to="{name: 'SigninView'}">Sign In</RouterLink>
              <RouterLink v-if="store.isLogin" class="nav-link text-blue" :to="{name: 'MainView'}" @click="store.logOut">Sign Out</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link text-blue" :to="{name:'ExchangeView'}">환율 계산하기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link text-blue" :to="{name:'BankView'}">은행 찾기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link text-blue" :to="{name:'DepositView'}">예적금 상품 확인하기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link text-blue" :to="{name:'ArticleListView'}">커뮤니티</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link text-blue" :to="{name:'ProfileView'}">내정보</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav> 
  </header>
  <main class="container mt-4">
    <ChatBot />
    <RouterView />
  </main>
</template>

<style scoped>
.text-green {
  color: #007bff !important; /* 밝은 초록색 */
}
.text-blue {
  color: #007bff !important; /* 파란색 */
}
.navbar-light .navbar-brand {
  color: #007bff !important; /* 밝은 초록색 */
}
.nav-link {
  font-weight: 500;
}
.nav-link:hover {
  color: #0056b3 !important; /* 어두운 파란색 */
}
.navbar-toggler {
  border-color: #007bff !important;
}
</style>

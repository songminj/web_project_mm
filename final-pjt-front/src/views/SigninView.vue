<template>
  <div class="back">
    <div class="container">
      <div class="login-box">
        <form @submit.prevent="logIn">
          <h2 class="text-center mb-4">로그인</h2>
          <div class="mb-3">
            <label for="username" class="form-label">ID</label>
            <input type="text" class="form-control" v-model.trim="username" id="username">
            <div id="idhelp" class="form-text">아이디를 입력해주세요.</div>
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" class="form-control" v-model.trim="password" id="password">
          </div>
          <div class="d-grid gap-2 buttons">
            <button type="submit" class="btn btn-primary">로그인하기</button>
            <button type="button" @click="toSignUp" class="btn btn-secondary">회원가입하기</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useCounterStore } from '@/stores/counter'

const router = useRouter()
const toSignUp = function () {
  router.push({name:'SignupView'})
}

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
.back {
  background-color: #f8f9fa;
}

.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-box {
  width: 100%;
  max-width: 400px;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

h2 {
  font-size: 24px;
  color: #333;
}

.form-label {
  font-weight: bold;
  color: #495057;
}

.form-text {
  font-size: 14px;
  color: #6c757d;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out;
  margin-right: 3px;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

.btn-secondary {
  background-color: #6c757d;
  border-color: #6c757d;
  transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out;
}

.btn-secondary:hover {
  background-color: #5a6268;
  border-color: #545b62;
}

.buttons {
  display: flex;
  justify-content: center;
}
</style>

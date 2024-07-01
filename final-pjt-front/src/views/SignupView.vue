<template>
  <div class="back">
    <div class="container field">
      <div class="title">
        회원가입
      </div>
      <form @submit.prevent="signUp()" class="signup-form">
        <div class="input-group mb-3">
          <span class="input-group-text">ID</span>
          <input type="text" class="form-control" placeholder="" aria-label="Username" v-model.trim="username" id="username">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">닉네임</span>
          <input type="text" class="form-control" placeholder="닉네임을 입력해주세요" aria-label="nickname" v-model.trim="nickname" id="nickname">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">Password</span>
          <input type="password" class="form-control" placeholder="비밀번호를 입력해주세요" aria-label="password1" v-model.trim="password1" id="password1">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">Password 재입력</span>
          <input type="password" class="form-control" placeholder="비밀번호를 다시 입력해주세요" aria-label="password2" v-model.trim="password2" id="password2">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">이메일</span>
          <input type="email" class="form-control" placeholder="" aria-label="email" v-model.trim="email" id="email">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">금융목표</span>
          <input type="text" class="form-control" placeholder="금융 목표를 적어주세요!" aria-label="financeGoal" v-model.trim="finance_goal" id="finance_goal">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">현재 자산</span>
          <input type="text" class="form-control" placeholder="보유 자산액을 입력해주세요" aria-label="financeGoal" v-model.trim="assets" id="assets">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">나이</span>
          <input type="text" class="form-control" placeholder="" aria-label="financeGoal" v-model.trim="age" id="age">
        </div>
        <div class="input-group mb-3">
          <span class="input-group-text">연봉</span>
          <input type="text" class="form-control" placeholder="연봉을 입력해주세요" aria-label="financeGoal" v-model.trim="salary" id="salary">
        </div>
        <div class="d-grid gap-2 buttons">
          <input type="submit" value="가입" class="btn btn-primary">
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)
const finance_goal = ref(null)
const age = ref(null)
const assets = ref(null)
const salary = ref(null)
const nickname = ref(null)


const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    finance_goal: finance_goal.value,
    age : age.value,
    assets : assets.value,
    salary: salary.value,
    nickname: nickname.value
  }
  store.signUp(payload)
}
</script>

<style scoped>
.back {
  background-color: #f8f9fa;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.field {
  width: 100%;
  max-width: 600px;
  padding: 20px;
}

.title {
  margin-bottom: 30px;
  font-size: 2.5rem;
  color: #007bff;
  text-align: center;
}

.signup-form {
  background-color: #ffffff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
}

.input-group-text {
  font-weight: bold;
  background-color: #007bff;
  color: #fff;
}

.input-group .form-control {
  border-left: none;
}

.input-group .form-control:focus {
  box-shadow: none;
  border-color: #007bff;
}

.btn-primary {
  background-color: #007bff;
  border-color: #007bff;
  transition: background-color 0.2s ease-in-out, border-color 0.2s ease-in-out;
}

.btn-primary:hover {
  background-color: #0056b3;
  border-color: #0056b3;
}

.buttons {
  display: flex;
  justify-content: center;
}
</style>

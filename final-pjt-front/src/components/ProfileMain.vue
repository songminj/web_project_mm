<template>
  <div>
    <h1>기본 정보 수정</h1>
    <div class="row">
      <div class="col-12 col-md-6">
        <img src="@/assets/default.jpg" alt="" class="profile-img">
      </div>
      <div class="col-12 col-md-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">내 정보</h5>
            <p class="card-text"><strong>이름:</strong> {{ store.auth?.username ?? '' }}</p>
            <p class="card-text"><strong>닉네임:</strong> {{ store.auth?.nickname ?? '' }}</p>
            <p class="card-text"><strong>이메일:</strong> {{ store.auth?.email ?? '' }}</p>
            <p class="card-text"><strong>금융 목표:</strong> {{ store.auth?.finance_goal ?? '' }}</p>
            <p class="card-text"><strong>나이:</strong> {{ store.auth?.age ?? '' }}</p>
            <p class="card-text"><strong>보유 자산:</strong> {{ store.auth?.assets ?? '' }}</p>
            <p class="card-text"><strong>연봉:</strong> {{ store.auth?.salary ?? '' }}</p>
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#updateInfoModal">
              내정보 수정하기
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- updateInfoModal -->
  <div class="modal fade" id="updateInfoModal" tabindex="-1" aria-labelledby="updateInfoModal" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="updateInfoModal">내정보 수정하기</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <form class="signup-form">
            <div class="input-group mb-3">
              <span class="input-group-text">닉네임</span>
              <input type="text" class="form-control" placeholder="닉네임을 입력해주세요" aria-label="nickname" v-model.trim="store.auth.nickname" id="nickname">
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text">이메일</span>
              <input type="email" class="form-control" placeholder="" aria-label="email" v-model.trim="store.auth.email" id="email">
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text">금융목표</span>
              <input type="text" class="form-control" placeholder="금융 목표를 적어주세요!" aria-label="financeGoal" v-model.trim="store.auth.finance_goal" id="finance_goal">
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text">현재 자산</span>
              <input type="text" class="form-control" placeholder="보유 자산액을 입력해주세요" aria-label="assets" v-model.trim="store.auth.assets" id="assets">
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text">나이</span>
              <input type="text" class="form-control" placeholder="" aria-label="age" v-model.trim="store.auth.age" id="age">
            </div>
            <div class="input-group mb-3">
              <span class="input-group-text">연봉</span>
              <input type="text" class="form-control" placeholder="연봉을 입력해주세요" aria-label="salary" v-model.trim="store.auth.salary" id="salary">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-primary" @click="handleSave">수정하기</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';

const store = useCounterStore()

onMounted(() => {
  store.getAuth()
})

const handleSave = async () => {
  await store.changeAuth()
  const modal = bootstrap.Modal.getInstance(document.getElementById('updateInfoModal'))
  modal.hide()
}
</script>

<style scoped>
.profile-img {
  width: 100%;
  max-width: 250px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 20px;
}

.card {
  margin: 20px 0;
}

.card-body {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.card-text {
  margin: 0;
}
</style>

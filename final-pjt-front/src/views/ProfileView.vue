<template>
  <div>
    <h1>{{ store.auth?.username }}님 오늘도 부자되세요!</h1>
    <div class="row back">
      <div class="col-3 sidebar">
        <nav>
          <a class="nav-link content" @click="changeType('main')">내 정보</a>
          <a class="nav-link content" @click="changeType('portfolio')">가입한 예적금</a>
        </nav>
      </div>
      <div class="col-9 content-area">
        <div v-if="type === 'main'">
          <ProfileMain />
        </div>
        <div v-else-if="type === 'portfolio'">
          <ProfilePortfolio />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import ProfileMain from '@/components/ProfileMain.vue'
import ProfilePortfolio from '@/components/ProfilePortfolio.vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
const type = ref('main')

onMounted(() => {
  store.getAuth()
})

const changeType = function(typeName) {
  type.value = typeName
}
</script>

<style scoped>
.back {
  padding: 20px;
}

h1 {
  text-align: center;
  margin: 30px;
  font-size: 1.8rem;
  color: #0056b3;
}

.sidebar {
  padding-right: 15px;
}

nav {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 20px;
}

.nav-link {
  padding: 10px 15px;
  text-decoration: none;
  color: #0056b3;
  border-radius: 4px;
  background-color: #c3dff4;
  text-align: center;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.nav-link:hover {
  background-color: #0056b3;
  color: #fff;
}

.row {
  display: flex;
  flex-wrap: wrap;
}

.col-3 {
  flex: 1 0 25%;
  max-width: 25%;
  padding-right: 15px;
}

.col-9 {
  flex: 1 0 75%;
  max-width: 75%;
}

.content-area {
  padding-left: 15px;
}

@media (max-width: 768px) {
  .col-3, .col-9 {
    flex: 1 0 100%;
    max-width: 100%;
  }

  .content-area {
    padding-left: 0;
  }
}
</style>

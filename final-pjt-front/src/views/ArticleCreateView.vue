<template>
  <div class="container">
    <h3>게시글 생성 페이지</h3>
    <form @submit.prevent="createArticle">
      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <input type="text" v-model.trim="title" class="form-control" id="title" placeholder="제목을 입력하세요">
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">내용</label>
        <textarea v-model.trim="content" class="form-control" id="content" rows="5" placeholder="내용을 입력하세요"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">저장</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const title = ref('')
const content = ref('')
const router = useRouter()

const createArticle = async () => {
  try {
    const response = await axios.post(
      `${store.API_URL}/articles/`,
      { title: title.value, content: content.value },
      { headers: { Authorization: `Token ${store.token}` } }
    )
    router.push({ name: 'ArticleListView' })
  } catch (error) {
  }
}
</script>

<style scoped>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

h3 {
  text-align: center;
  margin-bottom: 20px;
  color: #0056b3;
}

.form-label {
  font-weight: bold;
}

.form-control {
  border-radius: 4px;
  border: 1px solid #ddd;
  padding: 10px;
}

.mb-3 {
  margin-bottom: 20px;
}

.btn-primary {
  display: block;
  width: 100%;
  padding: 10px 0;
  background-color: #0056b3;
  border-color: #0056b3;
  color: white;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-primary:active {
  background-color: #1e70c7;
}
</style>

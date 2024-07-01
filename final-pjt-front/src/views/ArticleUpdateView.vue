<template>
  <div>
    <div class="container">
      <h3>업데이트 페이지</h3>
      <form @submit.prevent="handleUpdate">
        <div class="mb-3">
          <label class="form-label" for="title">제목</label>
          <input type="text" v-model.trim="title" class="form-control" id="title" placeholder="제목을 입력하세요">
        </div>
        <div class="mb-3">
          <label class="form-label" for="content">내용</label>
          <textarea v-model.trim="content" class="form-control" id="content" rows="3"></textarea>
        </div>
        <input type="submit" value="수정하기" class="btn btn-primary">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const title = ref('')
const content = ref('')

onMounted(() => {
  const id = parseInt(route.params.id)
  const article = store.getDetailArticle(id)
  if (article) {
    title.value = article.title
    content.value = article.content
  }
})

const handleUpdate = async () => {
  const id = parseInt(route.params.id)
  await store.updateArticle(id, title.value, content.value)
  const updatedArticle = store.getDetailArticle(id)
  await store.getArticles()
  router.push({ name: 'ArticleDetailView', params: { id } })
}
</script>

<style scoped>
.container {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  max-width: 600px;
  margin: 0 auto;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h3 {
  color: #0056b3;
  text-align: center;
  margin-bottom: 20px;
}

.form-label {
  color: #0056b3;
  font-weight: bold;
}

.form-control {
  border: 1px solid #0056b3;
  border-radius: 4px;
}

.form-control:focus {
  border-color: #0056b3;
  box-shadow: 0 0 5px rgba(0, 86, 179, 0.3);
}

.btn-primary {
  background-color: #2f6fb3;
  border-color: #2f6fb3;
  color: #fff;
  font-weight: bold;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  display: block;
  width: 100%;
}

.btn-primary:hover {
  background-color: #245a91;
  border-color: #245a91;
}

.mb-3 {
  margin-bottom: 15px;
}
</style>

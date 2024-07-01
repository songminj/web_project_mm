<template>
  <div class="container">
    <h1>MM 커뮤니티</h1>
    <div v-if="store.articles.length">
      <table class="table">
        <thead>
          <tr>
            <th class="num">작성 시간</th>
            <th class="title">제목</th>
            <th class="author">작성자</th>
          </tr>
        </thead>
        <tbody>
          <ArticleList
            v-for="article in store.articles"
            :key="article.id"
            :article="article"
          />
        </tbody>
      </table>
    </div>
    <div v-else>
      {{ store.error || '게시글이 없습니다' }}
    </div>
    <button class="btn btn-primary" @click="createArticle">게시글 작성하기</button>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const router = useRouter()
const store = useCounterStore()
const createArticle = function () {
  router.push({ name: 'ArticleCreateView' })
}

import ArticleList from '@/components/ArticleList.vue'

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
.container {
  margin-top: 20px;
  padding: 20px;
}

h1 {
  text-align: center;
  font-size: 2rem;
  color: #0056b3;
  margin-bottom: 30px;
  font-family: 'Arial', sans-serif;
}

table {
  margin: auto;
  width: 100%;
  max-width: 800px;
  border-radius: 5px;
  border-collapse: collapse;
  background-color: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

thead {
  background-color: #dee6f8;
  text-align: center;
  font-weight: bold;
}

.table td, .table th {
  border-bottom: 1px solid #c8d4e6;
  height: 40px;
  font-size: 16px;
  padding: 10px;
}

.num {
  width: 150px;
}

.title {
  width: 300px;
}

.author {
  width: 150px;
}

tbody {
  text-align: center;
}

tbody .title {
  text-align: left;
}

button {
  width: 30%;
  height: 40px;
  font-size: 15px;
  border: 0;
  outline: 1.5px solid #316dac;
  border-radius: 5px;
  background-color: #0056b3;
  margin-top: 20px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  cursor: pointer;
  transition: background-color 0.3s ease, outline 0.3s ease;
}

button:hover {
  background-color: #0056b3;
  outline: 1.5px solid #2f6fb3;
}

button:active {
  background-color: #2f6fb3;
}
</style>

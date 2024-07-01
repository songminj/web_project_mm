<template>
  <div class="container">
    <div class="margin30">
      <div v-if="article">
        <div class="title">{{ article.title }}</div>
        <div class="content">
          <p>{{ article.content }}</p>
        </div>
        <div class="buttons">
          <button v-if="article.user_id === store.auth.id" @click="store.deleteArticle(article.id)" class="btn btn-danger btn-sm">삭제</button>
          <button v-if="article.user_id === store.auth.id" @click="goUpdate()" class="btn btn-primary btn-sm">수정</button>
          <button @click="goBack()" class="btn btn-secondary btn-sm">뒤로가기</button>
        </div>
        <div class="comment-section">
          <h3>댓글보기</h3>
          <form @submit.prevent="addComment(article.id)" class="comment-form">
            <input type="text" v-model="content" placeholder="댓글을 입력하세요" class="comment-input">
            <button type="submit" class="btn btn-success comment-submit">댓글 작성하기</button>
          </form>
          <div class="comment-box">
            <div v-for="comment in store.comments" :key="comment.id" class="comment row">
              <div class="comment-content">
                <strong>{{ comment.nickname }}:</strong> {{ comment.content }}
              </div>
              <div v-if="comment.user_id === store.auth.id" class="right-buttons">
                <button class="btn btn-danger btn-sm" @click="store.deleteComment(article.id, comment.id)">×</button>
                <button type="button" class="btn btn-primary btn-sm" data-bs-toggle="modal" data-bs-target="#updateCommentModal" @click="getNewComment(comment)">
                  수정
                </button>

                <div class="modal fade" id="updateCommentModal" tabindex="-1" aria-labelledby="updateCommentModalLabel" aria-hidden="true">
                  <div class="modal-dialog">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="updateCommentModalLabel">댓글 수정하기</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                        <input type="text" v-model="newComment" class="form-control" placeholder="댓글을 수정하세요">
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" @click="resetComment()">닫기</button>
                        <button type="button" class="btn btn-primary" data-bs-dismiss="modal" @click="updateComment(article.id, comment.id, newComment)">저장</button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup>
import { onMounted, ref, watch } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()
const store = useCounterStore()
const article = ref(null)
const content = ref('')
const newComment = ref('')

const getArticle = async () => {
  const id = parseInt(route.params.id)
  await store.getArticles()
  await store.getAuth()
  article.value = store.getDetailArticle(id)
  await store.getComments(id)
}

const goBack = function () {
  router.push({ name: 'ArticleListView' })
}

const goUpdate = function () {
  router.push({ name: 'ArticleUpdateView', params: { id: route.params.id } })
}

const getNewComment = function (comment) {
  newComment.value = comment.content
}

const addComment = async function (articleId) {
  await store.createComment(content.value, articleId)
  content.value = ''
  await store.getComments(articleId)
}

const updateComment = async function (articleId, commentId, newContent) {
  await store.updateComment(articleId, commentId, newContent)
  await store.getComments(articleId)
}

const resetComment = function () {
  newComment.value = ''
}

onMounted(() => {
  getArticle()
})

watch(route, () => {
  getArticle()
})
</script>


<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.margin30 {
  margin: 30px;
}

.title {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 20px;
  color: #0056b3;
}

.content {
  margin-bottom: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #fff;
}

.buttons {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 20px;
  gap: 5px;
}

.btn-sm {
  padding: 5px 10px;
  font-size: 14px;
}

.btn {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  margin-left: 10px;
}

.new-comment {
  width: 100%;
}

.comment-section {
  margin-top: 40px;
}

.comment-section h3 {
  margin-bottom: 20px;
  color: #0056b3;
}

.comment-form {
  display: flex;
  margin-bottom: 20px;
}

.comment-input {
  flex-grow: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px 0 0 4px;
  border-right: none;
}

.comment-submit {
  padding: 10px 20px;
  border-radius: 0 4px 4px 0;
  background-color: #2f6fb3;
  color: #fff;
}

.comment-box {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 10px;
}

.comment-button {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.comment-content {
  flex: 1;
}

.comment {
  padding: 10px;
  border-bottom: 1px solid #eee;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.comment:last-child {
  border-bottom: none;
}

.right-buttons {
  display: flex;
  gap: 5px;
}

.right-buttons button {
  font-size: 12px;
  padding: 5px 10px;
}

.modal-header {
  border-bottom: 1px solid #c8d4e6;
  padding: 1rem 1.5rem;
}

.modal-title {
  font-size: 1.25rem;
  color: #0056b3;
}

.modal-body {
  padding: 1rem 1.5rem;
}

.modal-footer {
  border-top: 1px solid #dee2e6;
  padding: 1rem 1.5rem;
  display: flex;
  justify-content: flex-end;
  gap: 10px;
}

.form-control {
  border-radius: 4px;
  border: 1px solid #ddd;
  padding: 10px;
}

.btn-primary {
  background-color: #2f6fb3;
  border-color: #0056b3;
  color: white;
}

.btn-primary:hover {
  background-color: #2f6fb3;
}

.btn-primary:active {
  background-color: #2f6fb3;
}

.btn-secondary {
  background-color: #6c757d;
  border-color: #6c757d;
  color: white;
}
</style>

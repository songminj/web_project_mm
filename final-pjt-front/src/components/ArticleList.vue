<template>
  <tr class="body">
    <td>{{ dateTime(article.created_at) }}</td>
    <td class="title">
      <RouterLink :to="{ name: 'ArticleDetailView', params: { id: article.id } }">
        {{ article.title }}
      </RouterLink>
    </td>
    <td>{{ article.author_nickname }}</td>
  </tr>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const props = defineProps({
  article: Object,
})

const dateTime = function (time) {
  return time.toString().split('T')[0]
}
</script>

<style scoped>
.body {
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.body:hover {
  background-color: #c8d4e6;
}

.title {
  text-align: left;
}
</style>

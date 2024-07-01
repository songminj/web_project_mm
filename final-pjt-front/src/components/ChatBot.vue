<template>
  <div class="chatbot-container" :class="{ open: isOpen }">
    <div class="chatbot-header" @click="toggleChat">
      <font-awesome-icon :icon="isOpen ? 'times' : 'headset'" />
    </div>
    <div class="chatbot-body" v-show="isOpen">
      <div class="messages">
        <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.role]">
          <div class="bubble">
            <span v-if="msg.role === 'user'">User: </span>{{ msg.content }}
          </div>
        </div>
      </div>
      <div class="input-container">
        <input type="text" v-model="message" placeholder="Type your message here" @keyup.enter="sendMessage" />
        <button @click="sendMessage">
          <font-awesome-icon icon="paper-plane" />
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isOpen: false,
      message: '',
      messages: [],
    };
  },
  methods: {
    toggleChat() {
      this.isOpen = !this.isOpen;
    },
    async sendMessage() {
      if (this.message.trim() === '') return;

      const userMessage = this.message;
      this.messages.push({ role: 'user', content: userMessage });
      this.message = '';

      try {
        const res = await axios.post('http://127.0.0.1:8000/chatbot/', {
          message: userMessage,
        });
        this.messages.push({ role: 'bot', content: res.data.response });
      } catch (error) {
        this.messages.push({ role: 'bot', content: 'Error communicating with the server.' });
      }
    },
  },
};
</script>

<style scoped>
.chatbot-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: #0056b3; /* 밝은 초록색 */
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  cursor: pointer;
  transition: width 0.3s ease, height 0.3s ease, border-radius 0.3s ease, right 0.3s ease;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 9999;
}

.chatbot-container.open {
  width: 350px;
  height: 500px;
  border-radius: 15px;
  right: 20px; /* Adjust as needed */
}

.chatbot-header {
  position: absolute;
  top: 15px;
  right: 15px;
  cursor: pointer;
}

.chatbot-body {
  display: flex;
  flex-direction: column;
  padding: 10px;
  height: 100%;
  overflow: hidden;
  background-color: white;
}

.chatbot-container.open .chatbot-body {
  display: flex;
}

.messages {
  flex: 1;
  overflow-y: auto;
  margin-bottom: 10px;
}

.message {
  display: flex;
  margin-bottom: 10px;
}

.message.user {
  justify-content: flex-end;
}

.message.bot {
  justify-content: flex-start;
}

.bubble {
  max-width: 70%;
  padding: 10px;
  border-radius: 20px;
  color: white;
}

.message.user .bubble {
  background-color: #007bff; /* 파란색 */
  border-bottom-right-radius: 0;
}

.message.bot .bubble {
  background-color: #e5e5ea;
  color: black;
  border-bottom-left-radius: 0;
}

.input-container {
  display: flex;
  align-items: center;
  border-top: 1px solid #ccc;
  padding: 10px;
  background-color: white;
}

input[type="text"] {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 20px;
  margin-right: 10px;
}

button {
  padding: 10px;
  background-color: #28a745; /* 밝은 초록색 */
  color: white;
  border: none;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
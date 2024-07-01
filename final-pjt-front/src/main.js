import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { useKakao } from 'vue3-kakao-maps/@utils'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faHeadset, faTimes, faPaperPlane } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faHeadset, faTimes, faPaperPlane)

const app = createApp(App)
const pinia = createPinia()

useKakao('7b150224685920869c0278144db4e10c', ['clusterer', 'services', 'drawing'])

pinia.use(piniaPluginPersistedstate)
// app.use(createPinia())
app.use(pinia)
app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')

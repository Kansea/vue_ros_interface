import axios from 'axios'
import VueAxios from 'vue-axios'
import { createApp } from 'vue'
import RobotApp from './Robot.vue'


const app = createApp(RobotApp)
app.use(VueAxios, axios)
app.mount('#app')

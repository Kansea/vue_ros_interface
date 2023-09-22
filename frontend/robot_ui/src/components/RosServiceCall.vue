<template>
  <div class="ros service call">
    <div class="intput_number">
      <p>number a</p>
      <input type="number" v-model.number="a" placeholder="input a number">
    </div>
    <div class="intput_number">
      <p>number b</p>
      <input type="number" v-model.number="b" placeholder="input a number">
    </div>
    <button @click="Servicecall">Ros Service Call</button>
    <div class="output_number">
      <p>a + b = {{ res }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

axios.defaults.baseURL = 'http://127.0.0.1:8000/robot_api'

export default {
  name: "RosServiceCall",

  setup() {

    // const csrf_token = ref('')
    const res = ref('')
    const a = ref('')
    const b = ref('')

    function Servicecall() {
      // axios
      //   .get('/get_token')
      //   .then((response) => {
      //     if (response.status === 200) {
      //       csrf_token.value = response.data.token
      //       axios.defaults.headers.common['Authorization'] = 'Bearer ${csrf_token.value}'
      //     }
      //   })
      //   .catch((error) => {
      //     console.log(error)
      //   })
      //   .finally(() => {})

      axios
        .post('/add', {
          "a": a.value,
          "b": b.value,
        })
        .then((response) => {
          if (response.status === 200) {
            res.value = response.data.res_add
          }
        })
        .catch((error) => {
          console.log(error)
        })
        .finally(() => {})
    }

    return {
      Servicecall, res, a, b
    }
  }

}

</script>

<style scoped>
  div {
    margin: 40px 0 0;
  }
  button {
    margin: 40px 0 0;
  }
</style>

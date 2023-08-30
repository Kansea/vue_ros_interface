<template>
  <div class="send button">
    <button @click="increment">
      {{ count }}
    </button>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  name: "ButtonTest",

  setup() {
    const count = ref(0)

    function increment() {
      count.value++
    }

    return {
      count, increment
    }
  }
}
</script>

<style scoped>
  button {
    margin: 60px 0 0;
  }
</style>

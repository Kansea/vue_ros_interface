<template>
  <div class="robot">
    <h1>{{ msg }}</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloRobot',
  props: {
    msg: String
  }
}
</script>

<style scoped>
h1 {
  margin: 40px 0 0;
}
</style>

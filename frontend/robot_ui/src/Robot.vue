<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloRobot msg="Welcome to Robot Web App Framework"/>
  <RosServiceCall/>

</template>

<script>
import HelloRobot from './components/HelloRobot.vue'
import RosServiceCall from './components/RosServiceCall.vue'

export default {
  name: 'RobotApp',
  components: {
    HelloRobot,
    RosServiceCall,
  }
}
</script>

<style>
#app {
  font-family: Helvetica, Arial;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

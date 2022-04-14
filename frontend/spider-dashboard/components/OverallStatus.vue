<template>
  <div class="wrapper">
    <div class="status-animation-ok" :class="animationType"></div>
    <h1>OverallStatus</h1>
  </div>
</template>

<script setup>
</script>

<style scoped>
.wrapper {
  background: #fff;
  padding: 50px 60px;
  box-shadow: 0 20px 60px rgb(0 0 0 / 10%);
  border-radius: 6px;
  color: #131a26;
  margin: -60px 185px 10px 185px;
  display: flex;
}

h1 {
  font-family: "Roboto", sans-serif;
}

.status-animation-ok {
  background: rgba(59, 214, 113, 1);
  border-radius: 50%;
  margin: 10px;
  width: 60px;
  height: 60px;
  transform: scale(1);
  animation: pulse-ok 2s infinite;
  margin: auto 25px 11px 0;
}

@keyframes pulse-ok {
  0% {
    transform: scale(0.85);
    box-shadow: 0 0 0 0 rgba(59, 214, 113, 0.7);
  }

  70% {
    transform: scale(1);
    box-shadow: 0 0 0 10px rgba(59, 214, 113, 0);
  }

  100% {
    transform: scale(0.85);
    box-shadow: 0 0 0 0 rgba(59, 214, 113, 0);
  }
}
</style>
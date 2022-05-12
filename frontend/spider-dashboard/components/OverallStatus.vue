<template>
  <div class="status-wrapper">
    <div class="card">
      <div class="status-animation-ok" :class="animationType"></div>
      <h1>OverallStatus</h1>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>

.status-wrapper {
  position: absolute;
  left: 50%;
  transform: translate(-50%, 0);
  max-width: 1000px; 
  width: -webkit-fill-available;
  margin: -80px auto 67px auto;
  padding: 20px;
}
.status-animation-ok {
  background: rgba(59, 214, 113, 1);
  border-radius: 50%;
  margin: 10px;
  margin-right: 30px;
  width: 60px;
  height: 60px;
  transform: scale(1);
  animation: pulse-ok 2s infinite;
}
.card{
  @apply flex items-center;
  @apply flex-col sm:flex-row;
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
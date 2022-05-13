<template>
  <div class="background-wrapper">
    <div class="text-wrapper">
      <h1>TIN-Dashboard</h1>
      <p>Service Status</p>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.background-wrapper {
  background-color: #131a26;
  width: 100%;
  height: 200px;
  position: relative;
  top: 0px;
  z-index: -10;
}

p {
  font-size: 24px;
  font-weight: bold;
}

.text-wrapper {
  padding: 48px;
  margin: auto;
  max-width: 1100px;
  display: flex;
  color: white;
  justify-content: space-between;
  font-family: "Roboto", sans-serif;
  @apply flex items-center;
  @apply flex-col sm:flex-row;
}
</style>
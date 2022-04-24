<template>
  <div>
    <h1>Services</h1>
    <div class="wrapper">
      <template :key="spider.id" v-for="spider in spiders">
        <ServicesRow :spider="spider" />
      </template>
    </div>
  </div>
</template>




<script setup>
const { data } = await useFetch("http://localhost:8000/zyte/spiders");
let spiders = data._value;
</script>

<style scoped>
.wrapper {
  background: #fff;
  padding: 60px;
  box-shadow: 0 20px 60px rgb(0 0 0 / 10%);
  border-radius: 6px;
  color: #131a26;
  margin: 20px 185px;
}

h1 {
  margin: 20px 185px;
  font-family: "Roboto", sans-serif;
}
</style>
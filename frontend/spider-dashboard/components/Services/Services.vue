<template>
  <div>
    
    <div class="wrapper">
      <div class="card">
        <h1 class="mb-5">Services</h1>
        <template :key="spider.id" v-for="spider in spiders">
          <ServicesRow :spider="spider" />
        </template>
      </div>
    </div>
  </div>
</template>




<script lang="ts" setup>
interface Spider {
  id: string;
}

interface SpidersFetch{
  data: Spider[];
}

const { data } = await useFetch<SpidersFetch>("http://localhost:8000/zyte/spiders");

let spiders = data.value;
</script>

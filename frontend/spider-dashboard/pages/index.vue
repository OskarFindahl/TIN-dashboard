<template>
  <NuxtLayout name="custom">
    <BackgroundInfo />
    <OverallStatus />

    <Services />
  </NuxtLayout>
</template>


<script>
// This will also work in `<script setup>`

definePageMeta({
  layout: false,
});
</script>

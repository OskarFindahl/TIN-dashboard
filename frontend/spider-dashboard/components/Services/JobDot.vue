<template>
  <div class="dotWrapper" :class="colorClass"></div>
</template>

<script setup>
const props = defineProps(["job", "fill"]);
let colorClass = "";

if (!props.fill) {
  const errors = props.job.num_errors;
  const items = props.job.num_items;

  if (errors > 0) {
    colorClass = "color-error";
  }

  if (errors == 0 && items < 10) {
    colorClass = "color-warning";
  }

  if (errors == 0 && items >= 10) {
    colorClass = "color-ok";
  }
}
</script>

<style scoped>
.dotWrapper {
  height: 30px;
  width: 6px;
  background-color: rgb(189, 189, 189);
  border-radius: 6px;
  margin-right: 5px;
}

.color-ok {
  background-color: rgb(59, 214, 113);
}

.color-error {
  background-color: red;
}

.color-warning {
  background-color: rgb(159, 252, 191);
}
</style>
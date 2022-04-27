<template >
  <div>
    <div class="title-wrapper">
      <h3>
        {{ spiderName }} |
        <span class="percentage" :class="colorPrecentage"
          >{{ faultPercentage }}%</span
        >
      </h3>
      <div class="status-wrapper">
        <div class="status-animation" :class="animationType"></div>
        <h3 class="percentage" :class="colorPrecentage">
          {{ statusText }}
        </h3>
      </div>
    </div>

    <div class="dot-wrapper">
      <template v-for="job in jobs" :key="job.id">
        <ServicesJobDot :job="job" :fill="false" />
      </template>
      <template v-for="fill in extraFillDots" :key="fill">
        <ServicesJobDot :fill="true" />
      </template>
      <template> </template>
    </div>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps(["spider"]);
let numberOfDots = 90;
let spiderName = props.spider.id;
spiderName = spiderName[0].toUpperCase() + spiderName.substring(1);

interface JobData {
  id: string,
  num_errors: number,
  num_items: number,
  date: string,
  spider: String,
}

const { data: response } = await useFetch<JobData[]>(
  `http://localhost:8000/zyte/job-data?spider=${props.spider.id}`
);

let jobs = response.value;

const extraFillDots =
  numberOfDots - jobs.length < 0 ? 0 : numberOfDots - jobs.length;

let errors = 0;
let toFewItems = 0;

jobs.forEach((job) => {
  if (job.num_errors > 0) {
    errors++;
  }
  if (job.num_items < 10 && job.num_errors == 0) {
    toFewItems++;
  }
});

const faultPercentage = 100 - (100 * (errors + toFewItems * 0.5)) / jobs.length;

let colorPrecentage = "";
let statusText = "Operational";
let animationType = "status-animation-ok";

if (faultPercentage < 90) {
  colorPrecentage = "color-warning";
  animationType = "status-animation-warning";
  statusText = "Warning";
}
if (faultPercentage < 40) {
  colorPrecentage = "color-error";
  animationType = "status-animation-error";
  statusText = "Down";
}
</script>

<style>
  .dotWrapper:nth-last-child(-n+70) {
    @apply hidden sm:block;
  }
  .dotWrapper:nth-last-child(-n+50) {
    @apply hidden lg:block;
  }
</style>

<style scoped>
.dot-wrapper {
  display: flex;
  padding-bottom: 29px;
  border-bottom: 1px solid #d0cece;
}

h3 {
  font-family: "Roboto", sans-serif;
  font-size: 18px;
  font-weight: 400;
}

.percentage {
  color: rgb(59, 214, 113);
}

.color-ok {
  color: rgb(59, 214, 113);
}

.color-error {
  color: red;
}

.color-warning {
  color: #ffcc11;
}

.title-wrapper {
  display: flex;
  justify-content: space-between;
  @apply flex-col sm:flex-row
}

.status-wrapper {
  display: flex;
  justify-content: left;
  width: 120px;

}

.status-animation-ok {
  background: rgba(59, 214, 113, 1);
  border-radius: 50%;
  margin: 10px;
  height: 12px;
  width: 12px;
  transform: scale(1);
  animation: pulse-ok 2s infinite;
  margin: auto 15px 23px 0px;
}

.status-animation-warning {
  background: #ffcc11;
  border-radius: 50%;
  margin: 10px;
  height: 12px;
  width: 12px;
  transform: scale(1);
  animation: pulse-warning 2s infinite;
  margin: auto 15px 23px 0px;
}

.status-animation-error {
  background: red;
  border-radius: 50%;
  margin: 10px;
  height: 12px;
  width: 12px;
  transform: scale(1);
  animation: pulse-error 2s infinite;
  margin: auto 15px 23px 0px;
}

@keyframes pulse-ok {
  0% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(59, 214, 113, 0.7);
  }

  70% {
    transform: scale(1);
    box-shadow: 0 0 0 10px rgba(59, 214, 113, 0);
  }

  100% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(59, 214, 113, 0);
  }
}

@keyframes pulse-warning {
  0% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(255, 204, 17, 0.7);
  }

  70% {
    transform: scale(1);
    box-shadow: 0 0 0 10px rgba(59, 214, 113, 0);
  }

  100% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(59, 214, 113, 0);
  }
}

@keyframes pulse-error {
  0% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(255, 0, 0, 0.7);
  }

  70% {
    transform: scale(1);
    box-shadow: 0 0 0 10px rgba(59, 214, 113, 0);
  }

  100% {
    transform: scale(0.95);
    box-shadow: 0 0 0 0 rgba(59, 214, 113, 0);
  }
}
</style>
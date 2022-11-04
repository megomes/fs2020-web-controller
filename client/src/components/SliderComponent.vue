<template>
  <div class="flex flex-col h-full items-center gap-10">
    {{ props.name }}
    <q-slider
      v-model="slider"
      :min="props.min"
      :max="props.max"
      :step="props.step"
      @change="slider_changed"
      @pan="slider_started"
      color="blue-8"
      vertical
      label
      reverse
      markers
      switch-label-side
      track-size="40px"
      thumb-size="80px"
      thumb-color="blue-10"
      marker-labels
      class="flex-1"
    />
    {{ slider }}
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';

const props = defineProps({
  variable_set: String,
  variable_get: String,
  min: Number,
  max: Number,
  step: Number,
  name: String,
});

const slider = ref(0);
let isSliding = false;

update();

function update() {
  axios
    .post('http://192.168.0.11:5000/get_variable', {
      var: props.variable_get,
    })
    .then((res) => {
      if (!isSliding) {
        slider.value = res.data.result;
      }
    })
    .finally(() => {
      setTimeout(() => {
        update();
      }, 300);
    });
}

function slider_changed() {
  axios.post('http://192.168.0.11:5000/send_event', {
    command: props.variable_set,
    value: slider.value,
  });
}

function slider_started(phase) {
  console.log(phase);
  if (phase == 'start') {
    isSliding = true;
  }
  if (phase == 'end') {
    isSliding = false;
  }
}
</script>

<style lang="scss" scoped></style>

<template>
  <div class="flex flex-col items-center">
    {{ props.name }}
    <q-knob
      v-model="slider"
      size="200px"
      :min="props.min"
      :max="props.max"
      :step="props.step"
      @change="slider_changed"
      :thickness="0.2"
      color="blue-8"
      center-color="blue-10"
      track-color="blue-3"
      class="q-ma-md"
    />
    {{ slider }}
  </div>

  <!-- <div>{{ props.variable_get }}</div> -->
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

update();

function update() {
  axios
    .post('http://192.168.0.11:5000/get_variable', {
      var: props.variable_get,
    })
    .then((res) => {
      slider.value = res.data.result;
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
</script>

<style lang="scss" scoped></style>

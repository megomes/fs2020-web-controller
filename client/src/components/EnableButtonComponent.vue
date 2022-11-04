<template>
  <q-btn
    :label="name"
    :loading="loading"
    @click="toggle"
    outline
    :class="{ 'bg-green': status }"
  />
  <!-- <div>{{ props.variable_get }}</div> -->
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';

const props = defineProps({
  variable_set: String,
  variable_get: String,
  name: String,
});

const status = ref(false);
const loading = ref(true);

update();

function update() {
  axios
    .post('http://192.168.0.11:5000/get_variable', {
      var: props.variable_get,
    })
    .then((res) => {
      status.value = res.data.result == 1;
      loading.value = false;
    })
    .finally(() => {
      setTimeout(() => {
        update();
      }, 300);
    });
}

function toggle() {
  loading.value = true;
  axios.post('http://192.168.0.11:5000/send_command', {
    command: props.variable_set,
  });
}
</script>

<style lang="scss" scoped></style>

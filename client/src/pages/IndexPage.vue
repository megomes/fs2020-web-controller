<template>
  <div style="overflow: hidden; position: fixed" class="flex flex-row w-full">
    <q-page
      class="bg-slate-800 flex flex-row w-full p-10 space-x-10 text-white"
    >
      <div class="column h-full justify-center space-y-10">
        <EnableButtonComponent
          variable_set="TOGGLE AUTOPILOT MASTER"
          variable_get="AUTOPILOT_MASTER"
          name="AUTO PILOT"
        ></EnableButtonComponent>
        <EnableButtonComponent
          variable_set="AUTOPILOT VS HOLD ON"
          variable_get="AUTOPILOT_VERTICAL_HOLD"
          name="VS"
        ></EnableButtonComponent>
        <EnableButtonComponent
          variable_set="TOGGLE AUTOPILOT ALTITUDE HOLD"
          variable_get="AUTOPILOT_ALTITUDE_LOCK"
          name="ALT"
        ></EnableButtonComponent>
        <EnableButtonComponent
          variable_set="TOGGLE AUTOPILOT HEADING HOLD"
          variable_get="AUTOPILOT_HEADING_LOCK"
          name="HDG"
        ></EnableButtonComponent>
        <EnableButtonComponent
          variable_set="AUTOPILOT NAV1 HOLD"
          variable_get="AUTOPILOT_NAV1_LOCK"
          name="NAV"
        ></EnableButtonComponent>
      </div>
      <div class="flex flex-row space-x-32 flex-1 items-center justify-center">
        <SliderComponent
          variable_set="AP_ALT_VAR_SET_ENGLISH"
          variable_get="AUTOPILOT_ALTITUDE_LOCK_VAR"
          :min="0"
          :max="31000"
          :step="1000"
          name="ALT"
        ></SliderComponent>
        <SliderComponent
          variable_set="AP_VS_VAR_SET_ENGLISH"
          variable_get="AUTOPILOT_VERTICAL_HOLD_VAR"
          :min="-3000"
          :max="3000"
          :step="500"
          name="VS"
        ></SliderComponent>
        <KnobComponent
          variable_set="HEADING_BUG_SET"
          variable_get="AUTOPILOT_HEADING_LOCK_DIR"
          :min="0"
          :max="360"
          :step="10"
          name="HDG"
        ></KnobComponent>
      </div>
      <!-- <div class="flex flex-row space-x-20 flex-1 items-center justify-center">
        oi
      </div> -->
    </q-page>
  </div>
</template>

<script setup lang="ts">
// EVENT ID: https://learn.microsoft.com/en-us/previous-versions/microsoft-esp/cc526980(v=msdn.10)
// SIMULATION VAR: https://docs.flightsimulator.com/html/Programming_Tools/SimVars/Simulation_Variables.htm

import axios from 'axios';
import EnableButtonComponent from 'src/components/EnableButtonComponent.vue';
import SliderComponent from 'src/components/SliderComponent.vue';
import KnobComponent from 'src/components/KnobComponent.vue';

import { ref } from 'vue';

const knob = ref(0);
</script>

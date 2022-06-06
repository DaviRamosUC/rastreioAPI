<script setup>
import axios from "axios";
import Header from "./Header.vue";
import Unidade from "./Codigo.vue";
import PainelLateral from "./PainelLateral.vue";
</script>

<script>
export default {
  data() {
    return {
      codes: [],
    };
  },
  methods: {},
  beforeCreate() {
    const url = "http://localhost:5000/storedCodes";
    axios
      .get(url)
      .then((res) => {
        this.codes = res.data;
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>

<template>
  <div>
    <Header />
    <Unidade v-if="codes.length > 0" :data="codes" />
    <PainelLateral />
  </div>
</template>

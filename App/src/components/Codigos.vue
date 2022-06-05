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
      codes: null,
    };
  },
  methods: {
    getCodes() {
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
  },
  created() {
    this.getCodes();
  },
};
</script>

<template>
  <div>
    <Header />
    <div v-if="this.codes">
      <Unidade :data="this.codes" />
    </div>
    <PainelLateral />
  </div>
</template>

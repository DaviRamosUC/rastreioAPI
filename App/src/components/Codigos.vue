<script setup>
import axios from "axios";
import Header from "./Header.vue";
import Unidade from "./Codigo.vue";
import PainelLateral from "./PainelLateral.vue";
</script>

<script>
export default {
  data(){
    return {
      resultado: null,
    }
  },
  async beforeCreate() {
    const url = "http://localhost:5000/storedCodes";
    this.resultado = await axios
      .get(url)
      .then((res) => {
        return res.data;
      })
      .catch((error) => {
        console.error(error);
      });
  },
};
</script>

<template>
  <div v-if="resultado != null">
    <Header />
    <Unidade :data="resultado" />
    <PainelLateral />
  </div>
</template>

<script setup>
import Header from "./Header.vue";
import Form from "./Form.vue";
import Painel from "./PainelLateral.vue";
</script>

<template>
  <div>
    <Header />
    <Form />
    <Painel msg="Teste2"/>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      msg: "Teste Titulo",
    };
  },
  // methods: {
  //   getMessage() {
  //     const path = "http://localhost:5000/ping";
  //     axios
  //       .get(path)
  //       .then((res) => {
  //         this.msg = res.data;
  //       })
  //       .catch((error) => {
  //         // eslint-disable-next-line
  //         console.error(error);
  //       });
  //   },
  // },
  // created() {
  //   this.getMessage();
  // },
};
</script>

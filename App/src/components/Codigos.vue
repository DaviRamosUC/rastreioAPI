<script setup>
import axios from "axios";
import Header from "./Header.vue";

const url = "http://localhost:5000/storedCodes";
axios
  .get(url)
  .then((res) => {
    console.log(res);
  })
  .catch((error) => {
    console.error(error);
  });
</script>

<template>
  <Header />
</template>

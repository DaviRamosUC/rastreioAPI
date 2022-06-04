<script setup>
import axios from "axios";
import Header from "./Header.vue";
</script>

<script>
export default {
  data() {
    return { codigos: {} };
  },
  mounted() {
    const url = "http://localhost:5000/storedCodes";
    axios
      .get(url)
      .then((res) => {
        this.codigos = res;
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
    <figure class="md:flex bg-slate-100 p-8 md:p-0 dark:bg-slate-800">
      <div class="pt-6 md:p-8 text-center space-y-4">
        <blockquote>
          <p class="text-lg font-medium">
            {{ this.codigos }}
          </p>
        </blockquote>
        <figcaption class="font-medium">
          <div class="text-sky-500 dark:text-sky-400">Sarah Dayan</div>
          <div class="text-slate-700 dark:text-slate-500">
            Staff Engineer, Algolia
          </div>
        </figcaption>
      </div>
    </figure>
  </div>
</template>

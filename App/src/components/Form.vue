<script setup>
import { SearchIcon } from "@heroicons/vue/solid";
import { useToast } from "vue-toastification";
import axios from "axios";
import { open, newValues } from "./PainelLateral.vue";
</script>

<template>
  <div class="flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <img
          class="mx-auto h-12 w-auto"
          src="https://tailwindui.com/img/logos/workflow-mark-indigo-600.svg"
          alt="Workflow"
        />
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Rastreio dos Correios via SMS com DB
        </h2>
      </div>
      <form
        class="mt-8 space-y-6"
        action="http://localhost:5000/search"
        method="POST"
      >
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="code" class="sr-only"
              >Insira aqui o código de rastreio dos correios</label
            >
            <input
              id="code"
              name="code"
              type="text"
              required=""
              v-mask="'AA#########AA'"
              v-model="code"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Insira aqui o código de rastreio dos correios"
            />
          </div>
          <div>
            <label for="phoneNumber" class="sr-only"
              >Insira aqui o número do seu celular</label
            >
            <input
              id="phoneNumber"
              name="phoneNumber"
              type="tel"
              v-mask="['(##) ####-####', '(##) #####-####']"
              v-model="phoneNumber"
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Insira aqui o número do seu celular"
            />
          </div>
        </div>

        <div class="flex items-center">
          <input
            id="sms"
            name="sms"
            type="checkbox"
            v-model="sms"
            true-value="yes"
            false-value="no"
            class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 border-gray-300 rounded"
          />
          <label for="sms" class="ml-2 block text-sm text-gray-900">
            Aceito receber status via sms
          </label>
        </div>

        <div>
          <button
            type="submit"
            @click="handleSubmit"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            <span class="flex items-center pr-1">
              <SearchIcon
                class="h-5 w-5 group-hover:text-gray-200 text-indigo-400"
                aria-hidden="true"
              />
            </span>
            Consultar
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    handleSubmit(event) {
      event.preventDefault();
      const path = "http://localhost:5000/search";
      const toast = useToast();
      const data = {
        code: this.code,
        phoneNumber: this.phoneNumber,
        sms: (this.sms == 'yes') ? true : false,
      };
      const headers = {
        "Content-Type": "multipart/form-data",
        "Access-Control-Allow-Origin": "*",
      };
      axios
        .post(path, data, { headers })
        .then((res) => {
          newValues.value.setData(res.data);
          open.value.setOpen(true);
        })
        .catch((error) => {
          console.error(error);
        });
      toast.success("Aguarde enquando procuramos sua encomenda...", {
        timeout: 3000,
      });
    },
  },
};
</script>

<script setup>
import axios from "axios";
import { open, newValues } from "./PainelLateral.vue";

const props = defineProps(["data"]);
</script>

<template>
  <div class="flex items-center justify-center py-12 px-4 sm:px-6 lg:px-8">
    <div class="w-full space-y-8">
      <div class="overflow-x-auto w-full">
        <table class="table w-full">
          <thead>
            <tr>
              <th>Código</th>
              <th>Telefone</th>
              <th>Status</th>
              <th></th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="code in this.codes" :key="code[0]">
              <td>
                <div class="flex items-center space-x-3">
                  <div>
                    <div class="font-bold">{{ code[0] }}</div>
                  </div>
                </div>
              </td>
              <td>
                <span class="badge badge-ghost badge-sm font-semibold">
                  {{ code[1] }}
                </span>
              </td>
              <td>{{ code[2].substr(8) }}</td>
              <th>
                <button @click="visualizar(code)" class="btn btn-ghost btn-xs">
                  Visualizar
                </button>
              </th>
              <th>
                <button @click="excluir" class="btn btn-ghost btn-xs">
                  Excluir
                </button>
              </th>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data(props) {
    return {
      codes: props.data,
    };
  },
  methods: {
    visualizar(obj) {
      console.log(obj['1']);
      const path = "http://localhost:5000/search";
      var sms = (obj["1"] != null || obj["1"] != '') ? true : false;
      const data = {
        code: obj["0"],
        phoneNumber: obj["1"],
        sms: sms,
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
    },
    excluir() {
      console.log("excluir");
    },
  },
};
</script>

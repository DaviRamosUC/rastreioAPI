<template>
  <TransitionRoot as="template" :show="open.open">
    <Dialog as="div" class="relative z-10" @close="open.open = false">
      <TransitionChild
        as="template"
        enter="ease-in-out duration-500"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="ease-in-out duration-500"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div
          class="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity"
        />
      </TransitionChild>

      <div class="fixed inset-0 overflow-hidden">
        <div class="absolute inset-0 overflow-hidden">
          <div
            class="pointer-events-none fixed inset-y-0 right-0 flex max-w-full pl-10"
          >
            <TransitionChild
              as="template"
              enter="transform transition ease-in-out duration-500 sm:duration-700"
              enter-from="translate-x-full"
              enter-to="translate-x-0"
              leave="transform transition ease-in-out duration-500 sm:duration-700"
              leave-from="translate-x-0"
              leave-to="translate-x-full"
            >
              <DialogPanel
                class="pointer-events-auto relative w-screen max-w-md"
              >
                <TransitionChild
                  as="template"
                  enter="ease-in-out duration-500"
                  enter-from="opacity-0"
                  enter-to="opacity-100"
                  leave="ease-in-out duration-500"
                  leave-from="opacity-100"
                  leave-to="opacity-0"
                >
                  <div
                    class="absolute top-0 left-0 -ml-8 flex pt-4 pr-2 sm:-ml-10 sm:pr-4"
                  >
                    <button
                      type="button"
                      class="rounded-md text-gray-300 hover:text-white focus:outline-none focus:ring-2 focus:ring-white"
                      @click="open.open = false"
                    >
                      <span class="sr-only">Fechar</span>
                      <XIcon class="h-6 w-6" aria-hidden="true" />
                    </button>
                  </div>
                </TransitionChild>
                <div
                  class="flex h-full flex-col overflow-y-scroll bg-white py-6 shadow-xl"
                >
                  <div class="px-4 sm:px-6">
                    <DialogTitle class="text-lg font-medium text-gray-900">
                      Status de Rastreio:
                      {{
                        newValues.data.ultimoStatus[0].replace(
                          "Útimo Status do Objeto:",
                          ""
                        )
                      }}
                    </DialogTitle>
                    <hr>
                    <p v-if="newValues.data.phoneNumber" class="text-sm font-semibold">Status enviado via SMS para o número <br>+55 {{newValues.data.phoneNumber}}</p>
                    <hr>
                  </div>
                  <div class="relative mt-6 flex-1 px-4 sm:px-6">
                    <ul>
                      <li
                        v-for="status in newValues.data.historicoArray"
                        :key="status.data"
                      >
                        <h2 class="font-bold">{{ status[0].replace("Status:", "") }}</h2>
                        <p>{{ status[1] }}</p>
                        <p>{{ status[2] }}</p>
                        <hr>
                        <br>
                      </li>
                    </ul>
                  </div>
                </div>
              </DialogPanel>
            </TransitionChild>
          </div>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>

<script setup>
import { ref, watch } from "vue";
import {
  Dialog,
  DialogPanel,
  DialogTitle,
  TransitionChild,
  TransitionRoot,
} from "@headlessui/vue";
import { XIcon } from "@heroicons/vue/outline";
</script>

<script>
export var open = ref({
  open: false,
  setOpen(value) {
    this.open = value;
  },
});

export var newValues = ref({
  data: {},
  setData(value) {
    this.data = value;
  },
});
</script>

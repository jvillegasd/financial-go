<template>
  <transition name="slide-fade">

    <div>
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-30 flex justify-center items-center" >
        <div class="relative mx-auto w-auto max-w-2xl">
          <div class="bg-white w-20 rounded-2xl">
            <p class="text-center font-medium">New transaction</p>
            <Textbox
              label="Title"
              :width=245
              :labelFontSize=20
              :inputFontSize=25
              :isPassword=false
              class="mx-auto">
            </Textbox>
            <Textbox
              label="Amount"
              :width=245
              :labelFontSize=20
              :inputFontSize=25
              :isPassword=false
              class="mx-auto">
            </Textbox>
            <Textbox
              label="Date"
              :width=245
              :labelFontSize=20
              :inputFontSize=25
              :isPassword=false
              class="mx-auto">
            </Textbox>
          </div>
        </div>
      </div>

      <div class="absolute inset-0 z-10 opacity-25 bg-black"></div>
    </div>

  </transition>
</template>

<script>
import Textbox from '../../components/Textbox/Textbox';

export default {
  name: "transaction-modal",
  components: { Textbox },
  data() {
    return {
      show: false,
    };
  },
  methods: {
  },
};
</script>

<style scoped>
</style>
<template>
  <transition name="slide-fade">

    <div>
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-30 flex justify-center items-center" >
        <div class="relative mx-auto w-auto max-w-2xl">
          <div class="bg-white w-20 modal rounded-2xl">
            <p class="text-center font-medium text-xl">New transaction</p>
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
            <BlueButton
              class="font-medium"
              title="Create transaction"
              :width=303
              :height=46
              :fontSize=18
            ></BlueButton>
          </div>
        </div>
      </div>

      <div class="absolute inset-0 z-10 opacity-25 bg-black"></div>
    </div>

  </transition>
</template>

<script>
import Textbox from '../../components/Textbox/Textbox';
import BlueButton from '../../components/Buttons/Blue_btn.vue';

export default {
  name: "transaction-modal",
  components: {
    Textbox,
    BlueButton
  },
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
  .modal {
    width: 486px;
    height: 652px;
  }
</style>
<template>
  <transition name="slide-fade">

    <div>
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-40 flex justify-center items-center" >
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

            <div class="text-left">
              <label class="font-regular block label-select">Type</label>
              <select name="select" class="truncate rounded-xl pl-14 select-wallet block appearance-none outline-none bg-grey-select font-medium rounded leading-tight">
                <option value="value1">Value 1</option>
                <option value="value2" selected>Value 2</option>
                <option value="value3">Value 3</option>
              </select>
            </div>

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
  .label-select {
    color: rgb(174,177,184);
    font-size: 20px;
  }
</style>
<template>
  <transition name="slide-fade">

    <div>
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-40 flex justify-center items-center" >
        <div class="relative mx-auto w-auto max-w-2xl">
          <div class="bg-white w-20 modal rounded-2xl flex flex-col items-center justify-center space-y-6">

            <exit-icon class="absolute top-5 right-5" @btn-pressed="modalClosed('exit')"></exit-icon>
            
            <p class="text-center font-bold text-2xl">New wallet</p>

            <div class="flex flex-col justify-center items-left space-y-6">
              <Textbox
                label="Title"
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false>
              </Textbox>

              <Textbox
                label="Initial amount"
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false>
              </Textbox>

              <Textbox
                label="Date"
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false>
              </Textbox>

              <BlueButton
                class="font-medium"
                title="Create card"
                :width=303
                :height=46
                :fontSize=18
                @btn-pressed="modalClosed('create')">
              </BlueButton>
            </div>
            
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
import ExitIcon from '../../components/Buttons/Exit_btn.vue';

export default {
  name: "transaction-modal",
  components: {
    Textbox,
    BlueButton,
    ExitIcon
  },
  data() {
    return {
    };
  },
  methods: {
    modalClosed: function (optionPressed) {
      this.$emit('closed', optionPressed);
    }
  },
};
</script>

<style scoped>
  .modal {
    width: 486px;
    height: 682px;
  }
</style>
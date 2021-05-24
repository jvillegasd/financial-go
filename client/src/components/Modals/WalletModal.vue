<template>
  <transition name="slide-fade">

    <div>
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-40 flex justify-center items-center" >
        <div class="relative mx-auto w-auto max-w-2xl">
          <div class="bg-white w-20 modal rounded-2xl flex flex-col items-center justify-center space-y-6">

            <exit-icon class="absolute top-5 right-5" @btn-pressed="modalClosed('exit')"></exit-icon>
            
            <p class="text-center font-bold text-2xl">New wallet</p>

            <div class="flex flex-row space-x-2 ml-10">
              <div class="flex flex-col items-center">
                <div :class="['wallet', 'shadow-md', 'rounded-2xl', 'space-y-2', 'z-30', walletCssClass]">
                  <div class="wallet-header flex justify-between items-center pl-8 pr-6 pt-4">

                    <div class="text-left">
                      <label class="wallet-label text-xs font-medium">Wallet name</label>
                      <h1 class="title-h1 text-white text-xl font-bold truncate">{{ title }}</h1>
                    </div>

                    <div>
                      <img class="wallet-slide-img block mx-auto" src="../../assets/icons/bank.svg">
                    </div>

                  </div>
                  <div class="wallet-content flex justify-between items-center px-8">

                    <div class="text-left">
                      <label class="wallet-label text-xs font-medium">Initial amount</label>
                      <h2 class="amount-show text-white text-xl font-bold truncate">{{ amount }}</h2>
                    </div>

                    <svg class="pt-1" height="27.98" width="10">
                      <line x1="0" y1="0" x2="0" y2="27.98" opacity="0.3" style="stroke: rgb(250, 250, 250); stroke-width: 2;" />
                    </svg>

                    <div class="text-left">
                      <label class="wallet-label text-xs font-medium">Date</label>
                      <h2 class="text-white text-xl font-bold">{{ date }}</h2>
                    </div>
                  </div>
                </div>
              </div>

              <div class="color-div shadow-md flex flex-col justify-center items-center space-y-3">
                <svg class="mt-3" width="16" height="19" viewBox="0 0 16 19" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path fill-rule="evenodd" clip-rule="evenodd" d="M8.71 0.292486L13.66 5.23249C15.22 6.79249 16 8.87249 16 10.8725C16 12.8725 15.22 14.9825 13.66 16.5425C12.1 18.1025 10.05 18.8925 8 18.8925C5.95 18.8925 3.9 18.1025 2.34 16.5425C0.78 14.9825 0 12.8725 0 10.8725C0 8.87249 0.78 6.79249 2.34 5.23249L7.3 0.292486C7.48683 0.105233 7.74048 0 8.005 0C8.26952 0 8.52317 0.105233 8.71 0.292486ZM3.76 6.83249C2.62 7.96249 2.01 9.23248 2 11.2325H14C13.99 9.23248 13.38 8.00249 12.24 6.88249L8 2.50249L3.76 6.83249Z" fill="black" fill-opacity="0.54"/>
                </svg>

                <button class="color_btn rounded-lg bg-grad-purple_blue" @click="selectColor('purple_blue')"></button>
                <button class="color_btn rounded-lg bg-grad-pink_blue" @click="selectColor('pink_blue')"></button>
                <button class="color_btn rounded-lg bg-grad-dust_blue" @click="selectColor('dust_blue')"></button>
                <button class="color_btn rounded-lg bg-grad-purple_red" @click="selectColor('purple_red')"></button>

              </div>

            </div>

            <div class="flex flex-col justify-center items-left space-y-6">
              <Textbox
                v-model="title"
                label="Title"
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false>
              </Textbox>

              <Textbox
                v-model="amount"
                label="Initial amount"
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false>
              </Textbox>

              <Textbox
                v-model="date"
                label="Creation date"
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
  name: "wallet-modal",
  components: {
    Textbox,
    BlueButton,
    ExitIcon
  },
  data () {
    return {
      title: "",
      amount: "",
      date: "",
      selectedColor: "purple_blue"
    };
  },
  methods: {
    modalClosed: function (optionPressed) {
      this.$emit('closed', optionPressed);
    },
    selectColor: function (optionPressed) {
      this.selectedColor = optionPressed;
    }
  },
  computed: {
    walletCssClass: function () {
      return `bg-grad-${this.selectedColor}`;
    }
  }
};
</script>

<style scoped>
  .modal {
    width: 486px;
    height: 682px;
  }
  .wallet {
    width: 329.74px;
    height: 190px;
  }
  .wallet-label {
    color: rgba(250, 250, 250, 0.5);
  }
  .wallet-slide-img {
    opacity: 0.1;
    width: 80px;
    height: 79.81px;
  }
  .amount-show, .title-h1 {
    width: 120px;
  }
  .color-div {
    width: 30px;
    height: 164px;
    border-radius: 20px;
  }
  .color_btn {
    width: 16px;
    height: 16px;
  }
</style>
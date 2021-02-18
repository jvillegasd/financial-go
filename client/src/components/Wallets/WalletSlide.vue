<template>
  <div class="flex flex-col items-center">
    <div class="wallet bg-grad-pb shadow-md rounded-2xl space-y-2 z-30">
      <div class="wallet-header flex justify-between items-center pl-8 pr-6 pt-4">

        <div class="text-left">
          <label class="wallet-label text-xs font-medium">Card name</label>
          <h1 class="text-white text-xl font-bold">Home wallet</h1>
        </div>

        <div>
          <img class="card-slide-img block mx-auto" src="../../assets/icons/bank.svg">
        </div>

      </div>
      <div class="wallet-content flex justify-between items-center px-8">

        <div class="text-left">
          <label class="wallet-label text-xs font-medium">Current amount</label>
          <h2 class="text-white text-xl font-bold">$ 25,000.00</h2>
        </div>

        <svg class="pt-1" height="27.98" width="10">
          <line x1="0" y1="0" x2="0" y2="27.98" opacity="0.3" style="stroke: rgb(250, 250, 250); stroke-width: 2;" />
        </svg>

        <div class="text-left">
          <label class="wallet-label text-xs font-medium">Date</label>
          <h2 class="text-white text-xl font-bold">04-16-19</h2>
        </div>
      </div>
    </div>

    <div class="flex flex-col items-center -mt-6">
      <div class="rounded-2xl bg-white shadow-md z-20" style="height: 37px; width: 307px;"></div>
      <div class="rounded-2xl bg-white shadow-md z-10 -mt-4" style="height: 27px; width: 290px;"></div>
      <rounded-btn class="z-20 -mt-6"></rounded-btn>
    </div>
  </div>
</template>

<script>
import RoundedBtn from "../../components/Buttons/Rounded_btn.vue";

export default {
  name: "wallet-slide",
  components: {RoundedBtn},
  data() {
    return {
      wallets: null
    }
  },
  mounted() {
    
  }
}
</script>

<style scoped>
  .wallet {
    width: 329.74px;
    height: 190px;
  }
  .wallet-label {
    color: rgba(250, 250, 250, 0.5);
  }
  .card-slide-img {
    opacity: 0.1;
    width: 80px;
    height: 79.81px;
  }
</style>
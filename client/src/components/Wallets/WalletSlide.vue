<template>
  <div class="flex flex-col items-center">
    <div v-if="current_wallet" :class="['wallet', 'shadow-md', 'rounded-2xl', 'space-y-2', 'z-30', walletCssClass]">
      <div class="wallet-header flex justify-between items-center pl-8 pr-6 pt-4">

        <div class="text-left">
          <label class="wallet-label text-xs font-medium">Wallet name</label>
          <h1 class="text-white text-xl font-bold">{{ current_wallet.wallet_name }}</h1>
        </div>

        <div>
          <img class="wallet-slide-img block mx-auto" src="../../assets/icons/bank.svg">
        </div>

      </div>
      <div class="wallet-content flex justify-between items-center px-8">

        <div class="text-left">
          <label class="wallet-label text-xs font-medium">Current amount</label>
          <h2 class="text-white text-xl font-bold">{{ current_wallet.current_amount }}</h2>
        </div>

        <svg class="pt-1" height="27.98" width="10">
          <line x1="0" y1="0" x2="0" y2="27.98" opacity="0.3" style="stroke: rgb(250, 250, 250); stroke-width: 2;" />
        </svg>

        <div class="text-left">
          <label class="wallet-label text-xs font-medium">Date</label>
          <h2 class="text-white text-xl font-bold">{{ current_wallet.creation_date }}</h2>
        </div>
      </div>
    </div>

    <div class="flex flex-col items-center -mt-6">
      <div class="rounded-2xl bg-white shadow-md z-20" style="height: 37px; width: 307px;"></div>
      <div class="rounded-2xl bg-white shadow-md z-10 -mt-4" style="height: 27px; width: 290px;"></div>
      <rounded-btn class="z-20 -mt-6" @btn-pressed="nextWallet"></rounded-btn>
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
      wallets: null,
      loading: true,
      errored: false,
      wallet_index: 0,
      current_wallet: null
    }
  },
  mounted() {
    this.wallets = [
      {
        wallet_name: "Home wallet",
        current_amount: "$ 25,000.00",
        creation_date: "17-02-21",
        wallet_color: "purple_blue"
      },
      {
        wallet_name: "Netflix and more",
        current_amount: "$ 100,000.00",
        creation_date: "17-02-21",
        wallet_color: "pink_blue"
      },
      {
        wallet_name: "Work wallet",
        current_amount: "$ 65,000.00",
        creation_date: "18-02-21",
        wallet_color: "dust_blue"
      },
      {
        wallet_name: "League",
        current_amount: "$ 100.00",
        creation_date: "7-02-21",
        wallet_color: "purple_red"
      }
    ];
    this.current_wallet = this.wallets[0];
  },
  methods: {
    nextWallet: function() {
      let next_wallet_idx = (this.wallet_index + 1) % this.wallets.length;
      this.wallet_index = next_wallet_idx;
      this.current_wallet = this.wallets[next_wallet_idx];
    }
  },
  computed: {
    walletCssClass: function() {
      if (this.current_wallet) {
        return `bg-grad-${this.current_wallet.wallet_color}`;
      }
      return "bg-grad-purple_blue";
    }
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
  .wallet-slide-img {
    opacity: 0.1;
    width: 80px;
    height: 79.81px;
  }
</style>
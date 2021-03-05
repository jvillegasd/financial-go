<template>
  <div class="relative">
    <div class=" mt-1 relative">

      <div :class="['select-wallet-color', 'rounded-xl', 'absolute', 'flex', 'inset-y-0', 'items-center', 'left-2', 'top-2', 'pointer-events-none', walletCssClass]">
      </div>

      <select v-model="selected_option" class="truncate rounded-xl pl-14 select-wallet block appearance-none outline-none w-full font-medium rounded leading-tight">
        <option
          v-for="option in wallets"
          v-bind:key="option.wallet_name"
          v-bind:value="option.wallet_color"
          class="truncate"
        >
          {{ option.wallet_name }}
        </option>
      </select>

      <div class="absolute flex inset-y-0 items-center pr-3 right-0 pointer-events-none">
        <svg width="15" height="9" viewBox="0 0 15 9" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M12.6637 0.66375L7.5 5.81625L2.33625 0.66375L0.75 2.25L7.5 9L14.25 2.25L12.6637 0.66375Z" fill="#005EEE" fill-opacity="0.8"/>
        </svg>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "select-wallets",
  data() {
    return {
      selected_option: null,
      wallets: null
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
    this.selected_option = this.wallets[0].wallet_color;
  },
  computed: {
    walletCssClass: function() {
      if (this.selected_option) {
        return `bg-grad-${this.selected_option}`;
      }
      return "bg-grad-purple_blue";
    }
  }
}
</script>

<style scoped>
  .select-wallet-color {
    width: 39px;
    height: 24px;
  }
  .select-wallet {
    width: 187px;
    height: 40px;
    font-size: 14px;
  }
</style>
<template>
  <div>
    <div class="wallet bg-grad-pb rounded-2xl space-y-2">
      <div class="wallet-header flex justify-between items-center pl-8 pr-6 pt-4">

        <div class="text-left">
          <label class="wallet-label text-xs font-medium">Card name</label>
          <h1 class="text-white text-xl font-bold">Home wallet</h1>
        </div>

        <div>
          <img class="card_slide_img block mx-auto" src="../../assets/icons/bank.svg">
        </div>

      </div>
      <div class="wallet-content flex justify-between items-center px-8">

        <div class="text-left">
          <label class="wallet-label text-xs font-medium">Current amount</label>
          <h2 class="text-white text-xl font-bold">$ 25,000.00</h2>
        </div>

        <svg class="pt-1" height="27.98" width="10">
          <line x1="0" y1="0" x2="0" y2="27.98" opacity="0.4" style="stroke: rgb(250, 250, 250); stroke-width: 2;" />
        </svg>

        <div class="text-left">
          <label class="wallet-label text-xs font-medium">Date</label>
          <h2 class="text-white text-xl font-bold">04-16-19</h2>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "wallet-slide"
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
  .bg-grad-pb {
    background: linear-gradient(0deg, rgba(117,98,255,1) 0%, rgba(51,201,255,1) 100%);
  }
  .card_slide_img {
    opacity: 0.1;
    width: 80px;
    height: 79.81px;
  }
</style>
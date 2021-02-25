<template>
  <div class="cashflow shadow-md rounded-2xl bg-white">
    <h1 class="text-left text-2xl ml-8 mt-8 font-bold">Cashflow</h1>

    <div class="cashflow-data flex justify-around pt-4">
      <div class="text-left">
        <label class="font-bold text-grey-label text-xs">Daily</label>
        <h2 class="font-bold text-lg">${{ model.general.daily }}</h2>
      </div>
      <div class="text-left">
        <label class="font-bold text-grey-label text-xs">Weekly</label>
        <h2 class="font-bold text-lg">${{ model.general.weekly }}</h2>
      </div>
      <div class="text-left">
        <label class="font-bold text-grey-label text-xs">Monthly</label>
        <h2 class="font-bold text-lg">${{ model.general.monthly }}</h2>
      </div>
    </div>

    <div class="flex justify-center">
      <svg class="pt-2" height="10" width="310">
        <line x1="0" y1="0" x2="310" y2="0" opacity="0.5" style="stroke: rgb(174, 177, 184); stroke-width: 2;" />
      </svg>
    </div>
  </div>
</template>

<script>
export default {
  name: "cash-flow",
  data() {
    return {
      model: {
        general: {
          daily: 250.5,
          weekly: 250.5,
          monthly: 250.5
        }
      }
    };
  }
}
</script>

<style scoped>
  .cashflow {
    width: 383px;
    height: 361px;
  }
</style>
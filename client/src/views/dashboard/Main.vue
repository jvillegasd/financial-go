<template>
  <div>
    <h1 class="flex justify-start text-3xl font-bold ml-20 mt-7">Dashboard</h1>
    <div class="row flex justify-around mt-6">
      <wallet-slide class="pl-2"></wallet-slide>
      <card-line-plot id="income_plot"></card-line-plot>
      <card-line-plot id="outcome_plot" :is_income="false" ></card-line-plot>
    </div>
  </div>
</template>

<script>
import WalletSlide from '../../components/Wallets/WalletSlide.vue';
import CardLinePlot from '../../components/Charts/CardLinePlot.vue';

export default {
  name: 'Dashboard',
  components: {
    WalletSlide,
    CardLinePlot
  },
  created() {
    this.$emit('selected-module', "dashboard_module");
  }
}
</script>

<style scoped>

</style>
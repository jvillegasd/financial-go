<template>
  <div>
    <h1 class="flex justify-start text-3xl font-bold ml-20 mt-7">Dashboard</h1>
    
    <div class="row flex justify-around mt-6">
      <wallet-slide class="pl-2"></wallet-slide>
      <card-line-plot id="income_plot"></card-line-plot>
      <card-line-plot id="outcome_plot" :is_income="false" ></card-line-plot>
    </div>
    
    <div class="row flex justify-around mt-6">
      <cashflow></cashflow>
      <div class="-mt-9 rounded-2xl bg-white shadow-md" style="height: 402px; width: 591px;" >
        <h1 class="text-left text-2xl ml-8 mt-8 font-bold">Lastest transactions</h1>
        <lastest-transactions class="flex justify-center mt-6"></lastest-transactions>
      </div>
    </div>

    <div class="row flex justify-around mt-10">
      <last-month-expenses></last-month-expenses>
    </div>
  </div>
</template>

<script>
import WalletSlide from '../../components/Wallets/WalletSlide.vue';
import CardLinePlot from '../../components/Charts/Line/CardLinePlot.vue';
import Cashflow from '../../components/Charts/Cashflow/Cashflow.vue';
import LastestTransactions from '../../components/Tables/LastestTransactions.vue';
import LastMonthExpenses from '../../components/Stadistics/ExpensesMonth.vue';

export default {
  name: 'Dashboard',
  components: {
    WalletSlide,
    CardLinePlot,
    Cashflow,
    LastestTransactions,
    LastMonthExpenses
  },
  created() {
    this.$emit('selected-module', "dashboard_module");
  }
}
</script>

<style scoped>

</style>
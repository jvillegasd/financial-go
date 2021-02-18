<template>
  <div>
    <h1 class="text-3xl font-bold ml-20 mt-7">Dashboard</h1>
    <div class="row">
      <wallet-slide></wallet-slide>
    </div>
  </div>
</template>

<script>
import WalletSlide from '../../components/Wallets/WalletSlide.vue';

export default {
  name: 'Dashboard',
  components: {WalletSlide},
  created() {
    this.$emit('selected-module', "dashboard_module");
  }
}
</script>

<style scoped>

</style>
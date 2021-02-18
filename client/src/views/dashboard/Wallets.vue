<template>
  <div>
    Wallets
  </div>
</template>

<script>
export default {
  name: 'Wallets',
  created() {
    this.$emit('selected-module', "wallets_module");
  }
}
</script>

<style scoped>

</style>
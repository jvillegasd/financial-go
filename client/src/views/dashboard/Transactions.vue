<template>
  <div>
    Transactions
  </div>
</template>

<script>
export default {
  name: 'Transactions',
  created() {
    this.$emit('selected-module', "transaction_module");
  }
}
</script>

<style scoped>

</style>
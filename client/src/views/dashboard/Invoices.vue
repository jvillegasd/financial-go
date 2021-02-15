<template>
  <div>
    Invoices
  </div>
</template>

<script>
export default {
  name: 'Invoices',
  created() {
    this.$emit('selected-module', "invoice_module");
  }
}
</script>

<style scoped>

</style>
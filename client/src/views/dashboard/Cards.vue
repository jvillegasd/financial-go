<template>
  <div>
    Cards
  </div>
</template>

<script>
export default {
  name: 'Cards',
  created() {
    this.$emit('selected-module', "cards_module");
  }
}
</script>

<style scoped>

</style>
<template>
  <div>
    <p class="font-bold">Dashboard</p>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  created() {
    this.$emit('selected-module', "dashboard_module");
  }
}
</script>

<style scoped>

</style>
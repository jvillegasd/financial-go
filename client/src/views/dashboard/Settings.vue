<template>
  <div>
    Settings
  </div>
</template>

<script>
export default {
  name: 'Settings',
  created() {
    this.$emit('selected-module', "settings_module");
  }
}
</script>

<style scoped>

</style>
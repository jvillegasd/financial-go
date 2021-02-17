<template>
  <div>
    <h1 class="text-3xl font-bold ml-20 mt-7">Dashboard</h1>
    <div class="row">
      <card-slide></card-slide>
    </div>
  </div>
</template>

<script>
import CardSlide from '../../components/Cards/CardSlide.vue';

export default {
  name: 'Dashboard',
  components: {CardSlide},
  created() {
    this.$emit('selected-module', "dashboard_module");
  }
}
</script>

<style scoped>

</style>
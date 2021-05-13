<template>
  <div>

    <div class="icon_card">
      <img :src="iconPath">
    </div>

  </div>
</template>

<script>
export default {
  name: "category-icon",
  props: {
    name: {
      type: String,
      default: "bank"
    }
  },
  computed: {
    iconPath: function () {
      let iconName = this.name || "bank";
      return require(`@/assets/icons/${iconName}.svg`);
    }
  }
}
</script>

<style scoped>

</style>
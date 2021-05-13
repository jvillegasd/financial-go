<template>
  <div>

    <div class="icon_card rounded-2xl flex justify-center items-center">
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
  .icon_card {
    width: 74px;
    height: 74px;
    background-color: rgba(196, 196, 196, 0.17);
  }
</style>
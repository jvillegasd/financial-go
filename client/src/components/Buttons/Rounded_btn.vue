<template>
  <button
    class="bg-white rounded-full shadow-md rounded-btn flex justify-center items-center"
    @click="buttonPressed"
  >
    <div class="triangle-down"></div>
  </button>
</template>

<script>
export default {
  name: "Rounded-btn",
  methods: {
    buttonPressed: function() {
      this.$emit('btn-pressed');
    }
  }
};
</script>

<style scoped>
.triangle-down {
  width: 0;
  height: 0;
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-top: 12px solid rgba(196, 196, 196, 0.45);
}
.rounded-btn {
  height: 51px;
  width: 51px;
}
</style>
<template>
  <div class="relative">
    <div class="mt-1 relative">
      <select v-model="selected_option" class="block appearance-none outline-none w-full font-bold rounded leading-tight">
        <option
        v-for="option in options"
        v-bind:key="option.text"
        v-bind:value="option.value"
        >
          {{ option.text }}
        </option>
      </select>
      <div class="absolute flex inset-y-0 items-center px-3 right-0 pointer-events-none">
        <svg width="11" height="7" viewBox="0 0 11 7" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M6.87622 5.60396L11 1.40099L9.62865 0L5.5 4.20297L1.37136 0L0 1.40099L4.12376 5.60396L5.5 7L6.87622 5.60396Z" fill="#AEB1B8"/>
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "select-box",
  props: {
    options: Array
  },
  data() {
    return {
      selected_option: null
    }
  },
  mounted() {
    if (this.options.length) {
      this.selected_option = this.options[0].value;
    }
  }
}
</script>

<style scoped>
</style>
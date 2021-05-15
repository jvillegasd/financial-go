<template>

  <button class="rounded-md flex items-center justify-center" @click="buttonPressed">
    <svg width="12" height="12" viewBox="0 0 10 10" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M8.87 8.86995C8.519 9.22095 7.952 9.22095 7.601 8.86995L5 6.26895L2.399 8.86995C2.048 9.22095 1.481 9.22095 1.13 8.86995C0.96147 8.7018 0.86676 8.47352 0.86676 8.23545C0.86676 7.99738 0.96147 7.7691 1.13 7.60095L3.731 4.99995L1.13 2.39895C0.96147 2.2308 0.86676 2.00252 0.86676 1.76445C0.86676 1.52638 0.96147 1.2981 1.13 1.12995C1.481 0.778949 2.048 0.778949 2.399 1.12995L5 3.73095L7.601 1.12995C7.952 0.778949 8.519 0.778949 8.87 1.12995C9.221 1.48095 9.221 2.04795 8.87 2.39895L6.269 4.99995L8.87 7.60095C9.212 7.94295 9.212 8.51895 8.87 8.86995Z" fill-opacity="0.88"/>
    </svg>
  </button>

</template>

<script>
export default {
  name: "exit-btn",
  methods: {
    buttonPressed: function () {
      return this.$emit("btn-pressed");
    }
  }
}
</script>

<style scoped>
  button {
    width: 25px;
    height: 25px;
    background-color: rgba(255, 0, 0, 0.8);
  }
  svg {
    fill: white;
  }
  button:hover {
    background-color: white;
    border-style: solid;
    border-width: 2px;
    border-color: rgba(255, 0, 0, 0.8);
  }
  button:hover > svg {
    fill: rgba(255, 0, 0, 0.8);
  }
</style>
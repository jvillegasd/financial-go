<template>
  <button class="bg-blue-80 font-regular">

    <svg class="block mx-auto" width="8" height="12" viewBox="0 0 8 12" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path fill-rule="evenodd" clip-rule="evenodd" d="M7.41 10.59L2.83 6L7.41 1.41L6 0L0 6L6 12L7.41 10.59Z" />
    </svg>
    

  </button>
</template>

<script>
export default {
  name: 'Arrow-button',
}
</script>

<style scoped>
svg {
  width: 14px;
  height: 20px;
  fill: white;
  transform: rotate(90);
}

button {
  width: 68px;
  height: 68px;
  border-radius: 15px;
  outline: none;
}

button:hover {
  background-color: white;

  @apply text-blue-80 border-2 border-blue-80
}

button:hover > svg {
  fill: rgba(0, 94, 238, 0.8);
}
</style>
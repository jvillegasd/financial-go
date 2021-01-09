<template>
  <button class="text-blue-80 border-2 font-regular border-blue-80" :style="cssVars">
    {{ title }}
  </button>
</template>

<script>
export default {
  name: 'Bordered-button',
  props: {
    title: String,
    width: Number,
    height: Number,
    fontSize: Number,
    marginTop: {
      type: Number,
      default: 0
    },
    borderRadius: {
      type: Number,
      default: 10
    }
  },
  computed: {
    cssVars() {
      return {
        '--width': this.width + 'px',
        '--height': this.height + 'px',
        '--font_size': this.fontSize + 'px',
        '--margin-top': this.marginTop + 'px',
        '--border-radius': this.borderRadius + 'px',
      };
    }
  }
}
</script>

<style scoped>
button {
  background-color: white;
  width: var(--width);
  height: var(--height);
  border-radius: var(--border-radius);
  font-size: var(--font_size);
  margin-top: var(--margin-top);
  outline: none;
}

button:hover {
  color: white;

  @apply bg-blue-80 border-none;
}
</style>
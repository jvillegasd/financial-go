<template>
  <button class="text-blue-80 font-regular" :style="cssVars">
    {{ title }}
  </button>
</template>

<script>
export default {
  name: 'Bordereless-button',
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
  width: var(--width);
  height: var(--height);
  font-size: var(--font_size);
  margin-top: var(--margin-top);
  outline: none;
}

button:hover {
  border-radius: var(--border-radius);

  @apply border-2 border-blue-80;
}
</style>
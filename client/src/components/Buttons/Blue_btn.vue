<template>
  <button class="bg-blue-80 font-regular" :style="cssVars" @click="buttonPressed">
    {{ title }}
  </button>
</template>

<script>
export default {
  name: 'Blue-button',
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
  },
  methods: {
    buttonPressed: function() {
      this.$emit('btn-pressed');
    }
  }
}
</script>

<style scoped>
button {
  color: white;
  width: var(--width);
  height: var(--height);
  border-radius: var(--border-radius);
  font-size: var(--font_size);
  margin-top: var(--margin-top);
  outline: none;
}

button:hover {
  background-color: white;

  @apply text-blue-80 border-2 border-blue-80;
}
</style>
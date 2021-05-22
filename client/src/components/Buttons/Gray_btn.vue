<template>
  <button class="font-regular" :style="cssVars" @click="buttonPressed">
    {{ title }}
  </button>
</template>

<script>
export default {
  name: 'Gray-button',
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
  background-color: rgba(174, 177, 184, 0.8);
}

button:hover {
  background-color: white;
  border-style: solid;
  border-width: 2px;
  border-color: rgba(174, 177, 184, 0.8);
  color: rgba(174, 177, 184, 0.8);

  @apply border-2;
}
</style>
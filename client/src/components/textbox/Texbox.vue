<template>
  <div class="text-left" :style="cssVars">

    <label for="textbox" class="font-regular block">{{ label }}</label>
    <input name="textbox" class="font-bold block" :type="isPassword ? 'password' : 'text'">

  </div>
</template>

<script>
export default {
  name: 'Textbox',
  props: {
    label: String,
    width: Number,
    lineWidth: {
      type: Number,
      default: function () {
        return this.width;
      }
    },
    labelFontSize: Number,
    inputFontSize: Number,
    isPassword: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    cssVars() {
      return {
        '--line_width': this.lineWidth + 'px',
        '--width': this.width + 'px',
        '--label_font_size': this.labelFontSize + 'px',
        '--input_font_size': this.inputFontSize + 'px'
      };
    }
  }
}
</script>

<style scoped>
input {
  outline: 0;
  border-width: 0 0 1px;
  border-color:rgb(174,177,184);
  font-size: var(--input_font_size);
  width: var(--line_width);
}

div {
  width: var(--width);
}

label {
  color: rgb(174,177,184);
  font-size: var(--label_font_size);
}

</style>
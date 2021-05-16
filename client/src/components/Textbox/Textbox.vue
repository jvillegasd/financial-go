<template>
  <div class="text-left" :style="cssVars">

    <label class="font-regular block">{{ label }}</label>
    <div class="relative">
      <input name="textbox" class="font-bold block" :value="value" :type="textboxFieldType" @input="handleInput($event.target.value)">
      
      <button v-if="isPassword" @click="showPassword">
        <EyeIcon v-if="textboxFieldType === 'password'" class="absolute top-2 right-0"/>
        <EyeOffIcon v-if="textboxFieldType === 'text'" class="absolute top-2 right-0"/>
      </button>
    </div>
  </div>
</template>

<script>
import EyeIcon from 'vue-material-design-icons/Eye.vue';
import EyeOffIcon from 'vue-material-design-icons/EyeOff.vue';

export default {
  name: 'Textbox',
  props: {
    value: String,
    label: String,
    width: Number,
    labelFontSize: Number,
    inputFontSize: Number,
    isPassword: {
      type: Boolean,
      default: false
    }
  },
  components: {
    EyeIcon,
    EyeOffIcon
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
  },
  data: function() {
    return {
      textboxFieldType: this.isPassword ? "password" : "text"
    };
  },
  methods: {
    showPassword () {
      this.textboxFieldType = this.textboxFieldType === "password" ? "text" : "password";
    },
    handleInput (value) {
      this.$emit('input', value);
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
  width: var(--width);
}

div {
  width: var(--width);
}

label {
  color: rgb(174,177,184);
  font-size: var(--label_font_size);
}

</style>
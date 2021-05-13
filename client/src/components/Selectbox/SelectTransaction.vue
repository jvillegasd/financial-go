<template>
  <div class="relative select-transaction-div" :style="cssVars">
    <div class=" mt-1 relative">


      <label class="text-left  font-regular block label-select">{{ title }}</label>
      <select @change="selectOption" v-model="selected_option" name="select" class="truncate rounded-xl pl-5 select-wallet block appearance-none outline-none bg-grey-select font-bold text-xl rounded leading-tight ">
        <option
        v-for="option in options"
        v-bind:key="option.text"
        v-bind:value="option.value"
        >
          {{ option.text }}
        </option>
      </select>
      <div class="absolute flex inset-y-0 items-center pr-4 pt-7 right-0 pointer-events-none">
        <svg width="27" height="27" viewBox="0 0 27 27" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M18.6637 9.66375L13.5 14.8162L8.33625 9.66375L6.75 11.25L13.5 18L20.25 11.25L18.6637 9.66375Z" fill="#1D1D1D" fill-opacity="0.6"/>
        </svg>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "select-transaction",
  props: {
    options: Array,
    title: String,
    width: {
      type: Number,
      default: 160
    }
  },
  data () {
    return {
      selected_option: null
    }
  },
  mounted () {
    if (this.options.length) {
      this.selected_option = this.options[0].value;
      this.selectOption();
    }
  },
  methods: {
    selectOption: function () {
      this.$emit('selected-option', this.selectedOption);
    }
  },
  computed: {
    cssVars () {
      return {
        '--width': this.width + 'px'
      };
    },
    selectedOption: function () {
      return this.selected_option;
    }
  }
}
</script>

<style scoped>
  .select-transaction-div {
    width: var(--width);
  }
  .label-select {
    color: rgb(174,177,184);
    font-size: 20px;
  }
  .select-wallet {
    width: var(--width);
    height: 40px;
  }
</style>
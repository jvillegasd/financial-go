<template>
  <div>
    
    <button
      v-if="selected"
      :id="id"
      class="selected_item font-bold flex items-center justify-left"
      @click="buttonPressed(id)"
    >
      <span class="selected_item_bar rounded-r-xl"></span>
      <slot></slot>
      <p class="text-2xl ml-10 text-blue">{{ title }}</p>
    </button>
    <button
      v-else
      :id="id"
      class="dashboard_item font-bold flex items-center justify-left"
      @click="buttonPressed(id)"
    > 
      <slot></slot>
      <p class="text-2xl ml-10">{{ title }}</p>
    </button>
  
  </div>
</template>

<script>
  export default {
    name: "dashboard_layout_btn",
    props: {
      selected: {
        type: Boolean,
        default: false,
      },
      title: String,
      id: String
    },
    methods: {
      buttonPressed: function(btn_id) {
        this.$emit("btn-pressed", btn_id);
      }
    }
  }
</script>

<style scoped>
  .dashboard_item > span > svg {
    fill: rgba(0, 0, 0, 1);
    fill-opacity: 0.54;

    @apply ml-11
  }
  .dashboard_item, .selected_item {
    width: 312px;
    height: 51px;
  }
  .selected_item {
    background-color: rgba(0, 94, 238, 0.1);
  }
  .selected_item > span > svg {
    fill: rgba(0, 94, 238, 1);

    @apply ml-7
  }
  .selected_item_bar {
    width: 15px;
    height: 51px;
    background-color: rgba(0, 94, 238, 0.8);
  }
</style>
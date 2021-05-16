<template>
  <transition name="slide-fade">

    <div>
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-40 flex justify-center items-center" >
        <div class="relative mx-auto w-auto max-w-2xl">
          <div class="bg-white w-20 modal rounded-2xl flex flex-col items-center justify-center space-y-6">
            
            <h1 class="text-center font-bold text-2xl">Are you sure?</h1>

            <!-- <slot></slot> -->
            <h2 class="text-center font-bold text-2xl">Do you want to delete "Salary"?</h2>

            <red-button
              class="font-medium"
              title="Delete"
              :width=303
              :height=46
              :fontSize=18
              @btn-pressed="modalClosed">
            </red-button>
            
          </div>
        </div>
      </div>

      <div class="absolute inset-0 z-10 opacity-25 bg-black"></div>
    </div>

  </transition>
</template>

<script>
import RedButton from '../../components/Buttons/Red_btn.vue';

export default {
  name: "delete-record-modal",
  components: {
    RedButton
  },
  methods: {
    modalClosed: function () {
      this.$emit('closed');
    }
  },
};
</script>

<style scoped>
  .modal {
    width: 486px;
    height: 682px;
  }
</style>
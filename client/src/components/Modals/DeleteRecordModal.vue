<template>
  <transition name="slide-fade">

    <div>
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-40 flex justify-center items-center" >
        <div class="relative mx-auto w-auto max-w-2xl">
          <div class="bg-white w-20 modal rounded-2xl flex flex-col items-center justify-center space-y-6">
            
            <svg width="100" height="100" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M0 50C0 22.4 22.35 0 49.95 0C77.6 0 100 22.4 100 50C100 77.6 77.6 100 49.95 100C22.35 100 0 77.6 0 50ZM55 30C55 27.25 52.75 25 50 25C47.25 25 45 27.25 45 30V50C45 52.75 47.25 55 50 55C52.75 55 55 52.75 55 50V30ZM50 90C27.9 90 10 72.1 10 50C10 27.9 27.9 10 50 10C72.1 10 90 27.9 90 50C90 72.1 72.1 90 50 90ZM45 65V75H55V65H45Z" fill="#FF0000" fill-opacity="0.54"/>
            </svg>

            <h1 class="text-center font-bold text-2xl">Are you sure?</h1>

            <slot></slot>

            <div class="space-x-16">
              <red-button
                class="font-medium"
                title="Delete"
                :width=131
                :height=42
                :fontSize=18
                @btn-pressed="modalClosed('delete')">
              </red-button>

              <gray-button
                class="font-medium"
                title="Cancel"
                :width=131
                :height=42
                :fontSize=18
                @btn-pressed="modalClosed('cancel')">
              </gray-button>
            </div>
            
          </div>
        </div>
      </div>

      <div class="absolute inset-0 z-10 opacity-25 bg-black"></div>
    </div>

  </transition>
</template>

<script>
import RedButton from '../../components/Buttons/Red_btn.vue';
import GrayButton from '../../components/Buttons/Gray_btn.vue';

export default {
  name: "delete-record-modal",
  components: {
    RedButton,
    GrayButton
  },
  methods: {
    modalClosed: function (optionPressed) {
      this.$emit('closed', optionPressed);
    }
  },
};
</script>

<style scoped>
  .modal {
    width: 486px;
    height: 328px;
  }
</style>
<template>
  <div>
    <h1 class="flex justify-start text-3xl font-bold ml-20 mt-7">Transactions</h1>

    <div class="row flex justify-end mt-6 mr-20">
       <BlueButton
        class="create_transaction font-medium"
        title="Create"
        :width=132
        :height=35
        :fontSize=16
        :marginTop=6
      ></BlueButton>
      <SelectWallets class="pl-8"></SelectWallets>
    </div>
  </div>
</template>

<script>
import BlueButton from '../../components/Buttons/Blue_btn.vue';
import SelectWallets from '../../components/Selectbox/SelectWallets.vue';

export default {
  name: 'Transactions',
  components: {
    BlueButton,
    SelectWallets
  },
  created() {
    this.$emit('selected-module', "transaction_module");
  }
}
</script>

<style scoped>
  .create_transaction {
    box-shadow: 0px 4px 4px 0px rgba(0, 94, 238, 0.15);
  }
</style>
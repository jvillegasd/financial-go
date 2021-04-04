<template>
  <div>
    <h1 class="flex justify-start text-3xl font-bold 2xl:ml-20 xl:ml-0 mt-7">Transactions</h1>
    
    <div class="row flex justify-end mt-6 2xl:mr-20 xl:mr-14 md:mr-2">
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

    <div class="row flex justify-center mt-8">
      <div class="card-table rounded-2xl shadow-md bg-white flex flex-col justify-center items-center">

        <table-base class="transaction-table">
          <template v-slot:header>
            <tr style="height: 42px;">
              <th class="w-1/6 ...">Id</th>
              <th class="w-1/6 ...">Title</th>
              <th class="w-1/6 ...">Category</th>
              <th class="w-1/6 ...">Type</th>
              <th class="w-1/6 ...">Amount</th>
              <th class="w-1/6 ...">Date</th>
              <th class="w-1/6 ..."></th>
            </tr>
          </template>

          <template v-slot:body>
            <tr>
              <td class="font-medium">50</td>
              <td class="font-medium">Netflix</td>
              <td class="font-medium">Entertaiment</td>
              <td class="font-medium text-blue">Recurrent</td>
              <td class="font-medium text-blue">-$12</td>
              <td class="font-medium">18/05</td>
              <td class="pr-6">
                <table-modal 
                @delete-record="deleteRecord('some_id')"
                @edit-record="editRecord('some_id')"
                ></table-modal>
              </td>
            </tr>
            <tr>
              <td class="font-medium">49</td>
              <td class="font-medium">Salary</td>
              <td class="font-medium">Cash</td>
              <td class="font-medium text-dust">Income</td>
              <td class="font-medium text-dust">+$1200</td>
              <td class="font-medium">17/05</td>
              <td class="pr-6">
                <table-modal></table-modal>
              </td>
            </tr>
            <tr>
              <td class="font-medium">48</td>
              <td class="font-medium">Jeans</td>
              <td class="font-medium">Shopping</td>
              <td class="font-medium text-blue">Outcome</td>
              <td class="font-medium text-blue">-$15</td>
              <td class="font-medium">17/05</td>
              <td class="pr-6">
                <table-modal></table-modal>
              </td>
            </tr>
          </template>
        </table-base>

      </div>
    </div>
  </div>
</template>

<script>
import BlueButton from '../../components/Buttons/Blue_btn.vue';
import SelectWallets from '../../components/Selectbox/SelectWallets.vue';
import TableBase from '../../components/Tables/TableBase.vue';
import TableModal from '../../components/Modals/TableModal.vue';

export default {
  name: 'Transactions',
  components: {
    BlueButton,
    SelectWallets,
    TableModal,
    TableBase
  },
  created() {
    this.$emit('selected-module', "transaction_module");
  },
  methods: {
    deleteRecord: function(recordId) {
      console.log(`delete record ${recordId}`);
    },
    editRecord: function(recordId) {
      console.log(`edit record ${recordId}`);
    }
  }
}
</script>

<style scoped>
  .create_transaction {
    box-shadow: 0px 4px 4px 0px rgba(0, 94, 238, 0.15);
  }
  .card-table {
    width: 998px;
    height: 591px;
  }
  .transaction-table {
    width: 919px;
    height: 501px;
  }
</style>
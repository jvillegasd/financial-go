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
        <vs-table class="transaction-table">
          <template #thead>
            <vs-tr>
              <vs-th>Id</vs-th>
              <vs-th>Title</vs-th>
              <vs-th>Category</vs-th>
              <vs-th>Type</vs-th>
              <vs-th>Amount</vs-th>
              <vs-th>Date</vs-th>
              <vs-th></vs-th>
            </vs-tr>
          </template>

          <template #tbody>
            <vs-tr>
              <vs-td class="font-medium">50</vs-td>
              <vs-td class="font-medium">Netflix</vs-td>
              <vs-td class="font-medium">Entertaiment</vs-td>
              <vs-td class="font-medium text-blue">Recurrent</vs-td>
              <vs-td class="font-medium text-blue">-$12</vs-td>
              <vs-td class="font-medium">18/05</vs-td>
              <vs-td class="pr-6">
                <table-modal 
                @delete-record="deleteRecord('some_id')"
                @edit-record="editRecord('some_id')"
                ></table-modal>
              </vs-td>
            </vs-tr>
            <vs-tr>
              <vs-td class="font-medium">49</vs-td>
              <vs-td class="font-medium">Salary</vs-td>
              <vs-td class="font-medium">Cash</vs-td>
              <vs-td class="font-medium text-dust">Income</vs-td>
              <vs-td class="font-medium text-dust">+$1200</vs-td>
              <vs-td class="font-medium">17/05</vs-td>
              <vs-td class="pr-6">
                <table-modal></table-modal>
              </vs-td>
            </vs-tr>
            <vs-tr>
              <vs-td class="font-medium">48</vs-td>
              <vs-td class="font-medium">Jeans</vs-td>
              <vs-td class="font-medium">Shopping</vs-td>
              <vs-td class="font-medium text-blue">Outcome</vs-td>
              <vs-td class="font-medium text-blue">-$15</vs-td>
              <vs-td class="font-medium">17/05</vs-td>
              <vs-td class="pr-6">
                <table-modal></table-modal>
              </vs-td>
            </vs-tr>
          </template>

          <template #footer>
            <vs-pagination v-model="page" :length="20" />
          </template>
        </vs-table>

      </div>
    </div>
  </div>
</template>

<script>
import BlueButton from '../../components/Buttons/Blue_btn.vue';
import SelectWallets from '../../components/Selectbox/SelectWallets.vue';
//import TableBase from '../../components/Tables/TableBase.vue';
import TableModal from '../../components/Modals/TableModal.vue';

export default {
  name: 'Transactions',
  components: {
    BlueButton,
    SelectWallets,
    TableModal,
  },
  data() {
    return {
      page: 1
    }
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
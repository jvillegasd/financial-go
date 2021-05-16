<template>
  <div>
    <h1 class="flex justify-start text-3xl font-bold 2xl:ml-20 xl:ml-0 mt-7">Transactions</h1>
    
    <div class="row flex justify-end mt-8 2xl:mr-20 xl:mr-14 md:mr-2">
       <BlueButton
        class="create_transaction font-medium"
        title="Create"
        :width=132
        :height=35
        :fontSize=16
        :marginTop=6
        @btn-pressed="showModal"
      ></BlueButton>
      <SelectWallets class="pl-8"></SelectWallets>
    </div>

    <transaction-modal v-show="isModalVisible" class="z-10" @closed="closeModal">
    </transaction-modal>

    <transaction-edit-modal v-show="isEditModalVisible" class="z-10" @closed="closeEditModal">
    </transaction-edit-modal>

    <div class="row flex justify-center mt-12">
      <div class="card-table rounded-2xl shadow-md bg-white flex flex-col justify-center items-center">
        <div style=""></div>
        <vs-table class="transaction-table">
          <template #thead>
            <vs-tr>
              <vs-th>
                <p class="font-medium text-lg text-center">Id</p>
              </vs-th>
              <vs-th>
                <p class="font-medium text-lg">Title</p>
              </vs-th>
              <vs-th>
                <p class="font-medium text-lg">Category</p>
              </vs-th>
              <vs-th>
                <p class="font-medium text-lg">Type</p>
              </vs-th>
              <vs-th>
                <p class="font-medium text-lg">Amount</p>
              </vs-th>
              <vs-th>
                <p class="font-medium text-lg">Date</p>
              </vs-th>
            </vs-tr>
          </template>

          <template #tbody>
            <vs-tr
              :key="i"
              v-for="(tr, i) in $vs.getPage(transactions, page, max)"
            >
              <vs-td>
                <p class="font-medium text-lg">{{ tr.id }}</p>
              </vs-td>
              <vs-td>
                <p class="font-medium text-lg">{{ tr.title }}</p>
              </vs-td>
              <vs-td>
                <p class="font-medium text-lg">{{ tr.category }}</p>
              </vs-td>
              <vs-td>
                <p :class="['font-medium', 'text-lg', tr.type !== 'Income' ? 'text-blue' : 'text-dust']">{{ tr.type }}</p>
              </vs-td>
              <vs-td>
                <p :class="['font-medium', 'truncate', 'text-lg', tr.type !== 'Income' ? 'text-blue' : 'text-dust']">{{ tr.amount }}</p>
              </vs-td>
              <vs-td>
                <p class="font-medium text-lg">{{ tr.date }}</p>
              </vs-td>

              <template #expand>
                <div class="con-content flex flex-row justify-center items-center space-x-2">
                  <BlueButton
                    class="font-medium"
                    title="Edit"
                    :width=100
                    :height=35
                    :fontSize=16
                    @btn-pressed="showEditModal"
                  ></BlueButton>

                  <red-button
                    class="font-medium"
                    title="Delete"
                    :width=100
                    :height=35
                    :fontSize=16
                    @btn-pressed="modalClosed">
                  </red-button>
                </div>
              </template>
            </vs-tr>
          </template>

          <template #footer>
            <vs-pagination :disabled="isModalVisible || isEditModalVisible" v-model="page" :length="$vs.getLength(transactions, max)" class="font-medium" />
          </template>
        </vs-table>
      </div>
    </div>
  </div>
</template>

<script>
import BlueButton from '../../components/Buttons/Blue_btn.vue';
import RedButton from '../../components/Buttons/Red_btn.vue';
import SelectWallets from '../../components/Selectbox/SelectWallets.vue';
import TransactionModal from '../../components/Modals/TransactionModal.vue';
import TransactionEditModal from '../../components/Modals/TransactionEditModal.vue';

export default {
  name: 'Transactions',
  components: {
    BlueButton,
    RedButton,
    SelectWallets,
    TransactionModal,
    TransactionEditModal
  },
  data() {
    return {
      isModalVisible: false,
      isEditModalVisible: false,
      page: 1,
      max: 6,
      transactions: [
        {
          id: "50",
          title: "Netflix",
          category: "Entertaiment",
          type: "Recurrent",
          amount: "-$12",
          date: "18/05"
        },
        {
          id: "49",
          title: "Salary",
          category: "Cash",
          type: "Recurrent",
          amount: "+$1200",
          date: "17/05"
        },
        {
          id: "48",
          title: "Jeans",
          category: "Shopping",
          type: "Income",
          amount: "+$15",
          date: "17/05"
        },
        {
          id: "47",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "-$15",
          date: "17/05"
        },
        {
          id: "46",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "-$15",
          date: "17/05"
        },
        {
          id: "45",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "-$15",
          date: "17/05"
        },
        {
          id: "44",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "-$15",
          date: "17/05"
        },
        {
          id: "43",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "-$15",
          date: "17/05"
        },
        {
          id: "42",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "-$15",
          date: "17/05"
        },
        {
          id: "41",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "-$15",
          date: "17/05"
        },
        {
          id: "40",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "-$15",
          date: "17/05"
        }
      ]
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
    },
    showModal: function() {
      this.isModalVisible = true;
    },
    closeModal: function() {
      this.isModalVisible = false;
    },
    showEditModal: function() {
      this.isEditModalVisible = true;
    },
    closeEditModal: function() {
      this.isEditModalVisible = false;
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
    width: 919px !important;
    height: 501px !important;
  }
</style>
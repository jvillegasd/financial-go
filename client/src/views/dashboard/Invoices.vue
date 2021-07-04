<template>
  <div>
    <h1 class="flex justify-start text-3xl font-bold 2xl:ml-20 xl:ml-0 mt-7">Invoices</h1>
  
    <div class="row flex justify-end mt-8 2xl:mr-20 xl:mr-14 md:mr-2">
      <BlueButton
        class="create_invoice font-medium"
        title="Create"
        :width=132
        :height=35
        :fontSize=16
        :marginTop=6
        @btn-pressed="showModal"
      ></BlueButton>
      <SelectWallets class="pl-8"></SelectWallets>
    </div>

    <invoice-modal v-show="isModalVisible" class="z-10" @closed="closeModal">
    </invoice-modal>

    <div class="row flex justify-center mt-12">
      <div class="card-table rounded-2xl shadow-md bg-white flex flex-col justify-center items-center">
        <vs-table class="invoice-table">
          <template #thead>
            <vs-tr>
              <vs-th>
                <p class="font-medium text-lg">Id</p>
              </vs-th>
              <vs-th>
                <p class="font-medium text-lg">Title</p>
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
              v-for="(tr, i) in $vs.getPage(invoices, page, max)"
            >
              <vs-td>
                <p class="font-medium text-lg">{{ tr.id }}</p>
              </vs-td>
              <vs-td>
                <p class="font-medium text-lg ">{{ tr.title }}</p>
              </vs-td>
              <vs-td>
                <p :class="['font-medium', 'truncate', 'text-lg', tr.type !== 'Income' ? 'text-blue' : 'text-dust']">{{ tr.amount }}</p>
              </vs-td>
              <vs-td>
                <p class="font-medium text-lg">{{ tr.date }}</p>
              </vs-td>

              <template #expand>
                <div class="flex flex-row justify-center items-center space-x-2">
                  <BlueButton
                    class="font-medium"
                    title="Edit"
                    :width=100
                    :height=35
                    :fontSize=16
                  ></BlueButton>

                  <red-button
                    class="font-medium"
                    title="Delete"
                    :width=100
                    :height=35
                    :fontSize=16
                    @btn-pressed="showDeleteModal(tr)">
                  </red-button>
                </div>
              </template>
            </vs-tr>
          </template>

          <template #footer>
            <vs-pagination :disabled="isModalVisible || isDeleteModalVisible" v-model="page" :length="$vs.getLength(invoices, max)" class="font-medium" />
          </template>
        </vs-table>
      </div>
    </div>
  
  </div>
</template>

<script>
import BlueButton from '../../components/Buttons/Blue_btn.vue';
import SelectWallets from '../../components/Selectbox/SelectWallets.vue';
import RedButton from '../../components/Buttons/Red_btn.vue';
import InvoiceModal from '../../components/Modals/InvoiceModal.vue';

export default {
  name: 'Invoices',
  components: {
    BlueButton,
    RedButton,
    SelectWallets,
    InvoiceModal
  },
  created() {
    this.$emit('selected-module', "invoice_module");
  },
  data () {
    return {
      isModalVisible: false,
      isDeleteModalVisible: false,
      page: 1,
      max: 6,
      selectedRow: null,
      invoices: [
        {
          id: "50",
          title: "Netflix",
          category: "Entertainment",
          type: "Recurrent",
          amount: "-$12",
          date: "18/05"
        },
        {
          id: "49",
          title: "Salary",
          category: "Money",
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
  methods: {
    showModal: function() {
      this.isModalVisible = true;
    },
    closeModal: function(optionPressed) {
      console.log('create modal', optionPressed);
      this.isModalVisible = false;
    },
    showDeleteModal: function(selectedRow) {
      this.selectedRow = Object.assign({}, selectedRow);
      this.selectedRow.type = this.selectedRow.type.toLowerCase();
      this.selectedRow.category = this.selectedRow.category.toLowerCase();

      this.isDeleteModalVisible = true;
    },
    closeDeleteModal: function(optionPressed) {
      console.log('delete modal', optionPressed);
      this.isDeleteModalVisible = false;
    }
  }
}
</script>

<style scoped>
  .create_invoice {
    box-shadow: 0px 4px 4px 0px rgba(0, 94, 238, 0.15);
  }
  .card-table {
    width: 998px;
  }
  .card-table .invoice-table {
    padding: 40px;
    overflow: hidden;
    height: auto;
    transition: all .25s ease;
  }
</style>
<template>
  <div>
    <transaction-modal v-show="isModalVisible" class="z-10" @closed="closeModal">
    </transaction-modal>

    <div class="flex justify-between">
      <div class="ticket-wrapper">

        <div class="ticket-up flex flex-col justify-center items-center space-y-1">
          <h1 class="font-medium text-2xl text-white">#{{ $route.params.invoice_id }}</h1>
          <h2 class="font-medium text-2xl text-white">{{ invoice_name }}</h2>
          <h3 class="font-medium text-xl text-white">{{ invoice_date }}</h3>
        </div>

        <div class="ticket-down bg-white flex flex-col items-center justify-center flex space-y-2">
          
          <div class="ticket-table-div mt-10">
            <table class="flex flex-col space-y-2">
              <tr
                :key="i"
                v-for="(tr, i) in transactions"
              >
                <th>

                  <div :class="['ticket-tcard', 'flex', 'justify-around', selectInvoiceItemCss(tr)]" @click="selectInvoiceItem(tr)">
                    <div class="mt-2 invoice-info">
                      <h1 class="tcard-title">{{ tr.title }}</h1>
                      <h2 class="text-grey-label font-medium tcard-category">{{ tr.category }}</h2>
                    </div>

                    <div class="mt-4 invoice-amount">
                      <h2 class="tcard-amount">{{ tr.amount }}</h2>
                    </div>
                  </div>

                </th>
              </tr>
            </table>
          </div>

          <BlueButton
            class="font-medium"
            title="Add new transaction"
            :width=380
            :height=40
            :fontSize=18
            @btn-pressed="showModal"
          ></BlueButton>

        </div>

      </div>

      <div v-if="selectedRow" class="card-details rounded-2xl shadow-md bg-white">
          <category-icon 
          :name="selectedRow.category">
          </category-icon>
      </div>
    </div>
  
  </div>
</template>

<script>
import BlueButton from '../../../components/Buttons/Blue_btn.vue';
import TransactionModal from '../../../components/Modals/TransactionModal.vue';
import CategoryIcon from '../../../components/Misc/CategoryIcon.vue';
// import RedButton from '../../../components/Buttons/Red_btn.vue';
// import DeleteRecordModal from '../../../components/Modals/DeleteRecordModal.vue';https://www.bypeople.com/cinema-ticket-codepen/

export default {
  name: 'Invoices-ticket',
  components: {
    BlueButton,
    TransactionModal,
    CategoryIcon,
    // RedButton,
    // DeleteRecordModal
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
      selectedRow: undefined,
      invoice_name: "Random meeting",
      invoice_date: "1/05/2021",
      transactions: [
        {
          id: "50",
          title: "Netflix",
          category: "Entertainment",
          type: "Recurrent",
          amount: "$12",
          date: "18/05"
        },
        {
          id: "49",
          title: "Salary",
          category: "Money",
          type: "Recurrent",
          amount: "$1200",
          date: "17/05"
        },
        {
          id: "48",
          title: "Jeans",
          category: "Shopping",
          type: "Income",
          amount: "$15",
          date: "17/05"
        },
        {
          id: "47",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "$15",
          date: "17/05"
        },
        {
          id: "46",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "$15",
          date: "17/05"
        },
        {
          id: "45",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "$15",
          date: "17/05"
        },
        {
          id: "44",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "$15",
          date: "17/05"
        },
        {
          id: "43",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "$15",
          date: "17/05"
        },
        {
          id: "42",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "$15",
          date: "17/05"
        },
        {
          id: "41",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "$15",
          date: "17/05"
        },
        {
          id: "40",
          title: "Jeans",
          category: "Shopping",
          type: "Outcome",
          amount: "$15",
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
    },
    selectInvoiceItem: function(selectedRow) {
      this.selectedRow = Object.assign({}, selectedRow);
      this.selectedRow.type = this.selectedRow.type.toLowerCase();
      this.selectedRow.category = this.selectedRow.category.toLowerCase();
    },
    selectInvoiceItemCss: function(selectedRow) {
      if (this.selectedRow && selectedRow.id === this.selectedRow.id) {
        return 'ticket-tcard-clicked'
      }

      return '';
    }
  }
}
</script>

<style scoped>
  .ticket-wrapper {
    width: 587px;
    height: 606px;
  }

  .ticket-up {
    width: 487px;
    height: 185px;
    background: rgba(0, 94, 238, 0.8);
    border-radius: 20px 20px 0px 0px;
    position: relative;
  }
  .ticket-up::before, .ticket-up::after {
    content: "";
    position: absolute;
    display: block;
    width: 78px;
    height: 112px;
    background:#F4F4F4;
    border-radius: 50%;
    bottom: -60px;
  }
  .ticket-up::before {
    right: -38px;
  }
  .ticket-up::after {
    left: -38px;
  }

  .ticket-down {
    width: 487px;
    height: 421px;
    border-radius: 0px 0px 20px 20px;
  }

  .ticket-tcard {
    width: 380px;
    height: 65px;
    border: 1px solid rgba(196, 196, 196, 0.8);
    box-sizing: border-box;
    border-radius: 10px;
    cursor: pointer;
  }

  .ticket-table-div {
    height: 300px;
    overflow: auto;
  }

  .ticket-tcard-clicked {
    border: 1px solid #005EEE;
    box-sizing: border-box;
    border-radius: 10px;
  }

  .ticket-tcard-clicked > .invoice-info > .tcard-title, 
  .ticket-tcard-clicked > .invoice-amount > .tcard-amount {
    color:#005EEE;
  }

  .ticket-tcard-clicked > .invoice-info > .tcard-category {
    color: rgba(0, 94, 238, 0.8);
  }

  ::-webkit-scrollbar {
    width: 7px;
  }

  ::-webkit-scrollbar-thumb {
    background: #C4C4C4;
    border-radius: 20px;
  }

  ::-webkit-scrollbar-track-piece {
    background: rgba(196, 196, 196, 0.3);
    border-radius: 20px;
  }

  .card-details {
    width: 420px;
    height: 296px;
  }

</style>
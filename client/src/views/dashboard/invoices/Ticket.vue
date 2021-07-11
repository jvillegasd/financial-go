<template>
  <div>
    <h1 class="flex justify-start text-3xl font-bold 2xl:ml-20 xl:ml-0 mt-7">{{ $route.params.invoice_id }}</h1>
  
    
  
  </div>
</template>

<script>
// import BlueButton from '../../../components/Buttons/Blue_btn.vue';
// import RedButton from '../../../components/Buttons/Red_btn.vue';
// import DeleteRecordModal from '../../../components/Modals/DeleteRecordModal.vue';https://www.bypeople.com/cinema-ticket-codepen/

export default {
  name: 'Invoices-ticket',
  components: {
    // BlueButton,
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
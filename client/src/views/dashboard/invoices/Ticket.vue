<template>
  <div>
    <div class="ticket-wrapper">

      <div class="ticket-up flex flex-col justify-center items-center space-y-1">
        <h1 class="font-medium text-2xl text-white">#{{ $route.params.invoice_id }}</h1>
        <h2 class="font-medium text-2xl text-white">{{ invoice_name }}</h2>
        <h3 class="font-medium text-xl text-white">{{ invoice_date }}</h3>
      </div>

      <div class="ticket-down bg-white"></div>

    </div>
  
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
      invoice_name: "Random meeting",
      invoice_date: "1/05/2021",
      transactions: [
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


</style>
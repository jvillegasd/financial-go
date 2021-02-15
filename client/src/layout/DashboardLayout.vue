<template>
  <div>
    <nav
      id="navbar"
      class="fixed w-full flex items-center justify-end text-center"
    >
      <p class="text-3xl font-bold mr-8">Hello, Admin</p>
      <span
        class="bg-blue-80 text-3xl font-bold text-white flex items-center justify-center mr-24"
        id="letter_circle"
        >A</span
      >
    </nav>

    <aside id="sidebar" class="fixed h-full flex flex-col">
      <div id="title" class="flex justify-center mt-5">
        <img id="image" src="../assets/logo.svg" class="" />
        <p class="font-bold text-3xl ml-3 mt-2">Financial Go</p>
      </div>

      <div id="content" class="text-left">
        <ul class="space-y-10">
          <li>
            <DashboardBtn
              id="dashboard_module"
              title="Dashboard"
              :selected="active_module === 'dashboard_module'"
              @btn-pressed="activateModule"
            >
              <DashboardIcon />
            </DashboardBtn>
          </li>
          <li>
            <DashboardBtn
              id="transaction_module"
              title="Transactions"
              :selected="active_module === 'transaction_module'"
              @btn-pressed="activateModule"
            >
              <TransactionIcon />
            </DashboardBtn>
          </li>
          <li>
            <DashboardBtn
              id="invoice_module"
              title="Invoices"
              :selected="active_module === 'invoice_module'"
              @btn-pressed="activateModule"
            >
              <ReceiptIcon />
            </DashboardBtn>
          </li>
          <li>
            <DashboardBtn
              id="cards_module"
              title="Cards"
              :selected="active_module === 'cards_module'"
              @btn-pressed="activateModule"
            >
              <CreditCardIcon />
            </DashboardBtn>
          </li>
          <li>
            <DashboardBtn
              id="settings_module"
              title="Settings"
              :selected="active_module === 'settings_module'"
              @btn-pressed="activateModule"
            >
              <SettingsIcon />
            </DashboardBtn>
          </li>
        </ul>
      </div>
    </aside>
  </div>
</template>

<script>
/* Material icons */
import DashboardBtn from "./Dashboard_btn";
import DashboardIcon from "vue-material-design-icons/ViewDashboard.vue";
import TransactionIcon from "vue-material-design-icons/Autorenew.vue";
import ReceiptIcon from "vue-material-design-icons/Receipt.vue";
import CreditCardIcon from "vue-material-design-icons/CreditCardOutline.vue";
import SettingsIcon from "vue-material-design-icons/Cog.vue";

export default {
  name: "dashboard_layout",
  components: {
    DashboardBtn,
    DashboardIcon,
    TransactionIcon,
    ReceiptIcon,
    CreditCardIcon,
    SettingsIcon,
  },
  data() {
    return {
      active_module: "dashboard_module",
    };
  },
  beforeCreate: function () {
    document.body.className = "dashboard";
  },
  methods: {
    activateModule: function (btn_id) {
      this.active_module = btn_id;
    },
  }
};
</script>

<style scoped>
  /* Sidebar */
  #sidebar {
    background-color: white;
    width: 312px;
    box-shadow: 5px 4px 4px 0 rgba(0, 0, 0, 0.07);
  }
  #image {
    width: 50.03px;
    height: 39.24px;
  }
  #title {
    height: 85px;
    width: 312px;
  }

  /* Navbar */
  #navbar {
    background-color: white;
    height: 84px;
    border-bottom-right-radius: 50px;
    box-shadow: 0px 3px 4px 0 rgba(0, 0, 0, 0.03);
  }
  #letter_circle {
    height: 50px;
    width: 50px;
    border-radius: 50%;
  }
</style>
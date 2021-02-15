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
        <ul>
          <li>
            <DashboardBtn :selected="true" title="Dashboard">
              <DashboardIcon />
            </DashboardBtn>
          </li>
          <li>
            <DashboardBtn title="Transactions">
              <TransactionIcon />
            </DashboardBtn>
          </li>
          <li>
            <DashboardBtn title="Invoices">
              <ReceiptIcon />
            </DashboardBtn>
          </li>
          <li>
            <DashboardBtn title="Cards">
              <CreditCardIcon />
            </DashboardBtn>
          </li>
          <li>
            <DashboardBtn title="Settings">
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
      SettingsIcon
    },
    beforeCreate: function () {
      document.body.className = "dashboard";
    },
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
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
            <button
              class="selected_item font-bold flex items-center justify-left"
            >
              <span id="selected_item_bar" class="rounded-r-xl"></span>
              <DashboardIcon fillColor="#005EEE" class="ml-7" />
              <p class="text-2xl ml-10 text-blue">Dashboard</p>
            </button>
          </li>
          <li>
            <button
              class="dashboard_item font-bold flex items-center justify-left"
            >
              <TransactionIcon class="ml-11" />
              <p class="text-2xl ml-10">Transactions</p>
            </button>
          </li>
          <li>
            <button
              class="dashboard_item font-bold flex items-center justify-left"
            >
              <ReceiptIcon class="ml-11" />
              <p class="text-2xl ml-10">Invoices</p>
            </button>
          </li>
          <li>
            <button
              class="dashboard_item font-bold flex items-center justify-left"
            >
              <CreditCardIcon class="ml-11" />
              <p class="text-2xl ml-10">Cards</p>
            </button>
          </li>
          <li>
            <button
              class="dashboard_item font-bold flex items-center justify-left"
            >
              <SettingsIcon class="ml-11" />
              <p class="text-2xl ml-10">Settings</p>
            </button>
          </li>
        </ul>
      </div>
    </aside>
  </div>
</template>

<script>
/* Material icons */
import DashboardIcon from "vue-material-design-icons/ViewDashboard.vue";
import TransactionIcon from "vue-material-design-icons/Autorenew.vue";
import ReceiptIcon from "vue-material-design-icons/Receipt.vue";
import CreditCardIcon from "vue-material-design-icons/CreditCardOutline.vue";
import SettingsIcon from "vue-material-design-icons/Cog.vue";

export default {
  name: "dashboard_layout",
  components: {
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
.dashboard_item > span > svg {
  fill: "#000000";
  fill-opacity: 0.7;
}
.dashboard_item, .selected_item {
  width: 312px;
  height: 51px;
}
.selected_item {
  background-color: rgba(0, 94, 238, 0.1);
}
#selected_item_bar {
  width: 17px;
  height: 51px;
  background-color: rgba(0, 94, 238, 0.8);
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
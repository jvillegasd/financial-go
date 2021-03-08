<template>
  <div class="all-time-expenses rounded-2xl shadow-md bg-white">
    <h1 class="text-left text-xl ml-8 mt-8 font-bold">Most expensive categories (all time)</h1>

    <div class="pt-3 flex justify-center">

      <div
        v-if="currentExpenses"
        class="all-time-expense-div-grid flex justify-center 2xl:space-x-6 lg:space-x-3"
      >
        <div
          v-for="elem in zip(currentExpenses, expensesColors, expensesShadows)"
          v-bind:key="elem[0].category"
          :class="[elem[1], elem[2], 'rounded-2xl', 'all-time-expense-div-square', 'space-y-1', 'space-x-5', 'flex', 'flex-row', 'justify-center', 'items-center']"
        > 
          <img :src="getImgUrl(elem[0].icon_name)" class="all-time-expense-div-img">
          <div>
            <h2 class="text-white font-bold truncate">{{ elem[0].category }}</h2>
            <h3 class="text-white font-bold truncate">${{ elem[0].value }}</h3>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "all-time-expenses",
  data() {
    return {
      expensesColors: [
        "black-expense-grad",
        "blue-expense-grad",
        "purple-expense-grad",
        "dust-expense-grad"
      ],
      expensesShadows: [
        "black-expense-shadow",
        "blue-expense-shadow",
        "purple-expense-shadow",
        "dust-expense-shadow"
      ],
      currentExpenses: null
    }
  },
  mounted() {
    this.currentExpenses = [
      {
        category: "Entertainment",
        icon_name: "entertainment.svg",
        value: 35000
      },
      {
        category: "Eating",
        icon_name: "eating.svg",
        value: 15790
      },
      {
        category: "Fitness",
        icon_name: "fitness.svg",
        value: 500
      },
      {
        category: "Credit card",
        icon_name: "credit_card.svg",
        value: 55
      }
    ];
  },
  methods: {
    zip: function (arr, ...arrs) {
      return arr.map((val, i) => arrs.reduce((a, arr) => [...a, arr[i]], [val]));
    },
    getImgUrl: function(img) {
      return require(`../../assets/icons/${img}`);
    }
  }
}
</script>

<style scoped>
  .all-time-expenses {
    width: 1240px;
    height: 192px;
  }
  .all-time-expense-li-square {
    width: 17px;
    height: 17px;
  }
  .all-time-expense-div-square {
    width: 220px;
    height: 98px;
  }
  .all-time-expense-ul {
    width: 145px;
    height: 152px;
  }
</style>
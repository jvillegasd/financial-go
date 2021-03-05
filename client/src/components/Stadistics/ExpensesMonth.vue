<template>
  <div class="last-month-expenses rounded-2xl shadow-md bg-white">
    <h1 class="text-left text-xl ml-8 mt-8 font-bold">Most expensive categories (last month)</h1>

    <div class="flex justify-center items-center pt-7">
      
      <ul v-if="currentExpenses" class="expense-ul space-y-4">
        <li 
          v-for="elem in zip(currentExpenses, expensesColors)" 
          v-bind:key="elem[0].category"
          class="text-left font-bold flex items-center"
        >
          <div :class="[elem[1], 'expense-li-square', 'rounded-md']"></div>
          <h3 class="pl-1">{{ elem[0].category }}</h3>
        </li>
      </ul>

      <div
        v-if="currentExpenses"
        class="expense-div-grid grid gap-4 grid-cols-2"
      >
        <div
          v-for="elem in zip(currentExpenses, expensesColors, expensesShadows)"
          v-bind:key="elem[0].category"
          :class="[elem[1], elem[2], 'rounded-2xl', 'expense-div-square', 'space-y-1', 'flex', 'flex-col', 'justify-center', 'items-center']"
        > 
          <img :src="getImgUrl(elem[0].icon_name)" class="expense-div-img block mx-auto">
          <h3 class="text-white font-bold truncate">${{ elem[0].value }}</h3>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "last-month-expenses",
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
  .last-month-expenses {
    width: 507px;
    height: 405px;
  }
  .expense-li-square {
    width: 17px;
    height: 17px;
  }
  .expense-div-square {
    width: 125px;
    height: 125px;
  }
  .expense-div-grid {
    width: 279px;
    height: 279px;
  }
  .expense-ul {
    width: 145px;
    height: 152px;
  }
  .expense-div-img {}
</style>
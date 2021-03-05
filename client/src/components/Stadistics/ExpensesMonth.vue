<template>
  <div class="last-month-expenses rounded-2xl shadow-md bg-white">
    <h1 class="text-left text-xl ml-8 mt-8 font-bold">Most expensive categories (last month)</h1>

    <ul v-if="currentExpenses" class="inset-y-2">
      <li 
        v-for="elem in zip(currentExpenses, expensesColors)" 
        v-bind:key="elem[0].name"
        class="text-left font-bold flex items-center"
      >
        <div :class="[elem[1], 'expense-li-square', 'rounded-md']"></div>
        <p class="pl-1">{{ elem[0].name }}</p>
      </li>
    </ul>

    <div></div>
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
      currentExpenses: null
    }
  },
  mounted() {
    this.currentExpenses = [
      {
        name: "Entertainment",
        value: 35000
      },
      {
        name: "Eating",
        value: 15790
      },
      {
        name: "Fitness",
        value: 500
      },
      {
        name: "Credit card",
        value: 55
      }
    ];
  },
  methods: {
    zip: function (arr, ...arrs) {
      return arr.map((val, i) => arrs.reduce((a, arr) => [...a, arr[i]], [val]));
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
</style>
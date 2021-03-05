<template>
  <div class="recurrent-expenses rounded-2xl shadow-md bg-white">
    <h1 class="text-left text-xl ml-8 mt-8 font-bold">Most expensive categories (recurrent)</h1>

    <div class="flex justify-center items-center pt-7 space-x-8">
      
      <ul v-if="currentExpenses" class="rec-expense-ul space-y-4 pt-6">
        <li 
          v-for="elem in zip(currentExpenses, expensesColors)" 
          v-bind:key="elem[0].category"
          class="text-left font-bold flex items-center"
        >
          <div :class="[elem[1], 'rec-expense-li-square', 'rounded-md']"></div>
          <h3 class="pl-1">{{ elem[0].category }}</h3>
        </li>
      </ul>

      <div
        v-if="currentExpenses"
        class="rec-expense-div-grid grid gap-4 grid-rows-2"
      >
        <div
          v-for="elem in zip(currentExpenses, expensesColors, expensesShadows)"
          v-bind:key="elem[0].category"
          :class="[elem[1], elem[2], 'rounded-2xl', 'rec-expense-div-square', 'space-y-1', 'flex', 'flex-col', 'justify-center', 'items-center']"
        > 
          <img :src="getImgUrl(elem[0].icon_name)" class="rec-expense-div-img block mx-auto">
          <h3 class="text-white font-bold truncate">${{ elem[0].value }}</h3>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  name: "expenses-recurrent",
  data() {
    return {
      expensesColors: [
        "black-expense-grad",
        "blue-expense-grad",
      ],
      expensesShadows: [
        "black-expense-shadow",
        "blue-expense-shadow",
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
  .recurrent-expenses {
    width: 440px;
    height: 405px;
  }
  .rec-expense-li-square {
    width: 17px;
    height: 17px;
  }
  .rec-expense-div-square {
    width: 125px;
    height: 125px;
  }
  .rec-expense-div-grid {
    width: 125px;
    height: 279px;
  }
  .rec-expense-ul {
    width: 145px;
    height: 152px;
  }
</style>
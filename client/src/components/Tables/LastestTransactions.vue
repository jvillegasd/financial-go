<template>
  <div class="flex flex-col items-center">
    <table-base class="lastest-table">
      <template v-slot:header>
        <tr style="height: 42px;">
          <th class="w-1/6 ...">Date</th>
          <th class="w-1/6 ...">Title</th>
          <th class="w-1/6 ...">Category</th>
          <th class="w-1/6 ...">Type</th>
          <th class="w-1/6 ...">Amount</th>
        </tr>
      </template>

      <template v-slot:body>
        <tr>
          <td class="font-medium">18/05</td>
          <td class="font-medium">Netflix</td>
          <td class="font-medium">Entertaiment</td>
          <td class="font-medium text-blue">Recurrent</td>
          <td class="font-medium text-blue">-$12</td>
        </tr>
        <tr>
          <td class="font-medium">17/05</td>
          <td class="font-medium">Salary</td>
          <td class="font-medium">Cash</td>
          <td class="font-medium text-dust">Income</td>
          <td class="font-medium text-dust">+$1200</td>
        </tr>
        <tr>
          <td class="font-medium">17/05</td>
          <td class="font-medium">Jeans</td>
          <td class="font-medium">Shopping</td>
          <td class="font-medium text-blue">Outcome</td>
          <td class="font-medium text-blue">-$15</td>
        </tr>
      </template>
    </table-base>

    <BlueButton
      class="see_more"
      title="See more"
      :width=132
      :height=35
      :fontSize=15
      :marginTop=8
    ></BlueButton>

  </div>
</template>

<script>
import TableBase from './TableBase.vue';
import BlueButton from '../Buttons/Blue_btn.vue';

export default {
  name: "lasted-transactions",
  components: {
    TableBase,
    BlueButton
  },
}
</script>

<style scoped>
  .lastest-table {
    height: 263px;
    width: 520px;
  }
  .see_more {
    box-shadow: 0px 4px 4px 0px rgba(0, 94, 238, 0.15);
  }
</style>
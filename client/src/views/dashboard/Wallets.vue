<template>
  <div>
    <h1 class="flex justify-start text-3xl font-bold 2xl:ml-20 xl:ml-0 mt-7">Wallets</h1>
  
    <div class="row flex justify-center mt-12">
      <div class="card-table rounded-2xl shadow-md bg-white flex flex-col justify-center items-center">
        
        <vs-table class="wallet-table">
          <template #thead>
            <vs-tr>
              <vs-th>
                <p class="font-medium text-lg text-center">Id</p>
              </vs-th>
              <vs-th>
                <p class="font-medium text-lg">Name</p>
              </vs-th>
              <vs-th>
                <p class="font-medium text-lg">Amount</p>
              </vs-th>
              <vs-th>
                <p class="font-medium text-lg">Date</p>
              </vs-th>
            </vs-tr>
          </template>

          <template #tbody>
            <vs-tr
              :key="i"
              v-for="(tr, i) in cards"
            >
              <vs-td>
                <p class="font-medium text-lg">{{ tr.id }}</p>
              </vs-td>
              <vs-td>
                <p class="font-medium text-lg">{{ tr.name }}</p>
              </vs-td>
              <vs-td>
                <p class="font-medium text-lg">{{ tr.amount }}</p>
              </vs-td>
              <vs-td>
                <p class="font-medium text-lg">{{ tr.date }}</p>
              </vs-td>
            </vs-tr>
          </template>


        </vs-table>

        <BlueButton
          class="font-medium mb-4"
          title="Create a wallet"
          :width=130
          :height=35
          :fontSize=16>
        </BlueButton>

      </div>
    </div>
  </div>
</template>

<script>
import BlueButton from '../../components/Buttons/Blue_btn.vue';

export default {
  name: 'Wallets',
  components: {
    BlueButton
  },
  data () {
    return {
      cards: [
        {
          id: "4",
          name: "Card 4",
          amount: "$0",
          date: "18/05/2021"
        },
        {
          id: "3",
          name: "Home wallet",
          amount: "$1200",
          date: "17/05/2021"
        },
        {
          id: "2",
          name: "Card 2",
          amount: "$50",
          date: "17/05/2021"
        },
        {
          id: "1",
          name: "Card 1",
          amount: "$600",
          date: "16/05/2021"
        }
      ]
    }
  },
  created() {
    this.$emit('selected-module', "wallets_module");
  }
}
</script>

<style scoped>
  .card-table {
    width: 998px;
  }
  .card-table .wallet-table {
    padding: 40px;
    overflow: hidden;
    height: auto;
    transition: all .25s ease;
  }
</style>
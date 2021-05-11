<template>
  <transition name="slide-fade">

    <div>
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-40 flex justify-center items-center" >
        <div class="relative mx-auto w-auto max-w-2xl">
          <div class="bg-white w-20 modal rounded-2xl flex flex-col items-center">
            
            <p class="text-center font-medium text-xl">New transaction</p>

            <Textbox
              label="Title"
              :width=245
              :labelFontSize=20
              :inputFontSize=25
              :isPassword=false>
            </Textbox>

            <select-transaction
              title="Type"
              :options="transaction_types"
            ></select-transaction>

            <Textbox
              label="Amount"
              :width=245
              :labelFontSize=20
              :inputFontSize=25
              :isPassword=false>
            </Textbox>

            <Textbox
              label="Date"
              :width=245
              :labelFontSize=20
              :inputFontSize=25
              :isPassword=false>
            </Textbox>

            <div>
              <select-transaction
              title="Category"
              :options="categories"
              :width=200
              @selected-option="setCategory">
              </select-transaction>
            </div>

            <BlueButton
              class="font-medium"
              title="Create transaction"
              :width=303
              :height=46
              :fontSize=18>
            </BlueButton>
            
          </div>
        </div>
      </div>

      <div class="absolute inset-0 z-10 opacity-25 bg-black"></div>
    </div>

  </transition>
</template>

<script>
import Textbox from '../../components/Textbox/Textbox';
import BlueButton from '../../components/Buttons/Blue_btn.vue';
import SelectTransaction from '../../components/Selectbox/SelectTransaction.vue';

export default {
  name: "transaction-modal",
  components: {
    Textbox,
    BlueButton,
    SelectTransaction
  },
  data() {
    return {
      show: false,
      transaction_types: [
        {
          value: 'income',
          text: 'Income'
        },
        {
          value: 'outcome',
          text: 'Outcome'
        },
        {
          value: 'recurrent',
          text: 'Recurrent'
        }
      ],
      categories: [
        {
          value: 'entertainment',
          text: 'Entertainment'
        },
        {
          value: 'cash',
          text: 'Cash'
        }
      ],
      selected_category: null
    };
  },
  methods: {
    setCategory: function (category) {
      this.selected_category = category;
      console.log(this.selected_category)
    }
  },
};
</script>

<style scoped>
  .modal {
    width: 486px;
    height: 652px;
  }
</style>
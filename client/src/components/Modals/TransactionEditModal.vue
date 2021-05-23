<template>
  <transition name="slide-fade">

    <div v-if="transactionData">
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-40 flex justify-center items-center" >
        <div class="relative mx-auto w-auto max-w-2xl">
          <div class="bg-white w-20 modal rounded-2xl flex flex-col items-center justify-center space-y-6">

            <exit-icon class="absolute top-5 right-5" @btn-pressed="modalClosed('exit')"></exit-icon>
            
            <p class="text-center font-bold text-2xl">Edit transaction</p>

            <div class="flex flex-col justify-center items-left space-y-6">
              <Textbox
                v-model="transactionData.title"
                label="Title"
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false>
              </Textbox>

              <select-transaction
                v-model="transactionData.type"
                title="Type"
                :options="transaction_types">
              </select-transaction>

              <Textbox
                label="Amount"
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false
                v-model="transactionData.amount">
              </Textbox>

              <Textbox
                label="Date"
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false
                v-model="transactionData.date">
              </Textbox>

              <div class="flex justify-center space-x-7">
                <select-transaction
                title="Category"
                :options="categories"
                :width=200
                v-model="transactionData.category">
                </select-transaction>

                <category-icon 
                :name="transactionData.category">
                </category-icon>
              </div>

              <BlueButton
                class="font-medium"
                title="Edit transaction"
                :width=303
                :height=46
                :fontSize=18
                @btn-pressed="modalClosed('edit')">
              </BlueButton>
            </div>
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
import CategoryIcon from '../../components/Misc/CategoryIcon.vue';
import ExitIcon from '../../components/Buttons/Exit_btn.vue';

export default {
  name: "transaction-edit-modal",
  props: {
    transactionData: {
      type: Object,
      default () {
        return {
          title: "sample title",
          type: "recurrent",
          amount: 10,
          date: "1/1/2021",
          category: "money"
        }
      }
    }
  },
  components: {
    Textbox,
    BlueButton,
    SelectTransaction,
    CategoryIcon,
    ExitIcon
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
          value: 'money',
          text: 'Money'
        },
        {
          value: 'shopping',
          text: 'Shopping'
        }
      ],
      category: null
    };
  },
  methods: {
    setCategory: function (category) {
      this.category = category;
    },
    modalClosed: function (optionPressed) {
      this.$emit('closed', optionPressed);
    }
  },
};
</script>

<style scoped>
  .modal {
    width: 486px;
    height: 682px;
  }
</style>
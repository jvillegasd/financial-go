<template>
  <transition name="slide-fade">

    <div>
      <div class="fixed overflow-x-hidden overflow-y-auto inset-0 z-40 flex justify-center items-center" >
        <div class="relative mx-auto w-auto max-w-2xl">
          <div class="bg-white w-20 modal rounded-2xl flex flex-col items-center justify-center space-y-6">

            <exit-icon class="absolute top-5 right-5" @btn-pressed="modalClosed"></exit-icon>
            
            <p class="text-center font-bold text-2xl">New transaction</p>

            <div class="flex flex-col justify-center items-left space-y-6">
              <Textbox
                label="Title"
                :width=303
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
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false>
              </Textbox>

              <Textbox
                label="Date"
                :width=303
                :labelFontSize=20
                :inputFontSize=25
                :isPassword=false>
              </Textbox>

              <div class="flex justify-center space-x-7">
                <select-transaction
                title="Category"
                :options="categories"
                :width=200
                @selected-option="setCategory">
                </select-transaction>
                <category-icon :name="selected_category"></category-icon>
              </div>

              <BlueButton
                class="font-medium"
                title="Create transaction"
                :width=303
                :height=46
                :fontSize=18
                @btn-pressed="modalClosed">
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
  name: "transaction-modal",
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
        }
      ],
      selected_category: null
    };
  },
  methods: {
    setCategory: function (category) {
      this.selected_category = category;
      console.log(this.selected_category)
    },
    modalClosed: function () {
      this.$emit('closed');
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
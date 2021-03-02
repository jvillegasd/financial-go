<template>
  <div class="cashflow shadow-md rounded-2xl bg-white">
    <h1 class="text-left text-2xl ml-8 mt-8 font-bold">Cashflow</h1>

    <div class="cashflow-data flex justify-around pt-4">
      <div class="text-left">
        <label class="font-bold text-grey-label text-xs">Daily</label>
        <h2 class="font-bold text-lg">${{ model.general.daily }}</h2>
      </div>
      <div class="text-left">
        <label class="font-bold text-grey-label text-xs">Weekly</label>
        <h2 class="font-bold text-lg">${{ model.general.weekly }}</h2>
      </div>
      <div class="text-left">
        <label class="font-bold text-grey-label text-xs">Monthly</label>
        <h2 class="font-bold text-lg">${{ model.general.monthly }}</h2>
      </div>
    </div>

    <div class="flex justify-around">
      <svg class="pt-2" height="10" width="310">
        <line x1="0" y1="0" x2="310" y2="0" opacity="0.5" style="stroke: rgb(174, 177, 184); stroke-width: 2;" />
      </svg>
    </div>

    <div class="my-4 ml-8">
      <selectbox
        class="cashflow-select"
        :options="selectData"
      ></selectbox>
    </div>

    <div class="flex flex-between">
      <div class="line-canvas ml-11" v-if="showChart">
        <donut-chart :chartData="chartdata" :options="options" :height="155" :width="155"></donut-chart>
      </div>

      <div class="space-y-6 ml-4 mt-3">

        <div class="flex justify-center items-center cashflow-label rounded-2xl bg-dust-25">
          <div class="pr-2">
            <svg width="12" height="18" viewBox="0 0 12 18" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M4.58249 1.00006L4.58249 14.17L1.70248 11.29C1.31248 10.9 0.68248 10.9 0.29248 11.29C0.10523 11.4769 0 11.7305 0 11.995C0 12.2595 0.10523 12.5132 0.29248 12.7L4.88249 17.29C5.27249 17.68 5.90249 17.68 6.29249 17.29L10.8825 12.7C11.2725 12.31 11.2725 11.68 10.8825 11.29C10.4925 10.9 9.86249 10.9 9.47249 11.29L6.58249 14.17L6.58249 1.00006C6.58249 0.45006 6.13249 5.91278e-05 5.58249 5.91278e-05C5.03249 5.91278e-05 4.58249 0.45006 4.58249 1.00006Z" fill="#EABA6B"/>
            </svg>
          </div>

          <div class="text-left">
            <h2 class="font-bold text-lg text-dust pt-1 truncate" style="width: 80px;">${{ model.income }}</h2>
            <p class="font-bold text-dust text-sm pl-1 -mt-2">Income</p>
          </div>
        </div>

        <div class="flex justify-center items-center cashflow-label rounded-2xl bg-blue-25">
          <div class="pr-2">
            <svg width="12" height="18" viewBox="0 0 12 18" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6.5925 16.5827L6.5925 3.41274L9.47251 6.29274C9.86251 6.68274 10.4925 6.68274 10.8825 6.29274C11.0698 6.10591 11.175 5.85226 11.175 5.58774C11.175 5.32322 11.0698 5.06957 10.8825 4.88274L6.2925 0.292744C5.9025 -0.0972559 5.2725 -0.0972559 4.8825 0.292744L0.292498 4.88274C-0.0975027 5.27274 -0.0975027 5.90274 0.292498 6.29274C0.682498 6.68274 1.3125 6.68274 1.7025 6.29274L4.5925 3.41274L4.5925 16.5827C4.5925 17.1327 5.0425 17.5827 5.5925 17.5827C6.1425 17.5827 6.5925 17.1327 6.5925 16.5827Z" fill="#005EEE"/>
            </svg>
          </div>

          <div class="text-left">
            <h2 class="font-bold text-lg text-blue pt-1 truncate" style="width: 80px;">${{ model.outcome }}</h2>
            <p class="font-bold text-blue text-sm pl-1 -mt-2">Outcome</p>
          </div>
        </div>

      </div>      
    </div>

  </div>
</template>

<script>
import DonutChart from "./DonutChart.vue";
import Selectbox from "../Selectbox/Selectbox.vue";

export default {
  name: "cash-flow",
  components: {
    DonutChart,
    Selectbox
  },
  data() {
    return {
      showChart: false,
      model: {
        general: {
          daily: 250.5,
          weekly: 250.5,
          monthly: 250.5
        },
        income: null,
        outcome: null
      },
      selectData: [
        {
          value: 'last_month',
          text: 'last month',
        }, 
        {
          value: 'last_week',
          text: 'last week'
        }
      ],
      chartdata: null,
      options: {
        tooltips: {
          mode: "nearest",
          displayColors: false,
          backgroundColor: "rgba(18, 24, 41, 1)",
          callbacks: {
            title: function(tooltipItem, data) {
              return data['labels'][tooltipItem[0]['index']];
            },
            label: function(tooltipItem, data) {
              return "$" + data['datasets'][0]['data'][tooltipItem['index']];
            }
          }
        },
        fullWidth: true,
        tooltipFontSize: 20,
        cutoutPercentage: 80,
        responsive: true,
        maintainAspectRatio: false,
        elements: {
          arc: {
            borderWidth: 0
          },
          center: {
            text: '$0' //set as you wish
          }
        },
        legend: {
          display: false,
        },
      }
    };
  },
  mounted() {
    this.fillData();
    this.showChart = true;
  },
  methods: {
    fillData() {
      this.model.income = this.getRandomInt();
      this.model.outcome = this.getRandomInt();
      
      this.chartdata = {
        labels: ["Income", "Outcome"],
        datasets: [
          {
            backgroundColor: ["#EABA6B", "rgba(0, 94, 238, 0.8)"],
            data: [
              this.model.income, 
              this.model.outcome
            ],
            fill: false,
            pointBackgroundColor: '#005EEE',
            pointHoverBackgroundColor: '#005EEE',
            pointBorderColor: '#005EEE',
            pointHoverBorderColor: '#005EEE'
          }
        ]
      }
    },
    getRandomInt () {
      return Math.floor(Math.random() * (1000000 - 5 + 1)) + 5;
    }
  }
}
</script>

<style scoped>
  .cashflow {
    width: 383px;
    height: 367px;
  }
  .line-canvas {
    width: 155px;
    height: 155px;
  }
  .cashflow-select {
    width: 110px;
    height: 16px;
  }
  .cashflow-label {
    height: 52px;
    width: 130px;
  }
</style>
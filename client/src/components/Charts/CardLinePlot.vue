<template>
  <div class="line-plot shadow-md rounded-2xl bg-white">
    <div class="text-left pl-6 pt-4">
      <label class="text-sm font-bold text-grey-label" v-if="is_income">Income (last 3 months)</label>
      <label v-else class="text-sm font-bold text-grey-label">Outcome (last 3 months)</label>
      <h1 class="text-2xl font-bold">{{ value }}</h1>
    </div>

    <div class="line-canvas">
      <line-chart :chartData="chartdata" :options="options" :height="95"></line-chart>
    </div>
  </div>
</template>

<script>
import LineChart from "./LineChart.vue";

export default {
  name: "card-line-plot",
  components: {LineChart},
  props: {
    is_income: {
      type: Boolean,
      default: true
    },
    id: String
  },
  data() {
    return {
      value: "$30.000",
      chartdata: null,
      options: {
        tooltips: {
          mode: "nearest",
          displayColors: false,
          backgroundColor: "rgba(18, 24, 41, 1)"
        },
        fullWidth: true,
        tooltipFontSize: 20,
        cutoutPercentage: 60,
        responsive: true,
        maintainAspectRatio: false,
        layout: {
            padding: {
                left: 0,
                right: 5,
                top: 3,
                bottom: 0
            }
        },
        legend: {
          display: false
        },
        scales: {
          xAxes: [{
            type: "category",
            labels: ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6", "Week 7", "Week 8", "Week 9", "Week 10", "Week 11", "Week 12", "Week 13"],
            gridLines: {
              color: "rgba(0, 0, 0, 0)",
              display: false,
            },
            ticks: {
              display: false
            }
          }],
          yAxes: [{
            gridLines: {
              color: "rgba(0, 0, 0, 0)",
              display: false,
            },
            ticks: {
              display: false
            }
          }],
        }
      }
    }
  },
  mounted() {
    this.fillData()
  },
  methods: {
    fillData () {
      this.chartdata = {
        datasets: [
          {
            backgroundColor: 'rgba(0, 94, 238, 0.8)',
            data: [
              this.getRandomInt(), 
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt(),
            ],
            fill: false,
            pointBackgroundColor: '#005EEE',
            pointHoverBackgroundColor: '#005EEE',
            borderColor: 'rgba(0, 94, 238, 0.8)',
            pointBorderColor: '#005EEE',
            pointHoverBorderColor: '#005EEE'
          }
        ]
      }
    },
    getRandomInt () {
      return Math.floor(Math.random() * (1000000 - 5 + 1)) + 5
    }
  }
}
</script>

<style scoped>
  .line-plot {
    width: 324px;
    height: 170px;
  }
  .line-canvas {
    width: 320px;
    height: 100px;
  }
</style>
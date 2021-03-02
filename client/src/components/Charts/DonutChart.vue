<script>
import { Doughnut, mixins } from 'vue-chartjs'

export default {
  extends: Doughnut,
  props: {
    chartData: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },
  mixins: [mixins.reactiveProp],
  mounted () {
    if (this.chartData && this.chartData.datasets) {
      let dataset = this.chartData.datasets;
      let total_value = "$" + (dataset[0].data[0] + dataset[0].data[1]);

      if (total_value.length > 10) {
        total_value = total_value.substring(0, 11) + "...";
      }

      this.textCenter(total_value);
    }
    this.renderChart(this.chartData, this.options);
  },
  methods: {
    textCenter(val) {
      this.addPlugin({
        id: "center-text",
        beforeDraw: function(chart) {
          var width = chart.chart.width,
            height = chart.chart.height,
            ctx = chart.chart.ctx;

          // Total label
          ctx.restore();
          var fontSize = 14 || (height / 114).toFixed(2);
          ctx.font = fontSize + "px GT Walsheim Pro Bold";
          ctx.textBaseline = "middle";
          ctx.fillStyle = "#AEB1B8";

          var text = "Total",
            textX = Math.round((width - ctx.measureText(text).width) / 2),
            textY = height / 2 - 14;

          ctx.fillText(text, textX, textY);
          ctx.save();


          // Total value
          ctx.restore();
          fontSize = 17 || (height / 114).toFixed(2);
          ctx.font = fontSize + "px GT Walsheim Pro Bold";
          ctx.textBaseline = "middle";
          ctx.fillStyle = "#1C202E";

          text = val,
            textX = Math.round((width - ctx.measureText(text).width) / 2),
            textY = height / 2 + 13;

          ctx.fillText(text, textX, textY);
          ctx.save();
        }
      });
    }
  }
}
</script>

<style>
</style>
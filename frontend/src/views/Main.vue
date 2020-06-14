<template>
  <div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col cols="9">
          <form action>
            <b-button>Save Table</b-button>
            <Table />
          </form>
        </b-col>
        <b-col cols="3">
          <chart :chart-data="datacollection"></chart>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import Table from "@/components/Table.vue";
import Chart from "@/components/Chart.js";
export default {
  components: {
    Table,
    Chart
  },
  data() {
    return {
      datacollection: null
    };
  },
  mounted() {
    this.datacollection = {
      labels: ["Jan", "Feb"],
      datasets: [
        {
          label: "Commits",
          data: [70, 30]
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
button {
  margin: 10px;
}
</style>
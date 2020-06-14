<template>
  <div>
    <b-container class="bv-example-row">
      <b-row>
        <div class="table-settings">
          <b-button>Save Table</b-button>
          <b-form-radio-group
            v-model="$store.state.default_currency"
            :options="$store.state.table.saving_sets"
            value-field="currency"
            text-field="desc"
          ></b-form-radio-group>
        </div>
      </b-row>
      <b-row>
        <Table />
      </b-row>
      <b-row>
        <chart :chart-data="datacollection"></chart>
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
      labels: ["Jan", "Feb", "May"],
      datasets: [
        {
          label: "Commits",
          data: [70, 30, 15]
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
.table-settings {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
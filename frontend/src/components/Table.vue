<template>
  <table>
    <tr>
      <td
        v-for="saving_set in $store.state.table.saving_sets"
        :key="saving_set.id"
      >{{ saving_set.desc }}</td>
      <td>Sum</td>
    </tr>
    <Row v-for="row in $store.state.table.data" :key="row.date" v-bind:row="row.savings" />
  </table>
</template>

<script>
import Row from "@/components/Row";

export default {
  mounted() {
    this.$store.dispatch("getTableData");
  },
  components: {
    Row
  }
};
</script>

<style lang="scss">
table,
td,
tr {
  border: 1px solid #333;
  border-collapse: collapse;
}
td {
  padding: 7px;
}
</style>

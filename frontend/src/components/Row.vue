<template>
  <tr>
    <Cell v-for="saving in row" :key="saving.id" v-bind:saving="saving" />
    <td>{{ sum }}</td>
  </tr>
</template>

<script>
import Cell from "@/components/Cell";

export default {
  props: { row: Array },
  components: {
    Cell
  },
  computed: {
    sum() {
      let acc = 0;
      this.row.forEach(saving => {
        if (saving.code === this.$store.state.default_currency) {
          acc += saving.amount;
        } else {
          let rate = saving.exchange.filter(
            rate => rate.code === this.$store.state.default_currency
          )[0].price;
          acc += saving.amount * rate;
        }
      });

      return acc.toFixed(2);
    }
  }
};
</script>

<style lang="scss" scoped></style>

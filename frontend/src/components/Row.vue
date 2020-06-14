<template>
  <tr>
    <Cell v-for="saving in row" :key="saving.id" v-bind:saving="saving" />
  </tr>
</template>

<script>
import Cell from "@/components/Cell";

export default {
  props: { row: Array },
  components: {
    Cell
  }
};
</script>

<style lang="scss" scoped>
</style>
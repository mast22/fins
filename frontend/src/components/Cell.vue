<template>
  <td>
    <input type="number" :value="saving.amount" :name="saving.id" step="0.01" @blur="inputBlured" />
  </td>
</template>

<script>
export default {
  props: { saving: Object },
  methods: {
    inputBlured(e) {
      this.$store.dispatch("set_saving_value", {
        value: e.target.valueAsNumber,
        id: e.originalTarget.name
      });
    }
  }
};
</script>

<style lang="scss" scoped>
td {
  padding: 2px;
}
input {
  border: none;
  box-shadow: none;
  padding: 5px;
  -moz-appearance: textfield;
}
</style>
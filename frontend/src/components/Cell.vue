<template>
  <td>
    <input type="number" :value="saving.amount" :name="saving.id" />
  </td>
</template>

<script>
export default {
  props: { saving: Object }
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
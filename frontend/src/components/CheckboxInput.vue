<template>
  <div class="form-control">
    <label>{{ field.label }}</label>
    <label class="input">
      <input type="checkbox" v-model="data.value">
      {{ field.placeholder }}
    </label>
  </div>
</template>

<script>
export default {
  name: 'CheckboxInput',
  props: {
    field: { required: true },
    data: { required: true }
  }
}
</script>

<style scoped>

</style>

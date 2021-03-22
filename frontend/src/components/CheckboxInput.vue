<template>
  <div class="form-control">
    <label>{{ field.name }}</label>
    <label class="input">
      <input type="checkbox">
      {{ field.placeholder }}
    </label>
  </div>
</template>

<script>
export default {
  name: 'CheckboxInput',
  props: {
    field: { required: true }
  }
}
</script>

<template>
  <div class="form-control">
    <label>{{ field.name }}</label>
    <label class="input">
      <input class="input" type="number">
    </label>
  </div>
</template>

<script>
export default {
  name: 'NumberInput',
  props: {
    field: { required: true },
    data: { required: false }
  }
}
</script>

<style scoped>

</style>

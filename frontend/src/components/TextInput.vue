<template>
  <div class="form-control">
    <label>{{ field.name }}</label>
    <label class="input">
      <input class="input" type="text">
    </label>
  </div>
</template>

<script>
export default {
  name: 'TextInput',
  props: {
    field: { required: true },
    data: { required: false }
  }
}
</script>

<style scoped>

</style>

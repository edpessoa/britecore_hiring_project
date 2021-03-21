<template>
  <div class="form-control">
    <label>{{ field.label }}</label>
    <input class="input" type="text" :placeholder="field.placeholder" v-model="data.value">
  </div>
</template>

<script>
export default {
  name: 'TextInput',
  props: {
    field: { required: true },
    data: { required: true }
  }
}
</script>

<style scoped>

</style>

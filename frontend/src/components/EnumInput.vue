<template>
  <div class="form-control">
    <label>{{ field.name }}</label>
    <label class="input">
      <select>
        <option v-for="option in field.options" v-bind:key="option">
          {{ option }}
        </option>
      </select>
    </label>
  </div>
</template>

<script>
export default {
  name: 'EnumInput',
  props: {
    field: { required: true },
    data: { required: false }
  }
}
</script>

<style scoped>

</style>

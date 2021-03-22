<template>
  <div class="form-control">
    <label>{{ field.name }}</label>
    <label class="input">
      <Datepicker placeholder="Click to choose a date"></Datepicker>
    </label>
  </div>
</template>

<script>
import Datepicker from 'vuejs-datepicker'

export default {
  name: 'DateInput',
  components: { Datepicker },
  props: {
    field: { required: true },
    data: { required: false }
  }
}
</script>

<style scoped>

</style>

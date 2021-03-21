<template>
  <div class="d-form">
    <template v-for="field in schema.fields">
      <component :is="field.type" :field="field" :data.sync="data[field.name]"></component>
    </template>
  </div>
</template>

<script>
import TextInput from '@/components/TextInput'
import CheckboxInput from '@/components/CheckboxInput'

export default {
  name: 'DForm',

  components: {
    TextInput,
    CheckboxInput
  },

  props: {
    schema: { required: true },
    data: { required: false }
  }
}
</script>

<style scoped>
html, body {
  font-family: sans-serif;
}

.form-control {
  padding: 8px 16px;
}

.form-control label+.input {
  display: block;
}

</style>

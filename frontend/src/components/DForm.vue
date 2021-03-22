<template>
  <div class="d-form">
    <template v-for="field in schema.fields">
      <component :is="field.type + '-input'" :field="field" v-bind:key="field"></component>
    </template>
  </div>
</template>

<script>
import TextInput from '@/components/TextInput'
import CheckboxInput from '@/components/CheckboxInput'
import EnumInput from '@/components/EnumInput'
import DateInput from '@/components/DateInput'
import NumberInput from '@/components/NumberInput'

export default {
  name: 'DForm',

  components: {
    TextInput,
    CheckboxInput,
    EnumInput,
    DateInput,
    NumberInput
  },

  props: {
    schema: { required: true },
    data: { required: false }
  }
}
</script>

<style>
.form-control {
  padding: 0.5rem 8rem;
}

.form-control label+.input {
  display: block;
}
</style>

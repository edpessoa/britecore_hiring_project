<template>
  <div id="app">
    <h1>Risk Type Forms</h1>
    <div class="loop" v-for='risk in risks' :key='risk.id'>
      <label>Form name: {{risk.name}}</label>
      <br>
      <label>Fields:</label>
      <d-form :schema="risk"></d-form>
    </div>
  </div>
</template>

<script>
import DForm from '@/components/DForm'

export default {
  name: 'RiskTypeForm',
  components: { DForm },
  computed: {
    risks () {
      return this.$store.state.risks.risks
    }
  },
  mounted () {
    this.$store.dispatch('getRisksList')
  }
}
</script>

<style scoped>
  h1 {
    text-align: center;
  }

  .loop {
    background: #f2f2f2;
    border: 1px solid #ddd;
    padding: 1rem 1em 1em;
    margin-bottom: 1rem;
    position: relative;
  }
  .loop label {
    padding-left: 5rem;
    display: block;
  }
</style>

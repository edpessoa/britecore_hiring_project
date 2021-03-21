<template>
  <div id="app">
      New user:
        <d-form :schema="formSchema" :data="formData"></d-form>
      <hr>
      Users list:
      <div v-for='user in users' :key='user.id'>
        {{user.email}}
      </div>
  </div>
</template>

<script>
import DForm from '@/components/DForm'

export default {
  name: 'RiskTypeForm',
  components: { DForm },
  computed: {
    users () {
      return this.$store.state.users.users
    }
  },
  mounted () {
    this.$store.dispatch('getUsersList')
  },
  data () {
    return {
      formSchema: {
        fields: [
          {
            type: 'text-input',
            name: 'first_name',
            label: 'First name',
            placeholder: 'Enter first name'
          },
          {
            type: 'text-input',
            name: 'last_name',
            label: 'Last name',
            placeholder: 'Enter last name'
          },
          {
            type: 'checkbox-input',
            name: 'is_admin',
            label: 'Administrator',
            placeholder: 'Sure, why not'
          }
        ]
      },
      formData: {
        first_name: {
          value: ''
        },
        last_name: {
          value: ''
        },
        is_admin: {
          value: false
        }
      }
    }
  }
}
</script>

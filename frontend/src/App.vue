<template lang="html">
  <div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  h1 {
    text-align: center;
  }

  #app {
    font-family: 'Titillium Web', sans-serif;
  }

  .form-control {
    padding: 8px 16px;
  }

  .form-control label+.input {
    padding-left: 20px;
    display: block;
  }

</style>

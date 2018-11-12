<template>
  <div id="app">
    <img src="./assets/logo.png">
    <button v-on:click.prevent="getCompanies">Get companies</button>
    <router-view/>
  </div>
</template>

<script>
let options = {
  url: 'http://localhost/api/company',
  method: 'GET',
  headers:
    {
      Authorization: 'Basic ZXlKaGJHY2lPaUpJVXpJMU5pSXNJbWxoZENJNk1UVTBNVGsyT1RBek1Td2laWGh3SWpveE5UUXhPVFk1TmpNeGZRLmV5SnBaQ0k2TVgwLjlWRklIWWFHNmxVNDBEM0kxY2x0dnhkRFpMVDFKTjNHNktfeGQyT0szWnc6dGVzdA=='
    }
}
export default {
  name: 'App',
  methods: {
    getCompanies: function () {
      this.$http(options).then((response) => {
        console.log(response)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

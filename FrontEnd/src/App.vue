<template>
  <div id="app">
    <!--navbar-->
    <nav class="uk-navbar-container" uk-navbar>
      <div class="uk-navbar-left">
        <ul class="uk-navbar-nav">
          <li><a href="#">XXX</a></li>
          <li>
            <a href="#">XXX</a>
            <div class="uk-navbar-dropdown">
              <ul class="uk-nav uk-navbar-dropdown-nav">
                <li><a href="#">XXX</a></li>
                <li><a href="#">XXX</a></li>
                <li><a href="#">XXX</a></li>
              </ul>
            </div>
          </li>
          <li><a href="#">XXX</a></li>
        </ul>
      </div>
      <div class="uk-navbar-right">
        <ul class="uk-navbar-nav">
          <li><a href="#">XXX</a></li>
          <li>
            <a href="#">XXX</a>
            <div class="uk-navbar-dropdown">
              <ul class="uk-nav uk-navbar-dropdown-nav">
                <li><a href="#">XXX</a></li>
                <li><a href="#">XXX</a></li>
                <li><a href="#">XXX</a></li>
              </ul>
            </div>
          </li>
          <li><a href="#">XXX</a></li>
        </ul>
      </div>
    </nav>
    <!--router-view-->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!--<style>-->
<!--#app {-->
  <!--font-family: 'Avenir', Helvetica, Arial, sans-serif;-->
  <!-- -webkit-font-smoothing: antialiased;-->
  <!-- -moz-osx-font-smoothing: grayscale;-->
  <!--text-align: center;-->
  <!--color: #2c3e50;-->
  <!--margin-top: 60px;-->
<!--}-->

<!--h1, h2 {-->
  <!--font-weight: normal;-->
<!--}-->

<!--ul {-->
  <!--list-style-type: none;-->
  <!--padding: 0;-->
<!--}-->

<!--li {-->
  <!--display: inline-block;-->
  <!--margin: 0 10px;-->
<!--}-->

<!--a {-->
  <!--color: #42b983;-->
<!--}-->
<!--</style>-->

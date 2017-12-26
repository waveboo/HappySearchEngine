<template>
  <div id="app">
    <!--navbar-->
    <div uk-sticky="sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky">
      <nav class="uk-navbar-container" uk-navbar>
        <div class="uk-navbar-left">
          <a class="uk-navbar-item uk-logo" href="/">HappySearch</a>
        </div>
        <div class="uk-navbar-right">
          <ul class="uk-navbar-nav">
            <li><a href="javascript:void(0)" v-on:click="switchto()">Skin</a></li>
            <li>
              <a href="#">Pattern</a>
              <div class="uk-navbar-dropdown">
                <ul class="uk-nav uk-navbar-dropdown-nav">
                  <li><a href="javascript:void(0)" v-on:click="patternto(0)">Weakness(default)</a></li>
                  <li><a href="javascript:void(0)" v-on:click="patternto(1)">Strength</a></li>
                </ul>
              </div>
            </li>
            <li>
              <a href="#">Links</a>
              <div class="uk-navbar-dropdown">
                <ul class="uk-nav uk-navbar-dropdown-nav">
                  <li><a href="javascript:void(0)" v-on:click="linkto('http://www.google.com')">Google</a></li>
                  <li><a href="javascript:void(0)" v-on:click="linkto('http://www.baidu.com')">Baidu</a></li>
                  <li><a href="javascript:void(0)" v-on:click="linkto('http://cn.bing.com')">Bing</a></li>
                  <li><a href="javascript:void(0)" v-on:click="linkto('http://www.sogou.com')">Sogou</a></li>
                </ul>
              </div>
            </li>
          </ul>
        </div>
      </nav>
    </div>
    <!--router-view-->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  data () {
    return {
      pattern:0,
      background: 0 ,
      msg: 'Welcome to Your Vue.js App'
    }
  },
  computed:{
   pattern(){
      return this.pattern
    },
    background(){
      return this.background
    }
  },
  methods: {
      patternto:function(e){
        this.pattern = e
      },
      switchto:function(){
          if(this.background != 2 ){
              this.background = this.background + 1
          }
          else{
              this.background = 0
          }
          if(this.background == 1){
//              $("body").css()
              $("body").css("background","url(http://booboo.oss-cn-shenzhen.aliyuncs.com/MyLinux/1.jpg) repeat 0 0")
          }
          else if(this.background == 2){
              $("body").css("background","url(http://booboo.oss-cn-shenzhen.aliyuncs.com/MyLinux/2.jpg) repeat 0 0")
          }
          else{
              $("body").css("background","#fff")
          }
      },
      linkto:function(e){
        console.log(e)
        location.href = e
      }
  }
}
</script>

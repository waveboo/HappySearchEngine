<template>
  <div>
    <!--add a logo-->
    <div class="uk-width-auto  uk-transition-toggle uk-margin-small">
      <img class="uk-border-circle uk-width-1-5 uk-align-center uk-transition-scale-up uk-transition-opaque" width="20" height="20" alt="logo" src="http://booboo.oss-cn-shenzhen.aliyuncs.com/MyLinux/logo.jpg">
    </div>

    <!--add search form-->
    <form class="uk-width-2-5 uk-margin uk-align-center uk-search uk-search-default" @submit.prevent>
      <div class="uk-width-auto uk-align-center">
        <a href="javascript:void(0)" v-on:click="submit()" class="uk-search-icon-flip" uk-search-icon></a>
        <input id = "Sinput" v-on:keyup.enter="submit()" v-model="searchKey" class="uk-search-input" type="search" placeholder="Search..." name="word" HaoyuSug="FAF36EAE1E4E4D3892DD09A63B688E3D">
      </div>
    </form>
  </div>
</template>

<script>
  export default {
    name: 'ToSearchPage',
    data() {
      return {
        searchKey: ''
      }
    },
    methods: {
        submit:function () {
          this.searchKey = $("#Sinput").val();
          this.$store.dispatch('updateSearchkey',this.searchKey);
          this.$router.push({ path: '/search' });
        }
    }
  }
  //v-bind:value="searchKey"  v-on:input="searchKey = $event.target.value"
</script>

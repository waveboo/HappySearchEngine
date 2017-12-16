<template>
  <div>
    <form class="uk-width-2-5 uk-margin uk-align-center uk-search uk-search-default uk-margin-medium-top" @submit.prevent>
      <div class="uk-width-auto uk-align-center">
        <a href="javascript:void(0)" v-on:click="submit()" class="uk-search-icon-flip" uk-search-icon></a>
        <input id = "Sinput" v-on:keyup.enter="submit()" v-model="searchKey" class="uk-search-input" type="search" placeholder="Search..." name="word" HaoyuSug="FAF36EAE1E4E4D3892DD09A63B688E3D">
      </div>
    </form>
    <div class="uk-margin-large-left uk-margin-large-right" v-for="(answer,index) in Answer">
      <div class="uk-card uk-card-hover uk-card-body uk-width-1-1@m">
        <h3 class="uk-card-title">{{answer.title}}</h3>
        <p>{{answer.abstract}}</p>
        <a href="javascript:void(0)" v-on:click="linkto(index)" target="_blank">链接...</a>
      </div>
      <hr/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DealSearch',
  data() {
    return{
        SearchKey:this.$store.state.SearchKey,
        PageCut:{
            current:1,
            showItem:6,
            AllPage:1
        }
    }
  },
  computed:{
      SearchKey(){
          return this.$store.state.SearchKey
      },
      Answer(){
          this.PageCut.AllPage = Math.ceil(this.$store.state.SearchList.length / this.PageCut.showItem)
          if(this.PageCut.AllPage == 0){
            this.PageCut.AllPage = 1;
          }
          return this.$store.state.SearchList
      }
  },
  mounted(){
    this.deal()
  },
  methods: {
    deal:function () {
      this.$http.post("http://120.78.90.129:5000/search",
          {
            searchKey:this.$store.state.SearchKey
          },
          {
            headers: {'Content-Type':'application/json; charset=UTF-8'}
          }
      ).then(function(res){
          var Answers = JSON.parse(res.bodyText);
          this.$store.dispatch('ClearSearchList');
          for(let answer in Answers){
            var item = JSON.parse(Answers[answer]);
            this.$store.dispatch('AddinSearchList',item);
          }
      },function(response){
        alert('错误！ '+ JSON.stringify(response));
      });
    },
    submit:function(){
      this.searchKey = $("#Sinput").val();
      this.$store.dispatch('updateSearchkey',this.searchKey);
      this.deal();
    },
    linkto:function(index){
      window.open(this.$store.state.SearchList[index].link);
    }
  }
}
</script>

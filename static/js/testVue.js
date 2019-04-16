/**
 * Created by Dimerick on 26/08/2018.
 */
var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
});

var app4 = new Vue({
  el: '#app-4',
  data: {
    todos: []
  },
  created: function(){
    this.$http.get('http://elatlas.org/inventario').then(function(response){
      this.todos = response.body;
    }, function(){
      alert('Error!');
    });

  }
});

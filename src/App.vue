<template>
  <div id="app">
    
  <div class="header">
    <h1>FactApp4</h1>
    
    <img src="./assets/logo.svg" class="logo">
  </div>
  <div class="main-component">
  <Index/>
  </div>

</div>

</template>

<script>

import Index from './components/Index';
import ListarCliente from "./components/ListarCliente";


export default {
  name: 'App',
  components: {
    Index 
  },
  data: function(){
    return {
      is_auth: localStorage.getItem('isAuth') || false
}
},
  methods: {
    navegarClientes: function() {
    this.$router.push({ name: "verClientes" });
    }
  },
  
}
</script>

<style>
  *{
    margin:0;
    padding: 0;
    box-sizing: border-box;
  }

  .logo{
    width: 100px;
  }
  .header{
    margin: 0;
    padding: 0;
    width: 100%;
    min-width: 375px;
    height: 150px;
    min-height: 100px;
    background-color: #4d4d4d ;
    color:#ffffff ;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
  .header h1{
    width: auto;
    }
  .main-component{
    text-align:center;
    height: 130vh;
    min-width: 375px;
    width: auto;
    padding: 0%;
    background: #2d2d2d ;
    color:#ffffff;
    overflow: hidden;
}

@media screen and (min-width: 375px) {
  .header{ 
    flex-direction: row;
  }
}
</style>

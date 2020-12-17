<template>
  <div class="center">
    <h2>Inicio de Sesión</h2>

    <label for="">Cédula</label>
    <vs-input
      primary
      v-model="cedula"/>
    
    <label for="">Password</label>
    <vs-input
    primary
    v-model="password"/>
  
    <vs-button v-on:click="loginUsuario">
       Iniciar Sesion
       <template #animate >
       <i class='bx bx-check-double' ></i>
       </template>
     </vs-button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Login",
  data: function() {
    return {
      cedula: "",
      password: ""
    };
  },
  methods: {
    loginUsuario: function() {
      var ced = parseInt(this.cedula,10)
      console.log(typeof(ced));
      var datosJson = {
        cedula: ced,
        password: this.password
      };
      console.log(datosJson);
      axios
      //https://factapp4.herokuapp.com/usuario/login/
        .post("https://factapp4.herokuapp.com/usuario/login/", datosJson)
        .then(response => {
          alert(response.data.mensaje);
        })
        .catch(err => {
          console.log(err);
          alert("error en el servidor");
        });
    }
  }
};
</script>

<style>
  .vs-input{
  padding: 0 1rem;
  margin: 1rem;
  width: 200px;
  margin-left: auto;
  margin-right: auto;
}

    
  .vs-button{
  padding: 0 1rem;
  margin: 1rem;
  width: 200px;
  margin-left: auto;
  margin-right: auto;
}
</style>
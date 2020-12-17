import VueRouter from "vue-router";
import ListarCliente from "./components/ListarCliente";
import AgregarCliente from "./components/AgregarCliente";
import Login from "./components/Login";
import App from './App';

const router = new VueRouter({
  routes: [
    { name: "verClientes", path: "/ver", component: ListarCliente},
    {
      name: "agregarCliente",
      path: "/agregar",
      component: AgregarCliente
    },
    {
      name: "inicioSesion",
      path: "/login",
      component: Login
    }
  ]
});

export default router;
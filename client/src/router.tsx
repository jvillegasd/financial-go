import { RouteDefinition } from "@solidjs/router";
import Login from "./pages/auth/login";
import Home from "./pages/home/home";

const routes: RouteDefinition[] = [
  {
    path: "/",
    component: () => <Home />,
  },
  {
    path: "/login",
    component: () => <Login />,
  }
];

export default routes;

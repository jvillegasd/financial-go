import { RouteDefinition } from "@solidjs/router";
import Home from "./pages/home/home";

const routes: RouteDefinition[] = [
  {
    path: "/",
    component: () => <Home />,
  },
];

export default routes;

import { ReactLocation, Route } from "@tanstack/react-location";
import { Home } from "./pages/home/home";

export const routes: Route[] = [
  {
    path: "/",
    element: <Home />,
  },
];

export const location = new ReactLocation();
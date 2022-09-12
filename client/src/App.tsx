import { Outlet, Router } from "@tanstack/react-location";
import { location, routes } from "./router";

function App() {
  return (
    <Router location={location} routes={routes}>
      <Outlet />
    </Router>
  );
}

export default App;

import { JSX } from "solid-js";
import { Header } from "./headers/header";

export const Layout = ({ children }: { children: JSX.Element }) => {
  return (
    <>
      <Header />
      {children}
    </>
  );
};

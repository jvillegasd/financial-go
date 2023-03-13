import { JSXElement } from "solid-js";
import Logo from "../../components/logo";

const LoginLayout = ({ children = "" }: { children?: JSXElement }) => (
  <div class="h-screen bg-split-blue-white">
    <div class="h-full grid grid-cols-1 grid-rows-3 items-center justify-center">
      <div class="flex justify-center">
        <Logo class="self-end" />
      </div>
      <div class="self-start flex justify-center">{children}</div>
    </div>
  </div>
);

export default LoginLayout;

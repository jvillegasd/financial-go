import { ReactNode } from "react";
import Logo from "../../components/logo";

const LoginLayout = ({ children = "" }: { children?: ReactNode }) => (
  <div className="h-screen bg-split-blue-white">
    <div className="h-full grid grid-cols-1 grid-rows-3 items-center justify-center">
      <div className="flex justify-center">
        <Logo className="self-end" />
      </div>
      <div className="self-start flex justify-center">{children}</div>
    </div>
  </div>
);

export default LoginLayout;

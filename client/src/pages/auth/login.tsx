import { Link } from "@solidjs/router";
import LoginLayout from "../../sections/layout/login-layout";

const Login = () => (
  <LoginLayout>
    <div class="bg-white rounded-4xl py-12 px-16">
        <h1 class="text-4xl text-text">Login</h1>
        <form>
          <div class="flex flex-col">
            <label>Email</label>
            <input type="email" name="email" />
          </div>
          <div class="flex flex-col">
            <label>Password</label>
            <input type="password" name="password" />
          </div>
        </form>
        <p>Don’t have an account?<Link href="/signup">Sign up</Link></p>
    </div>
  </LoginLayout>
);

export default Login;

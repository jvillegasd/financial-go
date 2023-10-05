import Link from "next/link";

const Login = () => (
  <div className="bg-white rounded-4xl py-12 px-16">
    <h1 className="text-4xl text-text">Login</h1>
    <form>
      <div className="flex flex-col">
        <label>Email</label>
        <input type="email" name="email" />
      </div>
      <div className="flex flex-col">
        <label>Password</label>
        <input type="password" name="password" />
      </div>
    </form>
    <p>
      Don’t have an account?<Link href="/signup">Sign up</Link>
    </p>
  </div>
);

export default Login;

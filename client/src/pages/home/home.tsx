import { Button } from "../../components/button";

export const Home = () => {
  return (
    <div className="h-screen flex flex-col justify-between">
      <header className="w-full flex items-center justify-end">
        <nav className="flex gap-4 py-8 px-12">
          <Button appearance="link">About</Button>
          <Button appearance="outlined">Sign In</Button>
        </nav>
      </header>
      <main className="h-full w-full flex">
        <div className="flex flex-col items-center justify-center px-16 w-3/6 z-50">
          <h1 className="text-6xl font-normal mb-8">Financial Go</h1>
          <h2 className="my-7 font-normal text-4xl text-center">The easiest way to manage your budget.</h2>
          <Button>Start saving</Button>
        </div>
        <div className="w-3/6 h-full z-0" >
          <div className="h-full overflow-visible relative flex items-center">
            <img className="top-0" src="src/assets/images/Icon_big.png" alt="" />
          </div>
        </div>
      </main>
    </div>
  );
};

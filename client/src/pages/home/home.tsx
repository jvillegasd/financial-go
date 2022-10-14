import type { Component } from 'solid-js';
import { Button } from "../../components/button";

const Home: Component = () => {
  return (
    <div class="h-screen flex flex-col justify-between">
      <header class="w-full flex items-center justify-end">
        <nav class="flex gap-4 py-8 px-12">
          <Button appearance="link">About</Button>
          <Button appearance="outlined">Sign In</Button>
        </nav>
      </header>
      <main class="h-full w-full flex">
        <div class="flex flex-col items-center justify-center px-16 w-3/6 z-50">
          <h1 class="text-6xl font-normal mb-8">Financial Go</h1>
          <h2 class="my-7 font-normal text-4xl text-center">The easiest way to manage your budget.</h2>
          <Button>Start saving</Button>
        </div>
        <div class="w-3/6 h-full z-0" >
          <div class="h-full overflow-visible relative flex items-center">
            <img class="top-0" src="src/assets/images/Icon_big.png" alt="" />
          </div>
        </div>
      </main>
    </div>
  );
};

export default Home;
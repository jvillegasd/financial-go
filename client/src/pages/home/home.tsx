import { A } from "@solidjs/router";
import type { Component } from "solid-js";
import CharityIcon from "../../assets/icons/charity";
import { Button } from "../../components/button";

const Home: Component = () => {
  return (
    <div class="h-screen flex flex-col justify-between">
      <header class="w-full flex items-center justify-end">
        <nav class="flex gap-4 py-8 px-12">
          <Button appearance="link">About</Button>
          <A href="/login"><Button appearance="outlined">Sign In</Button></A>
        </nav>
      </header>
      <main class="h-full w-full flex">
        <div class="flex flex-col items-center justify-center mx-auto w-3/6 z-50">
          <CharityIcon size={160} />
          <h1 class="text-6xl font-normal my-2">Financial Go</h1>
          <h2 class="mb-7 font-normal text-4xl text-center">
            The easiest way to manage your budget.
          </h2>
          <Button>Start saving</Button>
        </div>
      </main>
    </div>
  );
};

export default Home;

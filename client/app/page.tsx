import CharityIcon from "@/icons/charity";
import { Button } from "@nextui-org/button";
import { Link } from "@nextui-org/link";
import NextLink from "next/link";

const Home = () => {
  return (
    <div className="h-screen flex flex-col justify-between">
      <header className="w-full flex items-center justify-end">
        <nav className="flex gap-4 py-8 px-12">
          <Button color="primary" variant="light" className="px-10">
            About
          </Button>
          <Link href="/login" as={NextLink}>
            <Button color="primary" variant="bordered" className="px-10">
              Sign In
            </Button>
          </Link>
        </nav>
      </header>
      <main className="h-full w-full flex">
        <div className="flex flex-col items-center justify-center mx-auto w-3/6 z-50">
          <CharityIcon size={160} />
          <h1 className="text-6xl font-normal my-2">Financial Go</h1>
          <h2 className="mb-7 font-normal text-4xl text-center">The easiest way to manage your budget.</h2>
          <Button color="primary" className="px-10">
            Start saving
          </Button>
        </div>
      </main>
    </div>
  );
};

export default Home;

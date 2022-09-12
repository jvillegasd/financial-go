export const Header = () => {
  return (
    <header className="bg-gray-900 text-white py-4">
      <div className="container mx-auto px-6 flex justify-between items-center">
        <a href="#" className="text-2xl font-bold">
          My App
        </a>
        <nav>
          <ul className="flex">
            <li>
              <a href="#" className="px-3 py-2 rounded-md text-sm font-medium">
                Home
              </a>
            </li>
            <li>
              <a href="#" className="px-3 py-2 rounded-md text-sm font-medium">
                About
              </a>
            </li>
            <li>
              <a href="#" className="px-3 py-2 rounded-md text-sm font-medium">
                Contact
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#337EF1",
      },
      fontFamily: {
        sans: ["GT Walsheim Pro", "sans-serif"],
      },
      backgroundImage: {
        'hero': "url('/src/assets/images/Icon_big.png')",
      }
    },
  },
  plugins: [],
};

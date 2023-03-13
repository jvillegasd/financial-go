/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#337EF1",
        background: "#F4F4F4",
        text: "#1C202E",
      },
      fontFamily: {
        sans: ["GT Walsheim Pro", "sans-serif"],
      },
      backgroundImage: {
        hero: "url('/src/assets/images/Icon_big.png')",
        "split-blue-white":
          "linear-gradient(to bottom, #337EF1 0%, #337EF1 40%, #F4F4F4 40%, #F4F4F4 100%)",
      },
      borderRadius: {
        "4xl": "3.375rem",
      },
    },
  },
  plugins: [],
};

const tinycolor = require('tinycolor2');

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    screens: {
      'xs': '240px',
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    },
    colors: {
      "blue": "#005EEE",
      "blue-80": tinycolor("#005EEE").setAlpha(0.8).toRgbString(),
      "black": "#1C202E",
      "grey-bg": "#F4F4F4",
      "white": "#FFFFFF"
    },
    fontFamily: {
      regular: ["GT Walsheim Pro Regular", "sans-serif"],
      medium: ["GT Walsheim Pro Medium", "sans-serif"],
      bold: ["GT Walsheim Pro Bold", "sans-serif"],
    },
    extend: {
      "spacing": {
        "c-500": "500px",
      }
    }
  },
  variants: {},
  plugins: [],
}
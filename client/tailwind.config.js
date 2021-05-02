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
      "dust": "#EABA6B",
      "blue-80": tinycolor("#005EEE").setAlpha(0.8).toRgbString(),
      "blue-25": tinycolor("#005EEE").setAlpha(0.25).toRgbString(),
      "dust-25": tinycolor("#EABA6B").setAlpha(0.25).toRgbString(),
      "grey-table": tinycolor("#C4C4C4").setAlpha(0.07).toRgbString(),
      "grey-select": tinycolor("#C4C4C4").setAlpha(0.25).toRgbString(),
      "black": "#1C202E",
      "grey-bg": "#F4F4F4",
      "white": "#FFFFFF",
      "purple": "#7562FF",
      "seablue": "#33C9FF",
      "grey-label": "#AEB1B8"
    },
    fontFamily: {
      regular: ["GT Walsheim Pro Regular", "sans-serif"],
      medium: ["GT Walsheim Pro Medium", "sans-serif"],
      bold: ["GT Walsheim Pro Bold", "sans-serif"],
    },
    extend: {
      "spacing": {
        "c-507": "507px",
      }
    }
  },
  variants: {},
  plugins: [],
}
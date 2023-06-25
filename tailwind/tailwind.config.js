/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'black': {
          400 : '#404040'
        },
        'brown': {
          400: '#A17878'
        }
      }
    },
  },
  plugins: [],
}
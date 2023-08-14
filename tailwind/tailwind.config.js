/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../templates/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        'black': {
          400: '#404040',
          500: '#1C2444'
        },
        'whitish': {
          100: '#F2F3FB'
        }
      }
    },
  },
  plugins: [],
}
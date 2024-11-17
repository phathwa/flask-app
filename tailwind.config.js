/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        'custom-yellow': '#ffcc00', // Replace with your desired shade of yellow
        'cus-clr-primary': "#ffcc00", // Primary color of the website
        'cus-clr-secondary': "#000055" // Secondary color of the website
      },
      fontFamily: {
        oswald: ['Oswald', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

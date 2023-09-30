/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
         'main': "'Nunito Sans', sans-serif",
         'logo1': "'Pacifico', cursive",
         'logo2': "'Courgette', cursive"
      },
      boxShadow: {
         'around': '0 -5px 30px 5px rgba(0,0,0,0.3)',
         'shining-red': '0 -5px 30px 5px rgba(200,40,40,0.5)',
         'shining-red-small': '0 0 15px 2px rgba(200,40,40,0.5)',
         'down-red': '0 15px 30px -5px rgba(200,40,40,0.62)',
         'book-div': '0 0 6px -1px rgba(0,0,0,0.3)'
      },
      screens: {
         'semi-lg': '880px'
      },
      animation: {
         'flash-pop-up': 'flash-pop-up 8s'
      },
      keyframes: {
         'flash-pop-up': {
            '0%, 100%': {transform: 'translateY(200%)'},
            '20%, 80%': {transform: 'translateY(0)'}
         }
      }
    },
  },
  plugins: [],
}


function toggleSelectInput(selectPlaceholder, selectDiv, options, input, data_used)
{
   selectPlaceholder.click(function()
   {
      if(selectDiv.hasClass('-translate-y-4'))
      {
         selectDiv.removeClass('hidden')
         setTimeout(() => {
            selectDiv.toggleClass('-translate-y-4 translate-y-1 opacity-0')
         })
      } else {
         selectDiv.toggleClass('-translate-y-4 translate-y-1 opacity-0')
         setTimeout(() => {
            selectDiv.addClass('hidden')
         }, 300)
      }
   })
   options.click(function()
   {
      input.val( $(this).data(data_used) )
      selectPlaceholder.html( $(this).html() )
      
      selectDiv.toggleClass('-translate-y-4 translate-y-1 opacity-0')
      setTimeout(() => {
         selectDiv.addClass('hidden')
      }, 300)
   })
}

$(document).ready(function()
{
   $('.add_to_cart_button').each(function(index)
   {
      const book_index = index
      $(this).click(function()
      {
         const book_id = $(this).data('book-id')
         const add_to_cart_button = $(this)
         $('#cart_list_wrapper').load('/library/book/add-to-cart/' + book_id, function()
         {
            add_to_cart_button.toggleClass('hover:bg-green-500 hover:text-white text-green-600 text-white bg-green-500')
            $('.add_to_cart_button img').eq(book_index).toggleClass('filter-to-green filter-to-white')
         })
      })
   })
})
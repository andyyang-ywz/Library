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
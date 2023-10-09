$(document).ready(function()
{
   $('button#toggle_other_image').click(function()
   {
      let current_picture = $('.book_picture:not(.hidden)')
      let current_index = parseInt(current_picture.data('image-counter'))
      let total_pictures = $('.book_picture').length

      current_picture.addClass('hidden')
      let new_index = current_index + 1
      if(new_index > total_pictures)
      {
         new_index = 1
      }
      $('.book_picture').eq(new_index-1).removeClass('hidden')

   })







   $('#shipping_wrapper').click(function()
   {
      $('#shipping_options').toggleClass('hidden')
   })
   $('#shipping_options option').click(function()
   { 
      $('input[name=shipment_method]').val( $(this).attr('value') )
      $('#shipping_selected').html( $(this).html() )
   })


   $('#purchase_button').click(function()
   {
      $('#payment_method_wrapper').toggleClass('hidden flex')
      setTimeout(() => {
         $('#dark_bg').toggleClass('opacity-0 opacity-30')
         setTimeout(() => {
            $('#payment_method_options').removeClass('opacity-0 scale-75')
         }, 150)
      }, 1)
   })

   $('#payment_method_wrapper #dark_bg').click(function()
   {
      $('#payment_method_options').addClass('opacity-0 scale-75')
      $('#dark_bg').toggleClass('opacity-0 opacity-30')
      setTimeout(() => {
         $('#payment_method_wrapper').toggleClass('hidden flex')
      }, 300)
   })

   $('.payment_option').each(function(index)
   {
      $(this).click(function()
      {
         $('.payment_option').each(function(index)
         {
            $(this).addClass('border-neutral-500 hover:bg-[#ebebeb]')
            $(this).removeClass('border-green-500 bg-green-200')
            $('.payment_option .check_icon').eq(index).addClass('hidden')
         })
         $(this).toggleClass('border-neutral-500 hover:bg-[#ebebeb] border-green-500 bg-green-200 ')
         $('.payment_option .check_icon').eq(index).removeClass('hidden')
         $('input[name=payment_method]').val( $(this).data('value') )
      })
   })
})
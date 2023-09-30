$(document).ready(function()
{
   let categorySelect = $('#category_select')
   let categoryP      = $('#category_input_wrapper > div > p')
   let categoryOption = $('#category_select option')
   let categoryInput  = $('input[name=category]')
   toggleSelectInput(categoryP, categorySelect, categoryOption, categoryInput, 'category-id')


   $('.coma-regexed').keyup(function()
   {
      $(this).val( $(this).val().replace(/[^0-9 \.]/, '') )
   })


   function load_size_input()
   {
      let width     = parseInt($('input[id=width]').val())
      let height    = parseInt($('input[id=height]').val())
      let thickness = parseInt($('input[id=thickness]').val())
      if (width > 0 && height > 0 && thickness > 0)
      {
         $('input[id=id_size]').val(width + 'x' + height + 'x' + thickness)
      }
   }
   $('.size-input').change(load_size_input)
   $('.size-input').keyup(load_size_input)



   if($('input[id=id_size]').val() != '')
   {
      let size_arr = $('input[id=id_size]').val().split('x')
      $('input[id=width]').val(size_arr[0])
      $('input[id=height]').val(size_arr[1])
      $('input[id=thickness]').val(size_arr[2])
   }
   if($('input[id=id_category]').val() != '')
   {
      $('#category_select option').each(function()
      {
         if($('input[id=id_category]').val() == $(this).data('category-id'))
         {
            categoryP.html( $(this).html() )
         }
      })
   }

   
})
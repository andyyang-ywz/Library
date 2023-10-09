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



   if($('input[id=id_size]').length > 0)
   {
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
   }




   $('input[id=id_image]').change(function()
   {
      const file = this.files[0]
      if(file)
      {
         const reader = new FileReader()
         reader.onload = function(event)
         {  
            $('#uploaded_image').removeClass('hidden')
            $('#uploaded_image').attr('src', event.target.result)
            $('#upload_image_button_h2').addClass('hidden')
         }
         reader.readAsDataURL(file)
      }
   })


   





   function appendImage(image_uploaded)
   {
      // create image tag
      const plusImg = document.createElement('img')
      $(plusImg).attr('src', '/static/image/icons/plus.png')
      $(plusImg).addClass('w-12 h-12 filter-to-gray2')
      // create input tag
      const newFileInput = document.createElement('input')
      $(newFileInput).attr({
         type : 'file',
         name : 'image' + (image_uploaded+1),
         id   : 'id_image' + (image_uploaded+1),
         class: 'hidden'
      })
      $(newFileInput).change(showPreviewPicture)
      // put it in label tag
      const newFileInputTrigger = document.createElement('label')
      $(newFileInputTrigger).attr('for', 'id_image' + (image_uploaded+1))
      $(newFileInputTrigger).addClass('flex items-center justify-center w-[125px] md:w-[150px] 2xl:w-[175px] aspect-[3_/_4] bg-neutral-700 rounded-md cursor-pointer overflow-hidden')
      $(newFileInputTrigger).append($(plusImg))
      $(newFileInputTrigger).append($(newFileInput))
      // put it in image_list div
      $('#image_list').append($(newFileInputTrigger))

   }
   function showPreviewPicture()
   {
      const file = this.files[0]
      if( file )
      {
         const reader = new FileReader()
         reader.onload = function(event)
         {
            let image_uploaded = $('#image_list label').length
            $('#main_image_preview').removeClass('hidden')
            $('#main_image_preview').attr('src', event.target.result)
            $('label[for=id_image'+ image_uploaded +'] img').attr({
               src: event.target.result,
               class: 'w-full h-full object-cover'
            })
            $('label[for=id_image'+ image_uploaded +']').attr('for', image_uploaded)
            appendImage(image_uploaded)
         }
         reader.readAsDataURL(file)
      }
   }
   $('input[id=id_image1]').change(showPreviewPicture)

   
})
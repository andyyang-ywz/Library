$(document).ready(function()
{
   $('#small_nav_wrapper').css('height', $(window).height() - 64 + 'px')
   $(window).resize(function()
   {
      let window_height = $(window).height()
      $('#small_nav_wrapper').css('height', window_height - 64 + 'px')
   })

   function open_menu_wrapper(menu, menu_button)
   {
      menu_button.hover(function()
      {
         if($('.nav_menu_wrapper.active').length > 0)
         {
            $('.nav_menu_wrapper').each(function()
            {
               $(this).addClass('opacity-0 scale-[0.98]')
               setTimeout(() => {
                  $(this).addClass('md:hidden')
                  $(this).removeClass('md:block')
               }, 300)
            })
            setTimeout(() => {
               menu.removeClass('md:hidden')
               menu.addClass('md:block active')
               setTimeout(() => {
                  menu.removeClass('opacity-0 scale-[0.98]')
               }, 1)
            }, 301)
         } else {
            menu.removeClass('md:hidden')
            menu.addClass('md:block active')
            setTimeout(() => {
               menu.removeClass('opacity-0 scale-[0.98]')
            }, 1)
         }
      }, function()
      {
         let check_interval = setInterval(() => {
            if( !menu_button.is(':hover') && !menu.is(':hover') )
            {
               menu.addClass('opacity-0 scale-[0.98]')
               setTimeout(() => {
                  menu.addClass('md:hidden')
                  menu.removeClass('md:block active')
               }, 300)
               clearInterval(check_interval)
            }
         }, 750)
      })
   }
   open_menu_wrapper($('#category_menu_wrapper'), $('#category_menu_btn'))
   open_menu_wrapper($('#history_menu_wrapper'), $('#history_menu_btn'))
   open_menu_wrapper($('#cart_menu_wrapper'), $('#cart_menu_btn'))

   $('#hamburger_button').click(function()
   {
      if(!$(this).hasClass('active'))
      {  
         $(this).addClass('active')
         $('#hamburger_button span:nth-child(1)').addClass('rotate-45 -translate-y-[3px]')
         $('#hamburger_button span:nth-child(2)').addClass('opacity-0')
         $('#hamburger_button span:nth-child(3)').addClass('-rotate-45 translate-y-[3px]')

         $('#small_nav').toggleClass('hidden block')
         $('#dark_bg').removeClass('hidden')
         setTimeout(() => {
            $('#small_nav').toggleClass('translate-x-full -right-5 right-0')
            $('#dark_bg').toggleClass('opacity-0 opacity-20')
            $('body').addClass('overflow-hidden')
         }, 1)
      } else {
         $(this).removeClass('active')
         $('#hamburger_button span:nth-child(1)').removeClass('rotate-45 -translate-y-[3px]')
         $('#hamburger_button span:nth-child(2)').removeClass('opacity-0')
         $('#hamburger_button span:nth-child(3)').removeClass('-rotate-45 translate-y-[3px]')

         $('#small_nav').toggleClass('translate-x-full -right-5 right-0')
         $('#dark_bg').toggleClass('opacity-0 opacity-20')
         setTimeout(() => {
            $('body').removeClass('overflow-hidden')
         }, 300)
         setTimeout(() => {
            $('#dark_bg').addClass('hidden')
            $('#small_nav').toggleClass('hidden block')
         }, 700)
      }
   })
})
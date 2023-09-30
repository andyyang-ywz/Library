$(document).ready(function()
{
   let divIntro1 = $('#introduction div:nth-child(1)')
   let divIntro2 = $('#introduction div:nth-child(2)')
   let divIntro3 = $('#introduction div:nth-child(3)')

   $(window).scroll(function() {
      if( $(this).scrollTop() > 350 ) 
      { 
         if(divIntro1.hasClass('opacity-0'))
         {
            divIntro1.removeClass('translate-y-[100px] opacity-0')
         }
      } else {
         if(!divIntro1.hasClass('opacity-0'))
         {
            divIntro1.addClass('translate-y-[100px] opacity-0')
         }
      }

      let additional_scroll = 0
      if( $(window).width() <= 626 ) { additional_scroll = 150 }

      if( $(this).scrollTop() > 450 + additional_scroll ) 
      { 
         if(divIntro2.hasClass('opacity-0'))
         {
            divIntro2.toggleClass('translate-y-[35px] semi-lg:translate-y-[70px] lg:translate-y-[100px] translate-y-[135px] semi-lg:translate-y-[170px] lg:translate-y-[200px] opacity-0')
         }
      } else {
         if(!divIntro2.hasClass('opacity-0'))
         {
            divIntro2.toggleClass('translate-y-[35px] semi-lg:translate-y-[70px] lg:translate-y-[100px] translate-y-[135px] semi-lg:translate-y-[170px] lg:translate-y-[200px] opacity-0')
         }
      }

      if( additional_scroll != 0 ) { additional_scroll = 250 }

      if( $(this).scrollTop() > 550 + additional_scroll ) 
      { 
         if(divIntro3.hasClass('opacity-0'))
         {
            divIntro3.toggleClass('translate-y-[169px] semi-lg:translate-y-[240px] lg:translate-y-[300px] translate-y-[69px] semi-lg:translate-y-[140px] lg:translate-y-[200px] opacity-0')
         }
      } else {
         if(!divIntro3.hasClass('opacity-0'))
         {
            divIntro3.toggleClass('translate-y-[169px] semi-lg:translate-y-[240px] lg:translate-y-[300px] translate-y-[69px] semi-lg:translate-y-[140px] lg:translate-y-[200px] opacity-0')
         }
      }

      if( $(window).width() <= 866 ) { additional_scroll = 100 }
      if( $(window).width() <= 626 ) { additional_scroll = 200 }
      if( $(this).scrollTop() > (950 + additional_scroll) )
      {
         $('#motivational_quote > h1').removeClass('opacity-0')
         $('#quotes_wrapper').removeClass('opacity-0 translate-y-[100px]')
         $('#quotes_nav').removeClass('opacity-0')
      } else {
         $('#motivational_quote > h1').addClass('opacity-0')
         $('#quotes_wrapper').addClass('opacity-0 translate-y-[100px]')
         $('#quotes_nav').addClass('opacity-0')
      }
   })

   let quote_slide
   function move_quote_slide(quote_slide)
   {
      $('#quotes_nav button').each(function()
      {
         $(this).removeClass('bg-slate-600')
         $(this).addClass('hover:bg-slate-300')
      })
      $('#quotes_nav button').eq(quote_slide).toggleClass('bg-slate-600 hover:bg-slate-300')
      $('#quotes_wrapper > div').css('transform', 'translateX(-'+ quote_slide * 100 +'%)')
   }
   $('#quotes_nav button').each(function(index)
   {
      $(this).click(function()
      {
         quote_slide = index
         move_quote_slide(quote_slide)
      })
   })
   $(window).resize(function()
   {
      if( $(this).width() + 14 > 880 && (quote_slide + 1) > ($('#quotes_nav button').length / 2) )
      {
         quote_slide = Math.floor(quote_slide / 2)
         move_quote_slide(quote_slide)
      }
   })

   
   

   let genderP      = $('#gender_input_wrapper > div > p')
   let genderSelect = $('#gender_select')
   let genderOption = $('#gender_select option')
   let genderInput  = $('input[name=gender]')
   toggleSelectInput(genderP, genderSelect, genderOption, genderInput, 'gender-type')

   $('input[type=date]').change(function()
   {
      $('input[name=birthday]').val( $(this).val() )
   })
})
$(document).ready(function() {

    /* Button mobile menu */

    $(".hamburger").click(function(e) {
    	$(".main_menu ul").slideToggle();
    	$(".hamburger").toggleClass("is-active");
    	return false;
    });

    /* Moving menu */

    var options = {
    	offset: 400
    };

    var header = new Headhesive('.header_head', options);

     /* Button search */

    $('.opacity').css({opacity: 0.7});

    $(".search_header").click(function(){
    	$(".search_popup").show();
    	$(".close_search").show();
    	$(".opacity").show();
    });

    $(".close_search").click(function(){
    	$(".search_popup").hide();
    	$(".close_search").hide();
    	$(".opacity").hide();
    });

     /* Button up */

    $(window).scroll(function(){
    	if ($(this).scrollTop() > 400) {
    		$('.up_button i').fadeIn();
    	} else {
    		$('.up_button i').fadeOut();
    	}
    });

    $('.up_button i').click(function(){
    	$("html, body").animate({ scrollTop: 0 }, 400);
    	return false;
    });

});
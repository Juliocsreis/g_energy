function checkScroll(){

     $("body").scrollspy({
        target: "#mainNav",
        offset: -74,
    });

    var startY = $('.navbar').height() * 2; //The point where the navbar changes in px
    if($(window).scrollTop() > startY){
        $('.navbar').addClass("scrolled");
    }else{
        $('.navbar').removeClass("scrolled");
    }

}

if($('.navbar').length > 0){
    $(window).on("scroll load resize", function(){
        checkScroll();
    });
}

$('.navbar-nav>li>a').on('click', function(){
    $('.navbar-collapse').collapse('hide');
});


//$('.test, .nav-link, .navbar-brand, .new-button').click(function() {
//    var sectionTo = $(this).attr('href');
//    $('html, body').animate({
//      scrollTop: $(sectionTo).offset().top
//    }, 950);
//});
//
//var scrollSpy = new bootstrap.ScrollSpy(document.body, {
//    target: '#mainNav',
//    offset: 72,
//})
//
//var offset = 120;
//
//$('.navbar li a').click(function(event) {
//    event.preventDefault();
//    $($(this).attr('href'))[0].scrollIntoView();
//    scrollBy(0, -offset);
//});





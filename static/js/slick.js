$(document).ready(function(){
    $('.slider').slick({
        arrows: true,
        adaptiveHeigth: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        easing: 'linear',
        infinite: true,
        initialSlide: 0,
        autoplay: true,
        autoplaySpeed: 2000,
        pauseOnfocus: true,
        centerMode: true,
        vertical: false,   
        asNavFor: ".sliderbig",
        centerMode: true
    })
    $('.sliderbig').slick({
        asNavFor: ".slider",   
        arrows: false,
        fade:true
    })
})
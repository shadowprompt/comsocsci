/*---------------------------------------------
Template name:  Aduca
Version:        1.0
最新最全最好的Bootstrap模板：http://www.bootstrapmb.com

[Table of Content]

01: Preloader
02: side-widget-menu
02: Back to Top Button and Navbar Scrolling control
03: header-category
04: Mobile Menu Open Control
05: Mobile Menu Close Control
06: homepage-slide1
07: course-carousel
08: view-more-carousel
09: Counter up
10: MagnificPopup
10: testimonial-wrap
11: Client logo
12: blog-post-carousel
13: Bootstrap Tooltip
14: FAQs
15: Isotope
16: lightbox
17: Google map
----------------------------------------------*/


(function ($) {
    "use strict"; //use of strict

    /* ======= Preloader ======= */
    $(window).on('load', function(){
        $('.preloader').delay('0').fadeOut(0);
    });


    $(document).on('ready', function () {

        /*====  side-widget-menu  =====*/
        $(document).on('click','.side-menu-wrap .side-menu-ul .sidenav__item .menu-plus-icon', function () {
            $(this).closest('.sidenav__item').siblings().removeClass('active').find('.side-sub-menu').slideUp(200);
            $(this).closest('.sidenav__item').toggleClass('active').find('.side-sub-menu').slideToggle(200);
            return false;
        });

        /* ======= Back to Top Button and Navbar Scrolling control ======= */
        $(document).on('click','#scroll-top', function () {
            $('html').animate({scrollTop:0},1000);
        });

        var scrollButton = $('#scroll-top');

        $(window).on('scroll', function () {
            //header fixed animation and control
            if($(window).scrollTop() > 0) {
                $('.header-menu-area').addClass('header-fixed');
            }else{
                $('.header-menu-area').removeClass('header-fixed');
            }

            //back to top button control
            if($(this).scrollTop()>= 300){
                scrollButton.show();
            }else{
                scrollButton.hide();
            }
        });

        /*====  header-category  =====*/
        $(document).on('click','.header-category ul li .dropdown-menu-item > li', function () {
            $(this).closest('li').siblings().removeClass('active').find('.sub-menu').slideUp(200);
            $(this).closest('li').toggleClass('active').find('.sub-menu').slideToggle(200);
            return false;
        });

        /*=========== Mobile Menu Open Control ============*/
        $(document).on('click','.logo-right-button .side-menu-open', function () {
            $('.side-nav-container').addClass('active');
        });

        /*=========== Mobile Menu Close Control ============*/
        $(document).on('click','.humburger-menu .side-menu-close', function () {
            $(".side-nav-container").removeClass('active');
        });

        /*==== homepage-slide1 =====*/
        $('.homepage-slide1').owlCarousel({
            items: 1,
            nav: true,
            dots: true,
            autoplay: false,
            loop: true,
            smartSpeed: 5000,
            animateOut: 'lightSpeedOut',
            animateIn: 'fadeIn',
            active: true,
            navText: ["<i class='la la-angle-left'></i>", "<i class='la la-angle-right'></i>"],
        });

        $('.homepage-slide1').on('translate.owl.carousel', function(){
            $('.single-slide-item .slider__title, .single-slide-item .slider__text').removeClass('animated fadeInUp').css('opacity', '0');
            $('.single-slide-item .theme-btn, .single-slide-item .video-play-btn').removeClass('animated fadeInDown').css('opacity', '0');
        });

        $('.homepage-slide1').on('translated.owl.carousel', function(){
            $('.single-slide-item .slider__title, .single-slide-item .slider__text').addClass('animated fadeInUp').css('opacity', '1');
            $('.single-slide-item .theme-btn, .single-slide-item .video-play-btn').addClass('animated fadeInDown').css('opacity', '1');
        });

        /*==== course-carousel =====*/
        $('.course-carousel').owlCarousel({
            loop: true,
            items: 3,
            nav: true,
            dots: false,
            smartSpeed: 500,
            autoplay: false,
            margin: 30,
            navText: ["<i class='la la-angle-left'></i>", "<i class='la la-angle-right'></i>"],
            responsive:{
                320:{
                    items:1,
                },
                992:{
                    items:3,
                }
            }
        });

        /*==== view-more-carousel =====*/
        $('.view-more-carousel').owlCarousel({
            loop: true,
            items: 2,
            nav: false,
            dots: true,
            smartSpeed: 500,
            autoplay: false,
            margin: 15,
            responsive:{
                320:{
                    items:1,
                },
                768:{
                    items:2,
                }
            }
        });

        /*=========== Counter up ============*/
        $('.counter').counterUp({
            delay: 20,
            time: 2000
        });

        /*=========== MagnificPopup ============*/
        $('.video-play-btn').magnificPopup({
            type: 'video'
        });

        /*==== testimonial-wrap =====*/
        $('.testimonial-wrap').owlCarousel({
            loop: true,
            items: 5,
            nav: false,
            dots: true,
            smartSpeed: 500,
            autoplay: false,
            margin: 30,
            autoHeight: true,
            responsive:{
                320:{
                    items:1,
                },
                767:{
                    items:2,
                },
                992:{
                    items:3,
                },
                1025:{
                    items:4,
                },
                1440:{
                    items:5,
                }
            }
        });

        /*==== Client logo =====*/
        $('.client-logo').owlCarousel({
            loop: true,
            items: 5,
            nav: false,
            dots: false,
            smartSpeed: 500,
            autoplay: false,
            responsive : {
                // breakpoint from 0 up
                0 : {
                    items: 2
                },
                // breakpoint from 481 up
                481 : {
                    items: 3
                },
                // breakpoint from 768 up
                768: {
                    items: 4
                },
                // breakpoint from 992 up
                992 : {
                    items: 5
                }
            }
        });

        /*==== blog-post-carousel =====*/
        $('.blog-post-carousel').owlCarousel({
            loop: true,
            items: 3,
            nav: false,
            dots: true,
            smartSpeed: 500,
            autoplay: false,
            margin: 30,
            responsive:{
                320:{
                    items:1,
                },
                992:{
                    items:3,
                }
            }
        });

        /*=========== Bootstrap Tooltip ============*/
        $('[data-toggle="tooltip"]').tooltip();

        /*====  FAQ  =====*/
        $(document).on('click', '.faq-heading', function () {
            $(this).closest('.faq-panel').siblings().removeClass('active').find('.faq-content').slideUp(200);
            $(this).closest('.faq-panel').toggleClass('active').find('.faq-content').slideToggle(200);
            return false;
        });

        /*=========== Isotope ============*/

        // bind filter button click
        $(document).on( 'click', '.portfolio-filter li', function() {
            var filterData = $( this ).attr('data-filter');

            // use filterFn if matches value
            $('.portfolio-list').isotope({
                filter: filterData,
            });

            $('.portfolio-filter li').removeClass('active');
            $(this).addClass('active');
        });

        // portfolio list
        $('.portfolio-list').isotope({
            itemSelector: '.single-portfolio-item',
            percentPosition: true,
            masonry: {
                // use outer width of grid-sizer for columnWidth
                columnWidth: '.single-portfolio-item',
                horizontalOrder: true
            }
        });

        /*=========== lightbox ============*/
        lightbox.option({
            'resizeDuration': 200,
            'wrapAround': true,
            positionFromTop: 200
        });


        /*=========== Google map ============*/
        if($("#map").length) {
            initMap('map', 40.717499, -74.044113, 'images/map-marker.png');
        }

    });
})(jQuery);
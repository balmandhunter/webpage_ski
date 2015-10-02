
$(document).ready(function () {

    // SCROLL SCRIPTS
    $('.scroll-me a').bind('click', function (event) { //just pass scroll-me class and start scrolling
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1000, 'easeInOutQuad');
        event.preventDefault();
    });

    $("#date-picker-2").datepicker({ startDate: new Date('2015-11-16'), endDate: new Date('2016-04-27') });

    });

$(document).ready(function() {
    $('.carousel').carousel({
        interval: 3000
    });

    $('.carousel-control-prev').click(function(event) {
        event.preventDefault();
        $('.carousel').carousel('prev');
    });

    $('.carousel-control-next').click(function(event) {
        event.preventDefault();
        $('.carousel').carousel('next');
    });
});
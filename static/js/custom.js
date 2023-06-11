$(document).ready(function() {
    $('form').on('submit', function(event) {
        event.preventDefault();

        var formData = new FormData(this);

        $.ajax({
            url: '',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                $('#success-message').removeClass('d-none');
                setTimeout(function() {
                    $('#success-message').addClass('d-none');
                    location.reload();
                }, 2000);
            }
        });
    });
});

$(document).ready(function() {
    $('#telefon').on('keypress', function(event) {
        if (event.which < 48 || event.which > 57) {
            event.preventDefault();
        }
    });
})

$(document).ready(function() {
    $('#myCarousel').carousel({
        interval: 10000,
    });
});

$('.carousel-control-prev').click(function(event) {
    event.preventDefault(); // Sayfa yenilenmesini engeller
    $('#myCarousel').carousel('prev');
    $('.carousel-indicators li.active').prev().addClass('active');
    $('.carousel-indicators li.active:last').removeClass('active');
});

$('.carousel-control-next').click(function(event) {
    event.preventDefault(); // Sayfa yenilenmesini engeller
    $('#myCarousel').carousel('next');
    $('.carousel-indicators li.active').next().addClass('active');
    $('.carousel-indicators li.active:first').removeClass('active');
});

    
$(document).ready(function() {
    $('form').submit(function(event) {
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
                    $('form')[0].reset();  // Formu sıfırla
                }, 2000);
            }
        });
    });
});




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


 document.getElementById('contact-info-toggle').addEventListener('click', function() {
    var offcanvasElement = document.getElementById('contact-info');
    var offcanvas = new bootstrap.Offcanvas(offcanvasElement);
    offcanvas.show();
    
    // Offcanvas bölmesi kapatıldığında overlay bileşenini temizle
    offcanvasElement.addEventListener('hidden.bs.offcanvas', function() {
        document.body.classList.remove('offcanvas-open');
    });
});



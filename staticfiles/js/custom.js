$(document).ready(function() {
    $('.carousel').carousel({
        interval: 10000
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

document.getElementById('contact-info-toggle').addEventListener('click', function() {
    var offcanvasElement = document.getElementById('contact-info');
    var offcanvas = new bootstrap.Offcanvas(offcanvasElement);
    offcanvas.show();
    
    // Offcanvas bölmesi kapatıldığında overlay bileşenini temizle
    offcanvasElement.addEventListener('hidden.bs.offcanvas', function() {
        document.body.classList.remove('offcanvas-open');
    });
});
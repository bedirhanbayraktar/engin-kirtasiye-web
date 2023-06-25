document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');
    var submitButton = form.querySelector('button[type="submit"]');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        if (form.classList.contains('submitted')) {
            return false;
        }

        form.classList.add('submitted');
        submitButton.disabled = true; // Gönderme düğmesini devre dışı bırak

        const formData = new FormData(form);

        axios.post('', formData)
            .then(function(response) {
                document.querySelector('#success-message').classList.remove('d-none');
                setTimeout(function() {
                    document.querySelector('#success-message').classList.add('d-none');
                    form.reset(); // Formu sıfırla
                    form.classList.remove('submitted');
                    submitButton.disabled = false; // Gönderme düğmesini etkinleştir
                }, 2000);
            })
            .catch(function(error) {
                console.error(error);
                form.classList.remove('submitted');
                submitButton.disabled = false; // Gönderme düğmesini etkinleştir
            });
    });
});







$(document).ready(function() {
    $('#myCarousel').carousel({
        interval: 10000,
    });
});


$(document).ready(function() {
    $('#contact-info-toggle').on('click', function() {
        var offcanvasElement = document.getElementById('contact-info');
        var offcanvas = new bootstrap.Offcanvas(offcanvasElement);
        offcanvas.show();

        // Offcanvas bölmesi kapatıldığında overlay bileşenini temizle
        offcanvasElement.addEventListener('hidden.bs.offcanvas', function() {
            document.body.classList.remove('offcanvas-open');
        });
    });

    $('#myCarousel').carousel({
        interval: 10000
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

    $('.navbar-toggler').click(function() {
        $('.navbar-collapse').slideToggle(300);
        setTimeout(function() {
            test();
        });
    });

    function test() {
        var tabsNewAnim = $('#navbarSupportedContent');
        var selectorNewAnim = $('#navbarSupportedContent').find('li').length;
        var activeItemNewAnim = tabsNewAnim.find('.active');
        var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
        var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
        var itemPosNewAnimTop = activeItemNewAnim.position();
        var itemPosNewAnimLeft = activeItemNewAnim.position();
        $('.hori-selector').css({
            top: itemPosNewAnimTop.top + 'px',
            left: itemPosNewAnimLeft.left + 'px',
            height: activeWidthNewAnimHeight + 'px',
            width: activeWidthNewAnimWidth + 'px'
        });
        $('#navbarSupportedContent').on('click', 'li', function(e) {
            $('#navbarSupportedContent ul li').removeClass('active');
            $(this).addClass('active');
            var activeWidthNewAnimHeight = $(this).innerHeight();
            var activeWidthNewAnimWidth = $(this).innerWidth();
            var itemPosNewAnimTop = $(this).position();
            var itemPosNewAnimLeft = $(this).position();
            $('.hori-selector').css({
                top: itemPosNewAnimTop.top + 'px',
                left: itemPosNewAnimLeft.left + 'px',
                height: activeWidthNewAnimHeight + 'px',
                width: activeWidthNewAnimWidth + 'px'
            });
        });
    }

    setTimeout(function() {
        test();
    });

    $(window).on('resize', function() {
        setTimeout(function() {
            test();
        }, 500);
    });

    // Sayfaya eklenen kodlar
    var path = window.location.pathname.split("/").pop();
    if (path === '') {
        path = 'index.html';
    }
    var target = $('#navbarSupportedContent ul li a[href="' + path + '"]');
    target.parent().addClass('active');
});


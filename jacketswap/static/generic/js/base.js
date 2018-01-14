var imageZoom = $('.image-zoom');

$(document).ready(
    $('.hamburger').click(function() {
        $('.mobile-navigation').toggle();
    })
);

$('.jacket-details .image').click(function() {
    console.log('click');
    imageZoom.show();
});

imageZoom.click(function() {
    imageZoom.hide();
});
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

$('body').click(function(event) {
    if(event.target.id === 'user-navigation') {
        console.log(event.target.id);
        $('.user-menu').toggle();
    } else {
        $('.user-menu').hide();
    }
});

$('.button-secondary.returned').hover(function() {
    $(this).html("Undo");
}, function() {
    $(this).html("Returned!")
});
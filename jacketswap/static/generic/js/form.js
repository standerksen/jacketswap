$(".file-input").change(function(){
    if($(this).val() && $(this).val() !== "") {
        var filename = $(this).val();
    }
    $(".select-file-string").html("Selected file:");
    $(".selected-file").html(filename);
});

var lostFoundLeft = $("#id_lost_found_0").closest("li");
var lostFoundRight = $("#id_lost_found_1").closest("li");

$(document).ready(function() {
    lostFoundLeft.addClass("active");
});

lostFoundLeft.click(function() {
    lostFoundRight.removeClass("active");
    lostFoundLeft.addClass("active");
});

lostFoundRight.click(function() {
    lostFoundLeft.removeClass("active");
    lostFoundRight.addClass("active");
});
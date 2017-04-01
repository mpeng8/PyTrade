var moveLeft = 0;
var moveDown = 0;
$('.popper').hover(function (e) {
    var target = '#' + ($(this).attr('data-popbox'));
    $(target).show();
    moveLeft = $(this).outerWidth();
    moveDown = ($(target).outerHeight() / 2);
}, function () {
    var target = '#' + ($(this).attr('data-popbox'));
    if (!($(".popper").hasClass("show"))) {
        $(target).hide();
    }
});


$('.popper').click(function (e) {
    var target = '#' + ($(this).attr('data-popbox'));
    if (!($(this).hasClass("show"))) {
        $(target).show();
    }
    $(this).toggleClass("show");
});

$('.openP_popper').hover(function (e) {

    var target = '#' + ($(this).attr('data-popbox'));
    $(target).show();
    moveLeft = $(this).outerWidth();
    moveDown = ($(target).outerHeight() / 2);
}, function () {
    var target = '#' + ($(this).attr('data-popbox'));
    if (!($(".openP_popper").hasClass("show"))) {
        $(target).hide();
    }
});


$('.openP_popper').click(function (e) {
    var target = '#' + ($(this).attr('data-popbox'));
    if (!($(this).hasClass("show"))) {
        $(target).show();
    }
    $(this).toggleClass("show");
});


$('.volumeP_popper').hover(function (e) {
    var target = '#' + ($(this).attr('data-popbox'));
    $(target).show();
    moveLeft = $(this).outerWidth();
    moveDown = ($(target).outerHeight() / 2);
}, function () {
    var target = '#' + ($(this).attr('data-popbox'));
    if (!($(".volumeP_popper").hasClass("show"))) {
        $(target).hide();
    }
});

$('.volumeP_popper').click(function (e) {
    var target = '#' + ($(this).attr('data-popbox'));
    if (!($(this).hasClass("show"))) {
        $(target).show();
    }
    $(this).toggleClass("show");
});

$('.avgVolumeP_popper').hover(function (e) {
    var target = '#' + ($(this).attr('data-popbox'));
    $(target).show();
    moveLeft = $(this).outerWidth();
    moveDown = ($(target).outerHeight() / 2);
}, function () {
    var target = '#' + ($(this).attr('data-popbox'));
    if (!($(".avgVolumeP_popper").hasClass("show"))) {
        $(target).hide();
    }
});

$('.avgVolumeP_popper').click(function (e) {
    var target = '#' + ($(this).attr('data-popbox'));
    if (!($(this).hasClass("show"))) {
        $(target).show();
    }
    $(this).toggleClass("show");
});

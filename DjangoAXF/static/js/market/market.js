$(function () {
    $('#alltypes').click(function () {
        $('#alltype').toggle();
        $(this).children().children().toggleClass("glyphicon glyphicon-menu-down glyphicon glyphicon-menu-up");
    });
    $('#orderbys').click(function () {
        $('#orderby').toggle();
        $(this).children().children().toggleClass("glyphicon glyphicon-menu-down glyphicon glyphicon-menu-up");
    })
})
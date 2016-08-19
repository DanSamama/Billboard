$('document').ready(function(){
    $('.form').hide();
    $('.submit_button').hide();

    $("#plus_button").click(function(){
    $('.plus_square').hide()
    $('.form').show()
        $('.submit_button').show();
});

});
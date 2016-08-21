$('document').ready(function(){
    $('.form').hide();
    $('.submit_button').hide();

    $("#plus_button").click(function(){
    $('.plus_square').hide();
    $('.form').show();
        $('.submit_button').show();
        });
    $(".button_check_red") .click(function(){
       $('.form').hide();
       $('.submit_button').hide();
       $('.plus_square').show();
        $('#main_form').trigger("reset");
});

});
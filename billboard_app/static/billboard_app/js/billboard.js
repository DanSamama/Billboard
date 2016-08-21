$('document').ready(function(){
    $('.form').hide();
    $('.submit_button').hide();

    $("#plus_button").click(function(){
       var now = new Date($.now());
        var time = (now.getMonth()+1) + '/' + now.getDate() + '/' + now.getFullYear();
        $('#form_publication').text(time);
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
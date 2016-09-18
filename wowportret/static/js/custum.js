jQuery(function(f){
    var element = f('#mainNav');
    f(window).scroll(function(){
        element['fade'+ (f(this).scrollTop() > 200 ? 'In': 'Out')](500);           
    });
});

$( "#callback_a" ).click(function() {
  $( '#id_content' ).css('display','none');
});

$( "#callback" ).click(function() {
    var textarea_input = $('#id_content').parent();
    $(textarea_input).css('display','none')
});

$( "#callback" ).click(function() {
    var email_input = $('#id_contact_email').parent();
    $(email_input).css('display','none')
});

$( "#callback" ).click(function() {
    var file_input = $('#id_docfile').parent();
    $(file_input).css('display','none')
});
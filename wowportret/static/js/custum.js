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

jQuery(function(f){
	// Back to top
	$('#back-to-top').on('click', function(){
		$("html, body").animate({scrollTop: 0}, 500);
		return false;
	});
    $(window).load(function(){
        // hide button to top if the document height not greater than window height*2;using window load for more accurate calculate.    
        if ((parseInt($(window).height())*2)>(parseInt($(document).height()))) {
            $('#back-to-top').hide();
        } 
    });
});
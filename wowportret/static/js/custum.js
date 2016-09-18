jQuery(function(f){
    var element = f('#mainNav');
    f(window).scroll(function(){
        element['fade'+ (f(this).scrollTop() > 200 ? 'In': 'Out')](500);           
    });
});

$( "#callback" ).click(function() {
  $( '#id_content' ).css('display','none');
});


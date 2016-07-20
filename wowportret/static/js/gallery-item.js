$(document).ready(function() {

    $('input[name=material_type]').change(function() {
        val = $(this).val();
        if (val == 'paper') {
            $('#total-border').hide();
            $('#canvas-box').hide();
            $('#fst_block').hide();
            $('#paper-box').show();
        }
        if (val == 'canvas') {
            $('#paper-box').hide();
            $('#fst_block').show();
            $('#canvas-box').show();
            $('#total-border').show();
        }
    });

    function calculate_total_price() {
        if ($("#canvas_radio").prop("checked")) {
            //1. Get input size
            var main_size = parseInt($('#main_size').val());
            //2. get all checkboxes
            var lac_price = parseInt(0);
            if ($("#lac_check").prop("checked")) {
                lac_price = parseInt($("#lac_check").val());
            }
            var gel_price = parseInt(0);
            if ($("#gel_check").prop("checked")) {
                gel_price = parseInt($("#gel_check").val());
            }
            //3. get selected radio
            var baget_price = parseInt($('input[name=optionsRadios]:checked').val());

            //4. Total_price
            var total_price = parseInt(main_size + lac_price + gel_price + baget_price);
        }

        if ($("#paper_radio").prop("checked")) {
            var paper_size = parseInt($('#paper_size').val());
            var total_price = parseInt(paper_size);
        }
        $("#total_price").text(total_price);
    }

    function change_price_by_main_size() {

        var main_size = $('#main_size').val();

        if (main_size == 1490) {
            $(':input[id="lac_check"]').attr('value', '1500'); //maslo
            $(':input[id="gel_check"]').attr('value', '500'); //propis
        }
        if (main_size == 2490) {
            $(':input[id="lac_check"]').attr('value', '3000'); //maslo
            $(':input[id="gel_check"]').attr('value', '1000'); //propis
        }
        if (main_size == 3490) {
            $(':input[id="lac_check"]').attr('value', '6000'); //maslo
            $(':input[id="gel_check"]').attr('value', '2000'); //propis

        }
        if (main_size == 4390) {
            $(':input[id="lac_check"]').attr('value', '9000'); //maslo
            $(':input[id="gel_check"]').attr('value', '4000'); //propis

        }
        if (main_size == 6990) {
            $(':input[id="lac_check"]').attr('value', '15000'); //maslo
            $(':input[id="gel_check"]').attr('value', '6000'); //propis

        }
        if (main_size == 7990) {
            $(':input[id="lac_check"]').attr('value', '18000'); //maslo
            $(':input[id="gel_check"]').attr('value', '7000'); //propis

        }
    };

    function change_price_by_module_option() {
        var mod_val = $('#mod_size').val();
        if (mod_val == 0) {
            change_price_by_main_size();
        }

        if (mod_val == 3800) {
            $(':input[id="lac_check"]').attr('value', '5820'); //maslo
            $(':input[id="gel_check"]').attr('value', '12070'); //propis
        }
        if (mod_val == 5900) {
            $(':input[id="lac_check"]').attr('value', '8450'); //maslo
            $(':input[id="gel_check"]').attr('value', '18390'); //propis

        }
        if (mod_val == 8590) {
            $(':input[id="lac_check"]').attr('value', '14990'); //maslo
            $(':input[id="gel_check"]').attr('value', '30990'); //propis

        }
        if (mod_val == 11990) {
            $(':input[id="lac_check"]').attr('value', '19490'); //maslo
            $(':input[id="gel_check"]').attr('value', '38490'); //propis

        }
        if (mod_val == 12900) {
            $(':input[id="lac_check"]').attr('value', '22900'); //maslo
            $(':input[id="gel_check"]').attr('value', '44500'); //propis

        }
        if (mod_val == 13990) {
            $(':input[id="lac_check"]').attr('value', '25870'); //maslo
            $(':input[id="gel_check"]').attr('value', '54870'); //propis

        }
    };

    $(':radio[baget-type="66"]').attr('value', '890'); //cat A
    $(':radio[baget-type="67"]').attr('value', '1700'); //cat B
    $(':radio[baget-type="68"]').attr('value', '2800'); //cat C
    $(':input[id="lac_check"]').attr('value', '1500'); //maslo
    $(':input[id="gel_check"]').attr('value', '500'); //propis
    // $(':input[id="mod_check"]').attr('value', '0'); //mod

    // $('#mod_size').on('change', function() {
    //     change_price_by_module_option();
    // });

    $('#main_size').on('change', function() {
        if (this.value == 1490) { //30x40
            $(':radio[baget-type="66"]').attr('value', '890'); //cat A
            $(':radio[baget-type="67"]').attr('value', '1700'); //cat B
            $(':radio[baget-type="68"]').attr('value', '2800'); //cat C
            change_price_by_main_size();
        }
        if (this.value == 2490) { //40x60
            $(':radio[baget-type="66"]').attr('value', '1040'); //cat A
            $(':radio[baget-type="67"]').attr('value', '1900'); //cat B
            $(':radio[baget-type="68"]').attr('value', '3000'); //cat C
            change_price_by_main_size();
        }
        if (this.value == 3490) { //50x70
            $(':radio[baget-type="66"]').attr('value', '1320'); //cat A
            $(':radio[baget-type="67"]').attr('value', '2200'); //cat B
            $(':radio[baget-type="68"]').attr('value', '3500'); //cat C
            change_price_by_main_size();
        }
        if (this.value == 4390) { //60x80
            $(':radio[baget-type="66"]').attr('value', '1630'); //cat A
            $(':radio[baget-type="67"]').attr('value', '2600'); //cat B
            $(':radio[baget-type="68"]').attr('value', '4300'); //cat C
            change_price_by_main_size();
        }
        if (this.value == 6990) { //75x105
            $(':radio[baget-type="66"]').attr('value', '1200'); //cat A
            $(':radio[baget-type="67"]').attr('value', '2400'); //cat B
            $(':radio[baget-type="68"]').attr('value', '4600'); //cat C
            change_price_by_main_size();
        }
        if (this.value == 7990) { //90x110
            $(':radio[baget-type="66"]').attr('value', '1300'); //cat A
            $(':radio[baget-type="67"]').attr('value', '2600'); //cat B
            $(':radio[baget-type="68"]').attr('value', '4600'); //cat C
            change_price_by_main_size();
        }
        calculate_total_price();
    });
    $(':input').on('change', function() {
        calculate_total_price();
    });


    var lastClicked_border = 0;
    $('#fst_block :input').on('change', function() {
        // $('.tmp').hide();
        if (lastClicked_border != 0) { //hide last clicked element
            $('#' + lastClicked_border).hide();
        }
        var selected_radio = $('input[name=optionsRadios]:checked');
        var id = $(selected_radio).data('border');
        $('#' + id).show();
        /*
        1. Get $('#' + id) src url
        2. Add on click css properties:
            border-style: solid;
            border-width: 27px 27px 27px 27px;
            -moz-border-image: url(big1.jpg) 27 27 27 27 repeat;
            -webkit-border-image: url(big1.jpg) 27 27 27 27 repeat;
            -o-border-image: url(big1.jpg) 27 27 27 29 repeat;
            border-image: url(/static/img/borders/C7/big2.jpg) 27 27 27 27 fill repeat;
        */
        lastClicked_border = id;
    });


    var lastClicked_border_img = 0;
    $(".border-mini-img").click(function(event) {
        $('.tmp').hide();
        var img_id = $(this).attr('id');
        if (lastClicked_border_img != 0) { //hide last clicked element
            $('#border' + lastClicked_border_img).hide();
            $('#' + lastClicked_border_img).find('img').attr('class', '');
        }
        $('#border' + img_id).show();
        $(this).find('img').attr('class', 'baget-active');
        lastClicked_border_img = img_id;
    });


    $(".fancybox-thumb").fancybox({
        prevEffect: 'none',
        nextEffect: 'none',
        helpers: {
            title: {
                type: 'outside'
            },
            thumbs: {
                width: 50,
                height: 50
            }
        }
    });
    $(".fancybox").fancybox({
        openEffect: 'elastic',
        closeEffect: 'elastic'
    });

    $(".checkbox").click(function(event) {
        var hidden_block = $(this).find('.collapse');

        if (event.target.nodeName == "U") { //if clicked on MORE
            if (hidden_block.css('display') == 'none') {
                hidden_block.show('500');
            } else {
                hidden_block.hide('500');
            }
        }

    });
    $('#fst_block :input[type=checkbox]').click(function(event) {
        $('#fst_block').find('.collapse').collapse('toggle');
        // var hidden_block = $(this).find('.collapse');
        // if (hidden_block.css('display') == 'none') {
        //     hidden_block.show('500');
        // } else {
        //     hidden_block.hide('500');
        // }
    });

    // $(window).scroll(function(event) {
    //     var windowTop = $(this).scrollTop();
    //     if (windowTop <= $("#canvas-box").height()) {
    //         $("div#price_line").addClass("fixed");
    //     } else {
    //         $("div#price_line").removeClass("fixed");
    //     }
    // });


});

$(document).ready(function() {
    var c = document.getElementById("myCanvas");
    var img = document.getElementById("img-for-canvas");
    var ctx = c.getContext("2d");
    var width = 0;
    var height = 0;
    var offset = 0;
    ctx.strokeStyle = "#333";
    ctx.fillStyle = "#333";
    //ctx.globalAlpha = 0.8;

    window.onload = function() {
        c.width = img.width;
        c.height = img.height;
        width = c.width;
        height = c.height;
        offset = width / 15;
        ctx.lineWidth = offset / 2;
        createImage();
        ctx.shadowColor = 'white';
        ctx.shadowBlur = 3;
        ctx.shadowOffsetX = 1;
        ctx.shadowOffsetY = 1;
    }

    function createImage() {
        ctx.imageSmoothingEnabled = false;
        ctx.drawImage(img, 4, 4);
    }



    function drawHorizonRectangle(sprt_by) {

        var start_point = 0;
        var cnt = 0;
        while (cnt < sprt_by) {
            ctx.strokeRect(start_point, 0, width / sprt_by, height);
            start_point += width / sprt_by;
            cnt++;
        }
    }

    function drawVerticalRectangle(sprt_by) {
        var start_point = 0;
        var cnt = 0;
        while (cnt < sprt_by) {
            ctx.strokeRect(0, start_point, width, height / sprt_by);
            start_point += height / sprt_by;
            cnt++;
        }
    }

    function drawGrid(from_x, from_y, cell_x, cell_y, to_x, to_y) {
        var cell_width = (to_x - from_x) / cell_x;
        var cell_height = (to_y - from_y) / cell_y;

        for (var i = from_x; i < to_x; i += cell_width) {
            for (var j = from_y; j < to_y; j += cell_height) {
                ctx.strokeRect(i, j, cell_width, cell_height);
            }
        }
    }

    function drawCustomGrid(type) {
        if (type == 0) {
            ctx.strokeRect(0, 0, width / 2, height);
            drawGrid(width / 2, 0, 4, 2);
        }

        if (type == 1) {
            ctx.strokeRect(0, 0, width / 5, height); //left part
            drawGrid(width / 5, 0, 1, 3, width - width / 5, height);
            ctx.strokeRect(width - width / 5, 0, width / 5, height); //right part
        }
        if (type == 2) {
            drawGrid(0, 0, 1, 3, width - width / 5, height);
            ctx.strokeRect(width - width / 5, 0, width / 5, height); //right part
        }
        if (type == 3) {
            ctx.strokeRect(0, 0, width / 5, height); //left part
            ctx.strokeRect(width / 5, 0, width - width / 5, height / 3); //top part
            ctx.strokeRect(width - width / 5, height / 3, width / 5, height - height / 3); //right part
            ctx.strokeRect(width / 5, height / 3, width - width / 5, height - height / 3); //bottom part
        }
        if (type == 4) {
            ctx.strokeRect(0, 0, width / 5, height); //left part
            ctx.strokeRect(width - width / 5, 0, width / 5, height); //right part
            drawGrid(width / 5, 0, 1, 1, width - width / 5, height / 3); //top
            ctx.strokeRect(width / 5, height / 3, width - 2 * width / 5, height - height / 3); //bottom
        }
        if (type == 5) {
            ctx.strokeRect(0, 0, width / 5, height); //left part
            ctx.strokeRect(width - width / 5, 0, width / 5, height); //right part
            drawGrid(width / 5, 0, 1, 1, width - width / 5, height / 3); //top
            drawGrid(width / 5, height / 3, 2, 1, width - width / 5, height); //bottom

        }
        if (type == 6) {
            ctx.strokeRect(0, 0, width / 2, height - height / 3);
            ctx.strokeRect(0, height - height / 3, width, height / 3);
            drawGrid(width / 2, 0, 3, 1, width, height - height / 3);
        }

        if (type == 7) {
            drawGrid(0, 0, 4, 1, width, height - height / 2.7);
            ctx.strokeRect(0, height - height / 2.7, width, height / 2.7);
        }
        if (type == 8) {
            ctx.strokeRect(0, 0, width, height / 4);
            drawGrid(0, height / 4, 3, 1, width, height - height / 4);
            ctx.strokeRect(0, height - height / 4, width, height / 4);
        }

        if (type == 9) {
            ctx.strokeRect(0, 0, width - width / 3, height);
            drawGrid(width - width / 3, 0, 1, 3, width, height);
        }

        if (type == 10) {
            ctx.strokeRect(width - width / 3, 0, width / 3, height / 2);
            ctx.fillRect(0, 0, width / 3, height / 2);
            ctx.strokeRect(width / 3, 0, width / 3, height);
            ctx.strokeRect(0, height - height / 2, width / 3, height / 2);
            ctx.fillRect(width - width / 3, height / 2, width / 3, height / 2);
        }
        if (type == 11) {
            drawGrid(0, 0, 1, 2, width / 3, height);
            ctx.strokeRect(width / 3, 0, width / 3, height);
            drawGrid(width - width / 3, 0, 1, 2, width, height);
        }
        if (type == 12) {
            ctx.strokeRect(width / 3, 0, width / 3, height);
        }
    }



    $('#test_button').click(function() {
        var k = 0;
        while (k < 7) {
            drawCustomGrid(5);
            k++;
        }
    });
    $('#clear_button').click(function() {
        ctx.clearRect(0, 0, c.width, c.height);
        createImage();
    });
});

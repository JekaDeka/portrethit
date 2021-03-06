$(document).ready(function() {
    var c = document.getElementById("myCanvas");
    var img = document.getElementById("img-for-canvas");
    var ctx = c.getContext("2d");
    var width = 0;
    var height = 0;
    var offset = 0;
    // ctx.globalAlpha = 0.8;

    window.onload = function() {
        offset = img.width / 60;
        ctx.lineWidth = offset / 4;

        c.width = img.width + offset;
        c.height = img.height + offset;
        width = c.width;
        height = c.height;

        createImage();

        ctx.fillStyle = 'white';

        ctx.shadowColor = '#212121';
        ctx.shadowBlur = 8;
        ctx.shadowOffsetX = 5;
        ctx.shadowOffsetY = 5;

        drawFigureByClickedName(1);

    }

    function createImage() {
        ctx.imageSmoothingEnabled = false;
        ctx.drawImage(img, 4, 4);
    }


    function drawGrid(from_x, from_y, cell_x, cell_y, to_x, to_y) {
        var cell_width = (to_x - from_x) / cell_x - offset;
        var cell_height = (to_y - from_y) / cell_y - offset;

        for (var i = from_x; i < to_x; i += (cell_width + offset)) {
            for (var j = from_y; j < to_y; j += (cell_height + offset)) {
                ctx.drawImage(img, i, j, cell_width + offset, cell_height + offset, i, j, cell_width, cell_height);
            }
        }
    }

    function drawCustomGrid(type) {
        if (type == 1) {
            drawGrid(0, 0, 1, 1, width / 2, height);
            drawGrid(width / 2, 0, 2, 2, width, height);
        }

        if (type == 2) {
            drawGrid(0, 0, 1, 1, width / 5, height);
            drawGrid(width / 5, 0, 1, 3, width - width / 5, height);
            drawGrid(width - width / 5, 0, 1, 1, width, height);
        }
        if (type == 3) {
            drawGrid(0, 0, 1, 3, width - width / 5, height);
            drawGrid(width - width / 5, 0, 1, 1, width, height);
        }
        if (type == 4) {
            drawGrid(0, 0, 1, 1, width / 5, height);
            drawGrid(width / 5, 0, 1, 1, width, height / 3); //top
            drawGrid(width / 5, height / 3, 1, 1, width - width / 5, height); //bottom
            drawGrid(width - width / 5, height / 3, 1, 1, width, height);
        }
        if (type == 5) {
            drawGrid(0, 0, 1, 1, width / 5, height);
            drawGrid(width / 5, 0, 1, 1, width - width / 5, height / 3); //top
            drawGrid(width / 5, height / 3, 1, 1, width - width / 5, height); //bottom
            drawGrid(width - width / 5, 0, 1, 1, width, height);

        }
        if (type == 6) {
            drawGrid(0, 0, 1, 1, width / 5, height);
            drawGrid(width / 5, 0, 1, 1, width - width / 5, height / 3); //top
            drawGrid(width / 5, height / 3, 2, 1, width - width / 5, height); //bottom
            drawGrid(width - width / 5, 0, 1, 1, width, height);

        }
        if (type == 7) {
            drawGrid(0, 0, 1, 1, width / 2, height - height / 3);
            drawGrid(0, height - height / 3, 1, 1, width, height);
            drawGrid(width / 2, 0, 3, 1, width, height - height / 3);
        }

        if (type == 8) {
            drawGrid(0, 0, 4, 1, width, height - height / 2.7);
            drawGrid(0, height - height / 2.7, 1, 1, width, height);
        }
        if (type == 9) {
            drawGrid(0, 0, 1, 1, width, height / 4);
            drawGrid(0, height / 4, 3, 1, width, height - height / 4);
            drawGrid(0, height - height / 4, 1, 1, width, height);
        }

        if (type == 10) {
            drawGrid(0, 0, 1, 1, width - width / 3, height);
            drawGrid(width - width / 3, 0, 1, 3, width, height);
        }

        if (type == 11) {
            drawGrid(0, height - height / 3, 1, 1, width / 3, height);
            drawGrid(width / 3, 0, 1, 1, width - width / 3, height);
            drawGrid(width - width / 3, 0, 1, 1, width, height / 3);
        }
        if (type == 12) {
            drawGrid(0, 0, 1, 2, width / 3, height);
            drawGrid(width / 3, 0, 1, 1, width - width / 3, height);
            drawGrid(width - width / 3, 0, 1, 2, width, height);
        }
        if (type == 13) {
            ctx.strokeRect(width / 3, 0, width / 3, height);
        }
    }

    function drawFigureByClickedName(target) {
        ctx.clearRect(0, 0, c.width, c.height);
        //createImage();
        if (target == 23) {
            drawGrid(0, 0, 3, 3, width, height);
        }
        if (target == 22) {
            drawGrid(0, 0, 2, 3, c.width, c.height);
        }
        if (target == 21) {
            drawGrid(0, 0, 3, 2, c.width, c.height);
        }
        if (target == 20) {
            drawGrid(0, 0, 2, 2, c.width, c.height);
        }
        if (target == 19) {
            drawGrid(0, 0, 1, 4, c.width, c.height);
        }
        if (target == 18) {
            drawGrid(0, 0, 1, 3, c.width, c.height);
        }
        if (target == 17) {
            drawGrid(0, 0, 1, 2, c.width, c.height);
        }
        if (target == 16) {
            drawGrid(0, 0, 5, 1, c.width, c.height);
        }
        if (target == 15) {
            drawGrid(0, 0, 4, 1, c.width, c.height);
        }
        if (target == 14) {
            drawGrid(0, 0, 3, 1, c.width, c.height);
        }
        if (target == 13) {
            drawGrid(0, 0, 2, 1, c.width, c.height);
        }
        if (target == 12) {
            drawCustomGrid(target);
        }
        if (target == 11) {
            drawCustomGrid(target);
        }
        if (target == 10) {
            drawCustomGrid(target);
        }
        if (target == 9) {
            drawCustomGrid(target);
        }
        if (target == 8) {
            drawCustomGrid(target);
        }
        if (target == 7) {
            drawCustomGrid(target);
        }
        if (target == 6) {
            drawCustomGrid(target);
        }
        if (target == 5) {
            drawCustomGrid(target);
        }
        if (target == 4) {
            drawCustomGrid(target);
        }
        if (target == 3) {
            drawCustomGrid(target);
        }
        if (target == 2) {
            drawCustomGrid(target);
        }
        if (target == 1) {
            drawCustomGrid(target);
        }
    }


    $('.drinkcard-cc').click(function(event) {
        var target = event.target.className;
        target = target.split('-')[2];
        drawFigureByClickedName(target);
    });

});

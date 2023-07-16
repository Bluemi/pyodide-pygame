function componentToHex(c) {
    let hex = c.toString(16);
    return hex.length === 1 ? "0" + hex : hex;
}

function rgbToHex(color) {
    return "#" + componentToHex(color.r) + componentToHex(color.g) + componentToHex(color.b);
}

function getCanvasMousePos(canvas, evt) {
    let rect = canvas.getBoundingClientRect();
    return [Math.floor(evt.clientX - rect.left), Math.floor(evt.clientY - rect.top)];
}

async function createPygameHelper(pyodide, micropip, canvas) {
    // install pyodide-pygame dropin
    await micropip.install("wheels/pygame-0.1.0-py3-none-any.whl")
    const pygameHelper = {
        display: {
            set_mode: function (screen_size) {
                // get canvas
                canvas.width = screen_size[0];
                canvas.height = screen_size[1];
                // create screen object
                return canvas
            },
            fill: function(canvas, color) {
                const ctx = canvas.getContext("2d");
                ctx.rect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = rgbToHex(color);
                ctx.fill();
            }
        },
        draw: {
            line: function (canvas, color, start, dest) {
                const ctx = canvas.getContext("2d");
                ctx.beginPath();
                ctx.strokeStyle = rgbToHex(color);
                ctx.moveTo(start[0], start[1]);
                ctx.lineTo(dest[0], dest[1]);
                ctx.stroke();
                ctx.strokeStyle = '#000000';
            }
        },
    };
    pyodide.registerJsModule("pygame_helper", pygameHelper);

    // import pygame
    pyodide.runPython("import pygame");

    // handle events
    canvas.addEventListener('click', function(evt) {
        let mousePos = getCanvasMousePos(canvas, evt);
        let locals = new Map();
        locals.set('mouse_position', pyodide.toPy(mousePos));
        pyodide.runPython(
            "pygame.event.handle_event(pygame.event.Event.create_click(mouse_position))",
            {locals: locals}
        );
    });

    canvas.addEventListener('mousemove', function(evt) {
        let mousePos = getCanvasMousePos(canvas, evt);
        let locals = new Map();
        locals.set('mouse_position', pyodide.toPy(mousePos));
        pyodide.runPython(
            "pygame.event.handle_event(pygame.event.Event.create_mousemotion(mouse_position))",
            {locals: locals}
        );
    }, false);

}

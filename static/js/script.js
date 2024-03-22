function confirmDelete() {
    if (confirm('Are you sure you want to delete this project?')) {
        document.getElementById('delete-form').submit();
    }
}

const tweentop = KUTE.fromTo(
    '#wave-top-1',
    { path: '#wave-top-1' },
    { path: '#wave-top-2' },
    { repeat: Infinity, duration: 1000, yoyo: true }
).start();

const tweenbottom = KUTE.fromTo(
    '#wave-bottom-1',
    { path: '#wave-bottom-1' },
    { path: '#wave-bottom-2' },
    { repeat: Infinity, duration: 1000, yoyo: true }
).start();


function drawBranch(p1x, p1y, p2x, p2y) {
    // mid-point of line:
    var mpx = (p2x + p1x) * 0.5;
    var mpy = (p2y + p1y) * 0.5;

    // angle of perpendicular to line:
    var theta = Math.atan2(p2y - p1y, p2x - p1x) - Math.PI / 2;

    // distance of control point from mid-point of line:
    var offset = -30;

    // location of control point:
    var c1x = mpx + offset * Math.cos(theta);
    var c1y = mpy + offset * Math.sin(theta);

    // construct the command to draw a quadratic curve
    var curve = "M" + p1x + " " + p1y + " Q " + c1x + " " + c1y + " " + p2x + " " + p2y;
    var curveElement = document.createElementNS("http://www.w3.org/2000/svg", "path");
    curveElement.setAttribute("d", curve);
    curveElement.setAttribute("stroke", "white");
    curveElement.setAttribute("stroke-width", "4");
    curveElement.setAttribute("stroke-linecap", "round");
    curveElement.setAttribute("fill", "transparent");
    document.getElementById("svg_{{ forloop.counter }}").appendChild(curveElement);
}

// // Example usage:
// window.onload = function() {
//     drawBranch(175, 50, 100, 100); // Example coordinates, replace with your own
// };

function drawBranch(p1x, p1y, p2x, p2y, counter) {
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
    var curveElement = document.getElementById("curve_"+ counter);
    
    curveElement.setAttribute("stroke", "white");
    curveElement.setAttribute("stroke-width", "4");
    curveElement.setAttribute("stroke-linecap", "round");
    curveElement.setAttribute("fill", "transparent");
    curveElement.setAttribute("d", curve);
};


function drawBranchAndCalculateCoordinates(counter) {
    // Get the coordinates of the end-point (circle au)
    var auX = parseFloat(document.getElementById("card-pos-" + counter).getBoundingClientRect().left) + 175; // Adjust as needed
    var auY = parseFloat(document.getElementById("card-pos-" + counter).getBoundingClientRect().top) + 50; // Adjust as needed

    // Get the coordinates of the start-point (circle sl)
    var slX = parseFloat(document.getElementById("card-pos-" + counter).getBoundingClientRect().left) + (document.getElementById("card-pos-" + counter).offsetWidth / 2);
    var slY = parseFloat(document.getElementById("card-pos-" + counter).getBoundingClientRect().top) + (document.getElementById("card-pos-" + counter).offsetHeight / 2);

    // Call drawBranch function with the obtained coordinates to draw connecting branch
    drawBranch(auX, auY, slX, slY, counter);
};


document.addEventListener('DOMContentLoaded', function() {
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
});

function confirmDelete() {
    if (confirm('Are you sure you want to delete this project?')) {
        document.getElementById('delete-form').submit();
    }
};


// // Example usage:
// window.onload = function() {
//     drawBranch(175, 50, 100, 100); // Example coordinates, replace with your own
// };

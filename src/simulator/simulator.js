let x;
let y;
let z;
let m; 
let cam;
let zcam;

function setup() {
    canvas = createCanvas(windowWidth, windowHeight, WEBGL);
    noStroke();
    x = random(-100, 100);
    y = windowHeight/5;
    z = random(-400, 600);
    m = true;
    cam = createCamera()
    zcam = cam.eyeZ;
}

function draw() {
    background(0);
    ambientLight(255, 122, 255);
    pointLight(255, 255, 255, 0, 0, windowHeight);

    push();
    translate(-windowWidth/5, 0, 0);
    rotateY((90 * PI) / 180);
    plane(windowWidth, windowHeight);
    pop();

    push();
    translate(windowWidth/5, 0, 0);
    rotateY((90 * PI) / 180);
    plane(windowWidth, windowHeight);
    pop();

    push();
    translate(0, windowHeight/5, 0, 0);
    rotateX((90 * PI) / 180);
    plane(windowHeight, windowWidth);
    pop();

    
    if (m) {
        push();
        translate(0, -windowHeight/2, 0);
        fill(255, 200, 255);
        rotateX((90 * PI) / 180);
        plane(windowHeight, windowWidth);
        pop();
    }

    push();
    translate(0, 0, -windowHeight);
    fill(255, 200, 200);
    plane(max(windowHeight, windowWidth), max(windowHeight, windowWidth));
    pop();
    
    drawBox(x, y, z, 100, 100);

    // behind camera wall
    push();
    translate(0, 0, zcam+1);
    fill(255, 200, 200);
    plane(max(windowHeight, windowWidth), max(windowHeight, windowWidth));
    pop();

    orbitControl(5);
}

function drawBox(x, y, z, d, gcolor) {
    push();
    translate(x, y, z);
    fill(gcolor);
    box(d);
    pop();
}

function windowResized() {
    resizeCanvas(windowWidth, windowHeight);
    zcam = cam.eyeZ;
}

function mousePressed() {
    if (m) {
        saveCanvas(canvas,"room","png");
        camera(0, -windowWidth/1.2, 0, 0, 0, 0, 0, 1, 0);
        m = false;
    }
    else {
        saveCanvas(canvas,"roomtop","png");
    }
}
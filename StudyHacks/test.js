var questions = ["1+1", "2+2", "3+3", "4+4"];
var answers = ["2", "4", "6", "8"];
var currentIndex = 0;

var currentQuestion =  questions[currentIndex];
var currentAnswer = answers[currentIndex];
var currentDisplay = 0

function setStart() {
    document.getElementById("item").innerHTML = currentQuestion;
}

function update() {
    if (currentDisplay == 0) {
        document.getElementById("item").innerHTML = currentQuestion;
    } else {
        document.getElementById("item").innerHTML = currentAnswer;
    }
}

function toggle() {
    if (currentDisplay == 1) {
        currentDisplay = 0
    } else {
        currentDisplay = 1
    }
    update();
}

function moveRight() {
    if (currentIndex != questions.length-1) {
        currentIndex += 1
        currentQuestion = questions[currentIndex]
        currentAnswer = answers[currentIndex]
    }
    update();
}
function moveLeft() {
    if (currentIndex != 0) {
        currentIndex -= 1
        currentQuestion = questions[currentIndex]
        currentAnswer = answers[currentIndex]
    }
    update();
}

window.addEventListener('keydown', (event) => {
    if (event.key == "ArrowRight") {
        moveRight();
    } else if (event.key == "ArrowLeft") {
        moveLeft();
    }

});
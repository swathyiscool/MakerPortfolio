// var questions = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"];
// var answers = ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9"];
// var replaceNow = [["q1", "a1"], ["q2", "a2"],["q3", "a3"], ["q4", "a4"], ["q5", "a5"], ["q6", "a6"], ["q7", "a7"], ["q8", "a8"], ["q9", "a9"]]
// var replaceNow = {{ replaceNow | tojson }};
// var answers = [];
// var questions = [];
// for(var element of replaceNow){
//     questions.push(element[0]);
//     answers.push(element[1]);
// }

var currentIndex = 0;
var currentQuestion =  questions[currentIndex];
var currentAnswer = answers[currentIndex];

var currentDisplay = 0

function update() {
    document.getElementById("frontText").innerHTML = currentQuestion;
    document.getElementById("backText").innerHTML = currentAnswer;
}

function setStart() {
    update();
}

function toggle() {
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
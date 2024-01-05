const cars = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9"];
function myFunction() {

    for (let i = 0; i < cars.length; i++) { 
    const box = document.createElement("div");
    box.id = "box";
    box.innerHTML = cars[i];
    const studysetqss = document.getElementById("studyqs");
    studysetqss.appendChild(box);
    }

}

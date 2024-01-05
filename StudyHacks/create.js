const studyqs = [];
const studyas = [];

const studysetqs = document.getElementById("studyqs");
const studysetas = document.getElementById("studyas");
// Define a counter variable to keep track of how many input boxes have been created
let counter = 1;

let ancurr = false;
let qcurr = false;

// Function to create a new input box for answers
function createInputA() {
  const inputa = document.createElement("input");
  inputa.type = "text";
  inputa.id = "userInputA" + counter;
  inputa.value = "a"+counter;
  inputa.className  = "inputa"
  studysetas.appendChild(inputa);
  
  inputa.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {

      const value = inputa.value;
      const index = studyas.length;
      studyas[index] = value; // store the value in the studyas array
      inputa.disabled = true; // disable the current input box when Enter key is pressed
      ancurr = true;
      if (ancurr == true && qcurr == true) {
        createInputA(); // create a new input box for answers
        createInputQ(); // create a new input box for questions
        counter++; // increment the counter variable
        ancurr = false;
        qcurr = false;
      }
    }
  });
}

// Function to create a new input box for questions
function createInputQ() {
  const inputq = document.createElement("input");
  inputq.type = "text";
  inputq.className  = "inputq"
  inputq.id = "userInputQ" + counter;
  inputq.value = "q"+counter;
  studysetqs.appendChild(inputq);

  inputq.addEventListener("keyup", function(event) {
    if (event.keyCode === 13) {
      qcurr = true;
      const value = inputq.value;
      const index = studyqs.length;
      studyqs[index] = value; // store the value in the studyqs array
      inputq.disabled = true; // disable the current input box when Enter key is pressed
      if (ancurr == true && qcurr == true) {
        createInputA(); // create a new input box for answers
        createInputQ(); // create a new input box for questions
        counter++; // increment the counter variable
        ancurr = false;
        qcurr = false;
      }
    }
  });
}

// Call the createInputA and createInputQ functions to create the initial input boxes
createInputA();
createInputQ();


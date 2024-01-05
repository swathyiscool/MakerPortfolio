// adding data in form of a dicitonary called Information
export function addData(information) {
    // sending data to /add_data Python Flask Function
    fetch('/adding_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      // making the information into a string and then sending it over
      body: JSON.stringify(information)
    })
  }


// getting data, with attributes of data being stored in dicitonary Information
export function getData(information) {
    // sending data to /get_data Python Flask Function
    return fetch('/getting_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(information)
    })
    .then(response => response.json())
    .then(data => {
      return data
    })
  }


export function getQuizletNames(information){
    return fetch('/get_quizlet_data', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(information)
  })
    .then(response => response.json())
    .then(data => {
      return data
    })
  }


// function to translate text to CHATGTP text
export function translateToChatGPT(name) {
    // return what /translateToChatGTP calls
    return fetch('/translateToChatGPT', {
        // I post text to python function
      method: 'POST',
      // I give python function name
      body: name
    })
    // python gives me response, I convert it to text
    .then(response => response.text());
}
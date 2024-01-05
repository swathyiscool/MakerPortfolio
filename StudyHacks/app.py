import os
import openai
from flask import Flask, redirect, render_template, request, url_for, jsonify

# importing important FLASK stuff
app = Flask(__name__)


# customizable key to use OPENAI
openai.api_key = os.getenv("OPENAI_API_KEY")

from flask import Flask, render_template, request

app = Flask(__name__)

# downloading HTML, main PAGE
@app.route('/')
def index():
    return render_template('index.html')

# getting input from JAVA SCRIPT Input
@app.route('/translateToChatGPT', methods=['POST'])
def process_form():
    # name is the INPUT from JAVA SCRIPT
    # decodes raw data in to String Name
    name = request.data.decode()
    # we generate the QUESTION we ask ChatGPT via a custom function
    question = generate_prompt(name)
    # we get Chat GPT's answer using a model
    # Chat_GPT_Response = openai.Completion.create(
    #     model="text-davinci-002",
    #     prompt=generate_prompt(question),
    #     temperature=0.6,
    #     max_tokens=20
    # )
    # # print the response to terminal (useful for debugging)
    # print(Chat_GPT_Response.choices[0].text)
    # #return the answer to the java script file, for it to use
    # return Chat_GPT_Response.choices[0].text
    import random
    x = random.randint(1, 10)
    x = str(x)
    return "worked" + x

from database import add_data
# Database to ADD DATA to the SERVER
@app.route('/add_data', methods=['POST'])
def handle_add_data():
    # gets data from the java script
    data = request.get_json()
    # function to add data
    add_data(data)
    # show that it worked
    return jsonify({'status': 'success'})

from database import get_data
# Accessing Database to RETRIEVE DATA from the SERVER
@app.route('/get_data')
def handle_get_data():
    dictionary = request.args.get('dictionary') 
    # gets username
    username = dictionary['username']
    # gets subject
    subject_name = dictionary['subject_name']
    # gets the data given username, and subject
    data = get_data(username, subject_name)
    # returns the data to java script application
    # prints 2d ARRAY
    print(data)
    return jsonify({'data': data})

if __name__ == '__main__':
    app.run(debug=True)

# importing testing phrases, which provides a template of how to form a question
import TestingPhrases

def generate_prompt(words):
    # if we are given a single word or multiple, make sure it is a list of words
    if isinstance(words, str):
        words = [words]
    # theme is how quizlet should format their answer
    theme_words = "Answer the questions academically in terms of chemistry"
    # this is how we ask chat GPT to format it for the coders (not useful for user)
    answer_format = "you display your answer, then you enter three times and then your next answer, and so on so forth"
    # this is how we limit how big the response should be
    num_sentences_limit = None
    num_characters_limit = 50
    limits = [num_sentences_limit, num_characters_limit]
    # we create a class with the set properties
    example = TestingPhrases.promptGenerator(theme_words, words, answer_format, limits)
    # example.prompt generates the question, and we print and return it
    print(example.prompt)
    return example.prompt














































##
@app.route('/create')
def create():
    return render_template('create.html')

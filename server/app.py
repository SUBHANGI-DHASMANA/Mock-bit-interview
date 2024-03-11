from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from transformers import AutoModelForCausalLM
import csv
import codecs
import random
from mockinterview_llama import model_setup
from langchain import PromptTemplate,  LLMChain

app = Flask(__name__)
CORS(app, origins='http://localhost:3000')

llm = model_setup()

if llm is not None:
    print("Model loaded successfully.")
else:
    print("Failed to load the model.")

file = "./Combined_Data_set.csv"
fields = []
rows = []

with codecs.open(file, 'r', 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        rows.append(row)

import traceback
def get_question():
    # try:
    #     record = random.randint(0,len(rows))
    #     topic = rows[record][0]
    #     template1 = f"""
    #     You are a data science interviewer between an interview, ask a question regarding the following given topic:
    #     Topic to ask question on as an interviewer: {topic}
    #     """
    #     print("Template:", template1)
    #     tokens = llm.tokenize(template1)
    #     print("Tokens:", tokens)
    #     next_question= llm(template1)
    #     print("Generated question (before conversion to JSON):", next_question)
    #     json_string = "{{\"question\": \"{}\", \"topic\": \"{}\"}}".format(next_question, topic)
    #     json_ques = json.loads(json_string, strict=False)
    #     return json_ques
    # except Exception as e:
    #     traceback.print_exc()
    #     print("Error generating question:", e)
    #     return {"error": str(e)}
    topic = "machine learning"
    json_string = "{{\"question\": \"{}\", \"topic\": \"{}\"}}".format("What is the difference between supervised and unsupervised learning?", topic)
    json_ques = json.loads(json_string, strict=False)
    return json_ques



def get_evaluation(response, question_data):
    # topic = question_data['topic']
    topic = "machine learning"
    template2 = f'''
    Consider yourself as a data science expert, you are in conversation with a person regarding data science and he has given you a response to the question: {topic}
    The response given by that person: {response}
    Comment on the response given by that person, whether it's correct or not, and what improvements could have been made in his response, if no improvements are required
    say that the answer was perfect, do not make up any random improvements.
    '''
    tokens = llm.tokenize(template2)
    evaluation = llm(template2, stream=False)
    json_string = json.dumps({"response": evaluation})
    json_eval = json.loads(json_string)
    print(json_eval)
    return json_eval

@app.route('/getquestion', methods=['GET'])
def generate_question():
    print("Generating question...")
    try:
        result = get_question()
        print("Generated question:", result)
        return jsonify(result)
    except Exception as e:
        print("Error generating question:", e)
        return jsonify({"error": str(e)}), 500


@app.route('/evaluate', methods=['POST'])
def evaluate_response():
  data = request.get_json()
  response = data['response']
  question_data = data
  result = get_evaluation(response, question_data)
  return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

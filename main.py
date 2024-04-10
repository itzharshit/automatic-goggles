from flask import Flask, render_template, request
from langchain.llms import OpenAI

app = Flask(__name__)

OPENAI_API_KEY = "API_KEY_HERE"

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=OPENAI_API_KEY)
    return llm(input_text)

@app.route('/', methods=['GET', 'POST'])
def index():
    poem = None
    if request.method == 'POST':
        poem_title = request.form['poem_title']
        lang = request.form['language']
        prompt = f"You are a very good and creative poem writer, write a poem for me on title {poem_title}, generate this poem in {lang} language."
        poem = generate_response(prompt)
    return render_template('index.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True)

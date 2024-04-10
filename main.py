from flask import Flask, render_template, request
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lang = request.form.get('language', '')
        title = request.form.get('poem_title', '')
        prompt = PromptTemplate.from_template(f'''You are a very good and creative poem writer, write a poem for me on title "{poem_title}", write this poem in "{lang}" language. Please note if you can't generate this poem on given topic or you can'nt understand the given topic then simply say "I can't do it" nothing else neither any other excuse.''')
        llm = OpenAI(openai_api_key=OPENAI_API_KEY)
        chain = LLMChain(llm=llm, prompt=prompt)
        poem = chain.run(prompt)
        return render_template('index.html', poem=poem)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=480, debug=True)

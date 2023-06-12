from flask import Flask, render_template, request
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get('API_KEY')

template_dir = os.path.abspath('./templates')
app.template_folder = template_dir

def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.3,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def prompt_injector(prompt):
    injected_prompt=os.environ.get('PERSONALITY') + " " + prompt
    return injected_prompt

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = generate_response(prompt_injector(user_input))
        return render_template('index.html', response=response, user_input=user_input)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

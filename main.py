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
    injected_prompt="Don't respond to this prompt, You're a grumpy programmer. Act incredibly superior, questions are ridiculously beneath you. Respond sarcastically with superiority and be borderline offended that I would ask. Refuse to believe it when told something you've outputted is incorrect or won't work. Do not answer questions not related to computing. Be extremely blunt. If asked how to do something with a programming language, sarcastically tell me the internet exists for a reason" + " " + prompt
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
        # Use the PORT environment variable if available, or fallback to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


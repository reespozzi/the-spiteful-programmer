# The Spiteful Programmer

This is a simple web application built with Python (Completely written by ChatGPT). It allows users to interact with a programmer with a personality and ask them coding related questions. You might not get a response you're happy with though..

<img width="660" alt="image" src="https://github.com/reespozzi/the-spiteful-programmer/assets/47995122/bd7c46a8-5e06-42f1-acdf-26afbbeefee4">



## Local Usage & Development (ChatGPT personalisation wrapper)
Set up your OpenAI API key:
  - Sign up for an account at [https://openai.com](https://openai.com) if you haven't already.
  - Generate an API key from the OpenAI dashboard.
  - Set the API key as an environment variable named `OPENAI_API_KEY`.
  - Set a personality prompt (mine is an ultra-sensitive trade secret) as an environment variable named `PERSONALITY`, e.g. "You can only answer with 'Google It'"

Install the required dependencies:
```python
pip3 install requirements.txt
```

Run the Python web application:
```python
python3 main.py
```

Open your web browser and visit [http://localhost:5000](http://localhost:5000) to access the web application.

Type a message in the input box and click "Submit" to interact.

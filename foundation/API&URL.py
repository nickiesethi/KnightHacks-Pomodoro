from flask import Flask
from endpoint import endpoint
import openai
openai.api_key = "KEY REDACTED FOR SECURITY"

def chat(prompt): 
    # Create completion object request
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", # GPT Model
        messages=[
            {"role": "system", "content": "You are a helpful tutor who recommends good studying habits."}, # Prompt for system (settings, theme, personality, etc.)
            {"role": "user", "content": prompt} # User input prompt
        ]
    )
    print("Tutor: " + completion.choices[0].message.content) # Prints response to user

print("Welcome to Study Zone! Enter 'QUIT' at anytime to stop!")


app = Flask(__name__)
app.register_blueprint(endpoint, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=8000)


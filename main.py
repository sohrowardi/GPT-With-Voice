import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

import speech_recognition as sr
from gtts import gTTS
import os

# Set your OpenAI API key here
openai_api_key = "YOUR_OPENAI_API_KEY"

# Function to generate text using OpenAI GPT API
def generate_text(prompt):
    # Implement your code to call OpenAI API and get the response
    # Use your OpenAI API key for authentication
    # Return the generated text
    pass

# Function to convert text to speech
def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="en")
    tts.save(filename)
    os.system("start " + filename)  # Opens the generated speech using the default media player

# Function to preprocess user input using nltk
def preprocess_text(user_input):
    # Tokenize the input
    words = word_tokenize(user_input)

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Reconstruct the sentence
    processed_input = " ".join(filtered_words)
    return processed_input

# Function to listen to user's voice
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Main loop
while True:
    user_input = listen()
    
    if user_input.lower() == "exit":
        print("Exiting...")
        break

    # Preprocess user input
    processed_input = preprocess_text(user_input)

    # Call OpenAI GPT API to generate response
    ai_response = generate_text(processed_input)

    # Convert AI-generated text to speech and play it
    text_to_speech(ai_response)                                                                                                                                                                                          
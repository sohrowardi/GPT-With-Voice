import os
import requests
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import pygame
from gtts import gTTS



# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Set your OpenAI API key here
openai_api_key = "YOUR_OPENAI_API_KEY"

# Function to generate text using OpenAI GPT API
def generate_text(prompt):
    # Implement your code to call OpenAI API and get the response
    # Use your OpenAI API key for authentication
    # Return the generated text
    url = "https://api.openai.com/v1/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 50
    }
    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()
    # Check if 'choices' key exists in the response
    if 'choices' in response_data:
        # Get the first choice (assuming there's only one)
        choice = response_data['choices'][0]
        # Check if 'text' key exists in the choice and the text is not empty
        if 'text' in choice and choice['text'].strip():
            return choice['text']
    # If 'choices' or 'text' key is not found or the text is empty, return an appropriate message
    return "Sorry, I couldn't generate a response at the moment. Please try again later."


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

# Function to listen to user's input
def listen():
    while True:
        choice = input("Would you like to input text or use voice? (text/voice): ").lower()
        if choice == "text":
            user_input = input("Enter your message: ")
            return user_input
        elif choice == "voice":
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source)
            try:
                user_input = recognizer.recognize_google(audio)
                print("You said:", user_input)
                return user_input
            except sr.UnknownValueError:
                print("Sorry, could not understand audio. Please try again.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
            print("Invalid choice. Please choose 'text' or 'voice'.")

# Function to convert text to speech and play it
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    # Save the speech to a temporary file
    tts_file = "temp.mp3"
    tts.save(tts_file)
    # Play the speech using playsound
    playsound(tts_file)
    # Remove the temporary file
    os.remove(tts_file)

# Initialize pygame
pygame.init()

# Function to convert text to speech and play it
def text_to_speech(text):
    tts = gTTS(text=text, lang="en")
    # Save the speech to a temporary file
    tts_file = "temp.mp3"
    tts.save(tts_file)
    # Load the speech file
    pygame.mixer.music.load(tts_file)
    # Play the speech
    pygame.mixer.music.play()
    # Wait for the speech to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # Remove the temporary file
    pygame.mixer.music.stop()
    pygame.mixer.quit()


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

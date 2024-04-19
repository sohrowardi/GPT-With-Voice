# GPT-in-Terminal

GPT-in-Terminal is a Python-based command-line application that allows users to interact with OpenAI's GPT models. It provides functionalities for text input, speech recognition, text processing, and text-to-speech conversion.

## Features

- **Text Input**: Users can type in their queries.
- **Voice Input**: Users can speak their queries, and the program will transcribe them.
- **Text Processing**: The program preprocesses the input to remove stopwords.
- **Text-to-Speech**: The program converts the generated text into speech and plays it back to the user.

## Installation

Before running the program, ensure you have the following dependencies installed:

- Python 3
- NLTK
- SpeechRecognition
- gTTS
- playsound
- pygame

You can install the required libraries using pip:

```bash
pip install nltk SpeechRecognition gTTS playsound pygame
```

## Usage
1. Clone the repository to your local machine.
2. Navigate to the cloned directory.
3. Run the `GPT-in-Terminal.py` script:

```bash
python GPT-in-Terminal.py
```

4. Follow the prompts to input text or use voice commands.

## Configuration
Set your OpenAI API key in the `GPT-in-Terminal.py` file:

```python
openai_api_key = "YOUR_OPENAI_API_KEY"
```

## Contributing
Contributions are welcome! Please feel free to submit pull requests or create issues for bugs and feature requests.



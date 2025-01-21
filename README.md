# ChatBot with GPT-3.5/4 and Tkinter GUI

This is a simple chatbot application built using OpenAI's GPT-3.5 or GPT-4 API and Tkinter for the graphical user interface (GUI). The chatbot allows users to interact with an AI model that can respond to user inputs and have a conversation.

## Features

- **Interactive Chat Window**: Users can type messages, and the chatbot will respond using OpenAI's GPT model.
- **Dark/Light Mode Toggle**: You can switch between dark and light modes for the interface.
- **Clear Chat Option**: You can clear the chat history with a button click.
- **Menu Bar**: The app has a menu bar with options to clear the chat or exit the application.

## Requirements

Before running this chatbot, make sure you have the following installed:

- Python 3.x
- Tkinter (typically bundled with Python, but install if necessary)
- OpenAI Python package (`openai`)

To install OpenAI Python package:

```bash
pip install openai
Setup
API Key: You need an OpenAI API key to interact with the GPT-3.5 or GPT-4 model.

Obtain your API key from OpenAI.
Replace the placeholder in the code (openai.api_key = "") with your actual API key.
Run the Application: After setting up the API key, you can run the script to launch the chatbot GUI.

bash
Copy
Edit
python chatbot.py
Interface: The application will open a window with:

A chat display area.
A text entry field for user input.
A Send button to send messages.
A menu bar with options to clear chat and toggle dark mode.
Functionality
send_message(): Handles the user's message input, sends it to the OpenAI API, and displays the response.
get_gpt_response(): Connects to OpenAI's GPT-3.5 or GPT-4 model and fetches the response.
clear_chat(): Clears the chat history.
toggle_dark_mode(): Switches between dark and light modes for the GUI.
Troubleshooting
If you get errors like "Authentication failed," ensure your OpenAI API key is correct.
In case of rate limits, try again after a brief wait.
Example
User: Hello, how are you?
ChatBot: I am doing great, thank you for asking! How can I assist you today?

License
This project is open-source. Feel free to modify or use it for your personal projects.

Credits
OpenAI for the GPT-3.5/4 API
Tkinter for creating the GUI
css
Copy
Edit

This `README.md` provides all the necessary details for someone to understand and use the chatbot application.







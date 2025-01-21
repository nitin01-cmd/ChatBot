import openai
from tkinter import *

# Set up OpenAI API Key
openai.api_key = "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"  # Replace with your actual OpenAI API key

# Function to get a response from OpenAI GPT
def get_gpt_response(prompt):
    try:
        # Call the OpenAI API using the gpt-3.5-turbo or gpt-4 model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with "gpt-4" if you have access
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        # Extract the assistant's reply
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Function to handle sending messages
def send_message():
    user_message = user_input.get()
    if not user_message.strip():
        return  # Ignore empty messages

    # Display the user message
    chat_window.insert(END, f"You: {user_message}\n")

    # Get the GPT response
    bot_response = get_gpt_response(user_message)
    chat_window.insert(END, f"ChatBot: {bot_response}\n")

    # Scroll to the bottom of the chat window
    chat_window.see(END)

    # Clear the user input field
    user_input.delete(0, END)

# Create the GUI application
root = Tk()
root.title("ChatBot with GPT")
root.geometry("500x600")

# Chat display window
chat_window = Text(root, width=60, height=30, wrap=WORD, font=("Arial", 12))
chat_window.pack(pady=10)

# User input field
user_input = Entry(root, width=50, font=("Arial", 14))
user_input.pack(pady=10)

# Send button
send_button = Button(root, text="Send", command=send_message, font=("Arial", 14), bg="blue", fg="white")
send_button.pack(pady=5)

# Start the GUI event loop
root.mainloop()

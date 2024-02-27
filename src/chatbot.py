
import os

# Get the directory of the current script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths to the data directory and Markdown files relative to the current script directory
DATA_DIR = os.path.join(os.path.dirname(CURRENT_DIR), "data")

TOPICS = {
    "variables_data_types": ["variable", "variables", "data types", "variable types"],
    "conditional_statements": ["if", "else", "elif", "conditional statements"],
    "loops": ["for loop", "while loop", "loops"]
}


# Function to read content from Markdown files
def read_markdown_file(file_name):
    file_path = os.path.join(DATA_DIR, file_name + ".md")
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

# Function to analyze user input and determine the topic
def analyze_input(user_input):
    for topic, keywords in TOPICS.items():
        for keyword in keywords:
            if keyword in user_input.lower():
                return topic
    return None

# Function to provide educational content based on user query
def provide_content(topic):
    if topic:
        content = read_markdown_file(topic)
        return content
    else:
        return "Sorry, I don't have information on that topic yet."

# Main function to handle user input and generate responses
def chat():
    print("Welcome to the Python Chatbot!")
    while True:
        user_input = input("You: ")

        # Check if the user wants to exit
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break

        # Analyze user input to determine the topic
        topic = analyze_input(user_input)

        # Provide content based on the determined topic
        response = provide_content(topic)

        # Print response
        print("Chatbot:", response)

# Call the main function to start the chatbot
if __name__ == "__main__":
    chat()

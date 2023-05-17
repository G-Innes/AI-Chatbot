import openai
import sys


# main handles the command line arguments & sets API key and AI name from them
# checks if all required arguments are present & calls conversation function & exits if not
def main():
    openai.api_key = sys.argv[1]
    ai_name = sys.argv[2]
    if len(sys.argv) != 3:
        sys.exit()
    else:
        chatbot_greeting(ai_name)


#  takes an ai_name parameter, which represents the name of the AI chatbot.
#  initializes an empty list called messages to store the conversation history.
#  this system message is appended to the messages list with the role "system".
def chatbot_greeting(ai_name):
    messages = []
    system_message = input(
        f"AI: Hello, My name is {ai_name}. What type of chatbot would you like?\n"
    )
    messages.append({"role": "system", "content": system_message})
    print(f"\nAI: OK, How can I assist you today?\n")
    chatbot_response(messages)


# the user's message is appended to the messages list with the role "user".
# API call generates a response from the AI based on the conversation history.
# the response from the AI is extracted from the API response and appended to the messages list with the role "assistant".
# AI's reply is printed to the console
def chatbot_response(messages):
    token_count = 0
    while True:
        try:
            message = input()
            messages.append({"role": "user", "content": message})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            reply = response["choices"][0]["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            print("\n AI: " + reply + "\n")
            # Update the token count by adding total of tokens used in AI response
            token_count += response["usage"]["total_tokens"]
            # Exits program & prints message with token count using ctrl D/Z
        except EOFError:
            print(f"Total tokens used: {token_count}\nGoodbye")
            sys.exit()


if __name__ == "__main__":
    main()

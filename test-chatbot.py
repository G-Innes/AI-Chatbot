from chatbot import chatbot_greeting, chatbot_response
import pytest
from unittest.mock import patch


# This function represents the Arrange and Act steps of the AAA pattern.
# It takes the AI's name as a parameter and returns a list of messages.
def chatbot_greeting(ai_name):
    messages = []
    # Arrange: Create the system message with the AI's name
    system_message = (
        f"AI: Hello, My name is {ai_name}. What type of chatbot would you like?"
    )
    # Arrange: Create the user message
    user_message = "How are you?"
    # Act: Add the system and user messages to the list
    messages.append({"role": "system", "content": system_message})
    messages.append({"role": "user", "content": user_message})
    # Return the list of messages
    return messages


# This test function represents the Assert step of the AAA pattern.
# It tests the chatbot_greeting function with different user inputs.
@pytest.mark.parametrize(
    "user_input", ["I'm good", "Not so great", "I prefer not to answer"]
)
def test_chatbot_greeting(capsys, user_input):
    ai_name = "Test AI"
    # Arrange: Define the expected messages based on the AI's name
    expected_messages = [
        {
            "role": "system",
            "content": f"AI: Hello, My name is {ai_name}. What type of chatbot would you like?",
        },
        {"role": "user", "content": "How are you?"},
    ]
    # Act: Patch the input function to simulate user input and capture the messages
    with patch("builtins.input", side_effect=[user_input, None]):
        messages = chatbot_greeting(ai_name)
        # Assert: Compare the actual messages with the expected messages
        assert messages == expected_messages

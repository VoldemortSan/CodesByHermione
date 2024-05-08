# Define patterns and responses for the customer service chatbot
patterns_responses = [
    (['hi', 'hello', 'hey'], ['Hello! Welcome to our customer service. How can I assist you today?', 'Hi there! How can I help you today?']),
    (['complaint'], ["I'm sorry to hear that. Could you please provide more details about your complaint?"]),
    (['refund', 'return'], ["Sure, I can assist you with that. Please provide your order number."]),
    (['cancel', 'cancellation'], ["I can help you with the cancellation process. Please provide your order details."]),
    (['status', 'delivery'], ["Let me check the status of your order. Could you please provide your order number?"]),
    (['thank you', 'thanks'], ["You're welcome! If you need further assistance, feel free to ask."]),
    (['bye', 'quit'], ["Goodbye! Have a great day."]),
]

# Function to find a matching response
def find_response(user_input):
    for patterns, responses in patterns_responses:
        if any(keyword in user_input.lower() for keyword in patterns):
            return responses
    return ["I'm sorry, I don't understand that."]

def main():
    print("Welcome to our Customer Service. How can I assist you today?")
    print("Enter 'bye' to end the conversation.")

    # Start interacting with the user
    while True:
        user_input = input("You: ").lower()  # Use strip() to remove newline character
        responses = find_response(user_input)
        for response in responses:
            print("Customer Service Bot:", response)

        # Check if the user wants to quit
        if user_input.lower() == 'bye':
            break

if __name__ == "__main__":
    main()
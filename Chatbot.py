import openai

# Replace with your OpenAI API key
openai.api_key = st.secrets["api_secret"]

def gpt4_chatbot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

def main():
    print("Hello! I'm a GPT-4 chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        response = gpt4_chatbot(user_input)
        print("Chatbot: " + response)


    st.title("chatbot :  streamlit + openai")


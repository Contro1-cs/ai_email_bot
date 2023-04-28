import openai
import streamlit as st
import pyperclip

openai.api_key = "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"


def app():
    st.title("Welcome to AI email bot")

    # create the dropdown menu with key-value pairs
    name_dict = {
        "Pratichee": "pradichee@gmail.com",
        "Shreyans": "shreyans@gmail.com",
        "Niranjan": "niranjan@gmail.com",
        "Aaditya": "aaditya@gmail.com"
    }
    name = st.selectbox("Select reciever", list(name_dict.keys()))
    reciever = name_dict[name]

    st.write("Enter your message after: Write an email to...")
    user_input = st.text_input("You can be as specific as you want!")
    wordCount = '300'
    tone = 'casual'
    notes = ''
    sender = 'Aaditya'
    editedPrompt = 'Write a detailed email to ' + name + ' on the following topic: ' + user_input + '. Keep the word count up to ' + wordCount + ' and keep the tone ' + \
        tone + 'At last I am the sender so mention my name as ' + sender

    if st.button("Generate email"):
        try:
            maxTokens = 1024
            response = openai.Completion.create(
                engine="text-davinci-002", prompt=editedPrompt, max_tokens=maxTokens
            )
            output_text = response["choices"][0]["text"]
            st.write(output_text)
            if st.button("Copy"):
                pyperclip.copy(output_text)
        except Exception as e:
            st.write("Oops! Something went wrong. Please try again later.")
            st.write(e)


# Run the Streamlit app
if __name__ == "__main__":
    app()

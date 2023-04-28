import openai
import streamlit as st

openai.api_key = "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"


def app():
    st.title("Welcome to AI email bot")
    st.write("Enter your message after: Write an email to...")

    user_input = st.text_input("You can be as specific as you want!")
    name = 'Niranjan Mathur'
    wordCount = '300'
    tone = 'casual'
    notes = ''
    editedPrompt = 'Write a detailed email on the following topic: ' + user_input + '. use my full name as ' + name + \
        'keeping the word count up to ' + wordCount + 'and keep the tone ' + \
        tone + '. Additionally also mention' + notes

    if st.button("Submit"):
        try:
            # if (wordCount <= 300):
            #     maxTokens = 521
            # elif (wordCount < 600):
            #     maxTokens = 800
            # else:
            #     maxTokens = 1024
            maxTokens = 1024
            response = openai.Completion.create(
                engine="text-davinci-002", prompt=editedPrompt, max_tokens=maxTokens
            )
            st.write(response["choices"][0]["text"])
        except Exception as e:
            st.write("Oops! Something went wrong. Please try again later.")
            st.write(e)


# Run the Streamlit app
if __name__ == "__main__":
    app()

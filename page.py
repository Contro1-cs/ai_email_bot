import openai
import streamlit as st



def app():
    st.title("Welcome to AI email bot")
    st.write("Enter your message after: Write an email to...")

    user_input = st.text_input("You can be as specific as you want!")
    name = 'Niranjan Mathur'
    wordCount = '300'
    tone = 'formal'
    editedPrompt = user_input + 'use my full name as ' + name + \
        'keeping the word count up to ' + wordCount + 'and keep the tone ' + tone

    if st.button("Submit"):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002", prompt=editedPrompt, max_tokens=1024
            )
            st.write(response["choices"][0]["text"])
        except Exception as e:
            st.write("Oops! Something went wrong. Please try again later.")
            st.write(e)


# Run the Streamlit app
if __name__ == "__main__":
    app()

import openai
import streamlit as st

openai.api_key = "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"



def app():
    st.title("Welcome to AI email bot")
    st.write("Enter your message after: Write an email to...")

    user_input = st.text_input("You can be as specific as you want!")

    if st.button("Submit"):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002", prompt=user_input, max_tokens=1024
            )
            st.write(response["choices"][0]["text"])
        except Exception as e:
            st.write("Oops! Something went wrong. Please try again later.")
            st.write(e)


# Run the Streamlit app
if __name__ == "__main__":
    app()

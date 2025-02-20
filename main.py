import streamlit as st


st.title("WeCredit Chatbot")

# Welcome message
st.write("Welcome to the WeCredit chatbot! Ask your financial queries here.")

# User input
user_input = st.text_input("Type your question:")

# Simple response logic (You can replace this with an actual AI model)
responses = {
    "loan": "We offer personal and business loans at competitive rates!",
    "interest rate": "Our interest rates range from 8% to 12% depending on the loan type.",
    "credit score": "A good credit score is usually above 750. Let us know if you need a credit report check!"
}

# Display response
if user_input:
    response = responses.get(user_input.lower(), "I'm sorry, I don't have an answer for that yet.")
    st.write(response)

import streamlit as st
import groq

def chatbot(prompt):
  response = client.chat.completions.create(
      model="LLAMA3-8B-8192",
      messages=[
          {"role": "user", "content": prompt}
      ]
  )
  return response.choices[0].message.content

# Streamlit app starts here
def main():
    st.title("GPT Chatbot Model - LLAMA3-8B-8192")
    st.write("Enter your question below:")

    # Input atext box for user
    user_input = st.text_area("You:", height=100)

    # Button to send input to chatbot
    if st.button("Submit"):
        if user_input:
            # Call the chatbot function
            response = chatbot(user_input)
            st.write(f"Chatbot: {response}")
        else:
            st.write("Please enter a message.")

# Set up your Groq API key
groq_api_key = st.secrets["groq_api_key"] 

# Run the main function
if __name__ == "__main__":
    main()

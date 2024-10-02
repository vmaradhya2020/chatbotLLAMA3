import streamlit as st
import Groq
from groq import Groq 

def chatbot(prompt):
  response = client.chat.completions.create(
      model="LLAMA3-8B-8192",
      messages=[
          {"role": "user", "content": prompt}
      ]
  )
  return response.choices[0].message.content

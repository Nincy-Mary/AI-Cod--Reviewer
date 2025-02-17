import google.generativeai as genai
import streamlit as st

st.title("AI Code Reviewer")

genai.configure(api_key='API')
system_instruction = """Send me the code,
 and I'll carefully analyze it to find any bugs.
   I'll explain where the issue is, why it's happening, and how to fix it. 
   Then, I'll provide the corrected version with a clear beginner-friendly explanation. str
"""


model = genai.GenerativeModel(model_name="models/gemini-2.0-flash-thinking-exp-1219",system_instruction=system_instruction)

def solve(user_prompt):
    
    respose = model.generate_content(user_prompt)
    
    
    return respose.text

np =st.text_area("Enter the code:")

if st.button("Debug >") and np:

    text = solve(np)
    st.write(text)
    # print(eval(text))

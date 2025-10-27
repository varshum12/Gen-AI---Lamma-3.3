# Write your code here
import streamlit as st
from groq import Groq

st.set_page_config(page_title= 'Gen Ai  Project ')
st.title('Lamma 3.3 gen Ai Project')
st.subheader('By Varsha Mhetre')
user_input =  st.text_area('Ask Any Question')

api_key  =  st.secrets['API_KEY']

client  =  Groq(api_key= api_key)

def model_respose(text :  str  ,  model_name =  "llama-3.3-70b-versatile"):
    stream  =  client.chat.completions.create(
        messages=  [
            {'role' :  'system' ,  
            'content' :  'you are helpful  assitant '} ,  

            {'role' :  'user' ,  
            'content' : text}

        
        ]  , 
        model  =  model_name , 
        stream= True

    )

    for  chunk  in  stream:
        response =  chunk.choices[0].delta.content
        if  response is not None:
            yield response

submit  =  st.button('Generate' ,  type  =  'primary')
if submit  :
    st.subheader("Generate  response")
    st.write_stream(model_respose(user_input))
import os
import openai
import streamlit as st

openai.api_key = os.getenv("CHATGPT_OPEN_API_KEY")

def translate_text(text, src_lang, trg_lang):
    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=f"Translate the following {src_lang} text to {trg_lang}: {text}",
                                        max_tokens=200,
                                        n=1,
                                        temperature=1)
    translated_text = response.choices[0].text.strip()
    return translated_text


def translate_text_using_chatgpt(text, src_lang, trg_lang):
    system_instruction = f"assistant는 번역앱으로서 동작한다. {src_lang}을 {trg_lang}으로 번역하고 번역된 텍스트만 출력한다."
    
    messages = [{"role":"system","content":system_instruction},
                {"role":"user","content":text}]
    
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages)
    print(response)
    
    translated_text = response['choices'][0]['message']['content']
    return translated_text


st.title("번역 서비스")

text = st.text_area("번역할 텍스트를 입력하세요","") 
src_lang = st.selectbox("원본 언어",["영어","한국어","일본어"], index=1)
trg_lang = st.selectbox("목표 언어",["영어","한국어","일본어"], index=0)

print(text, ":", src_lang, "->", trg_lang)

if st.button("번역"):
#    translated_result = translate_text(text, src_lang, trg_lang)
    translated_result = translate_text_using_chatgpt(text, src_lang, trg_lang)

    st.success(translated_result)
    

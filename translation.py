import streamlit as st
import pandas as pd
import requests
import json

# CLIENT_ID, CLIENT_SECRET = "m07Qad52bxDZmilgu_NN", "5EljNoNpWx" 
CLIENT_ID, CLIENT_SECRET = 'Ii8Zm5aHg0msCsfIINF9', 'XW4JCcoWhW'

def language_detection(text):
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    headers = {
     "Content-Type": "application/json",
     "X-Naver-Client-Id": CLIENT_ID,
     "X-Naver-Client-Secret": CLIENT_SECRET 
    }
    params = {"query": text}
    response = requests.post(url,json.dumps(params), headers=headers)
    result = response.json()["langCode"]
    return result

@st.experimental_memo
def translate(text, source, target):
    if source == target :
        return
    
    url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
     "Content-Type": "application/json",
     "X-Naver-Client-Id": CLIENT_ID,
     "X-Naver-Client-Secret": CLIENT_SECRET 
    }
    params = {"source": source, "target": target, "text": text}
    response = requests.post(url, json.dumps(params), headers=headers)
    result = response.json()["message"]["result"]["translatedText"]
    return result

lang_list = ['한국어(ko)','영어(en)','일본어(ja)','중국어 간체(zh-CN)','중국어 번체(zh-TW)','스페인어(es)','프랑스어(fr)','독일어(de)', '베트남어(vi)','인도네시아어(id)','러시아어(ru)','이탈리아어(it)']
# '힌디어(hi)' , '포르투갈어(pt)' , '페르시아어(fa)', '아랍어(ar)', '미얀마어(mm)'
lang = st.multiselect('언어',lang_list,)
text = st.text_area('입력',placeholder='text here', key='text',value='',max_chars=300)
if text :
    for index, i in enumerate(range(len(lang))):
        st.text_area(f'{lang[i]}',translate(text,source= language_detection(text), target=lang[index][lang[index].index('(') +1: lang[index].index(')')]))
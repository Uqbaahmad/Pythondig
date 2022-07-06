import streamlit as st
from textblob import TextBlob
from textblob import Word
# streamlit run nlp.py
# make Sidebar

def get_all_nouns(blob):
    nouns = []
    for tag in blob.tags:
        if tag[1] == "NN":
            nouns.append(tag[0])
    return nouns        
        
def get_sentiment(blob):
    polarity =  blob.sentiment.polarity
    if polarity < 0:
        return "negative"
    elif polarity == 0:
        return "neutral"
    else:
        return "positve"

def spell_check(text):
    words = text.split()
    output = {}
    for word in words:
        output[word] = Word(word).spellcheck()[0][1]
        return output        


st.sidebar.title("NLP using TextBlob")
msg = st.text_area("Enter Something in English", height=300)

#st.sidebar.subheader("Table of Content")                                                    #display
#st.sidebar.write(msg)              
#              
if st.button("Update"):
    st.sidebar.subheader("Table of Content")
    st.sidebar.write(msg)
if msg:
    blob = TextBlob(msg)     
    st.subheader("Part of Speech Tagging: Nouns")
    st.write(get_all_nouns(blob))

    st.subheader("Sentimental Analaysis")
    st.info(get_sentiment(blob))

    st.subheader("Check spelling")
    st.write(spell_check(msg))
    st.write(blob.correct())

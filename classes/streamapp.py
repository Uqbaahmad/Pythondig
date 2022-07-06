import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine 
from database import Author



def opendb():
    engine = create_engine('sqlite:///mydb.sqlite')
    Session = sessionmaker(bind=engine)
    return Session()
    

def add_author(name):
    db = opendb()                 # open database
    a = Author(name = name)       # create new author
    db.add(a)                     # add author to database
    db.commit()                   # commit changes
    db.close()                    # close database

def show_authors():
    db = opendb()
    a = Author(name= name)
    db.add(a)
    db.commit()
    db.close()

def delete_author(name):
    try:
        db = opendb()
        a = db.query(Author).filter_by(name = name).first()
        db.delete(a)
        db.commit()
        db.close()
        print("Author deleted")
    except: 
        print("Author not found")  

# to run
# streamlit run .\classes\streamapp.py


st.title("Book App")
st.subheader("Will use database to load and save data")

choices = ['List Authors', 'Add Author', 'Delete Author']
choice = st.sidebar.selectbox('Select An Option', choices)

if choice == choices[0]:
    for author in show_authors():
        st.subheader(f"{author.id}. {author.name}")
elif choice == choices[1]:
    name = st.text_input('Enter author name: ')
    if name:
        add_author(name)
        st.success('Author added')
    else:
        st.warning('Please enter author name')
elif choice == choices[2]:
    name = st.text_input('Enter author name: ')
    if name:
        if delete_author(name):
            st.success('Author deleted')
        else:
            st.error('Author not found')
    else:
        st.warning('Please enter author name')



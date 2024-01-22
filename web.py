import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo list:")
st.write("This app is to increase your productivity")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="New todo" , placeholder="Add new todo", 
              label_visibility="hidden")
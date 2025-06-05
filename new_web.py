import streamlit as st
import web_functions

todos = web_functions.get_todos()

def add_todo():
    temp_todo = st.session_state["new_todo"].title() + '\n'
    todos.append(temp_todo)
    web_functions.write_todos(todos)

st.title("My Todo App")
st.subheader("Use this app and boost productivity.\n")
st.write("Enter a todo:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{todo}_{index}")
    if checkbox:
        todos.pop(index)
        web_functions.write_todos(todos)
        st.rerun()

st.text_input(label="", placeholder="Add a todo...",
              on_change=add_todo, key='new_todo')






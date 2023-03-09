import streamlit as st
import function

todos = function.readfile()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new todo"] + "\n"
    todos.append(todo)
    function.writefile(todos)


st.title("Todo App")
st.subheader("this is my todo app")
st.write("This app is build by <b>Pritam</b>", unsafe_allow_html=True)

st.text_input(label="", placeholder="Add new todo.......", on_change=add_todo, key="new todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.writefile(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.write("Select the items to remove it")

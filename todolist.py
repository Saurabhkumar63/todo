import streamlit as st
st.set_page_config(page_title="to do list",page_icon=":bar_chart:",layout="wide")
st.title(":bar_chart:  todo list")
st.markdown("""<style>.stMainBlockContainer{padding-top:2rem}</style>""",unsafe_allow_html=True)
st.write("manage your daily task")
if"task" not in st.session_state:
    st.session_state.task=[]
task=st.text_input("enter your task")
if st.button("add task"):
    if task.strip():

      st.session_state.task.append(task)
      st.success("task add succesfully")
    else:
       st.warning("please enter a task")
st.subheader("My task")
for i ,item in enumerate(st.session_state.task):
    st.write(f"{i+1}.{item}")
if st.button("clear all task"):
   st.session_state.task=[]
   
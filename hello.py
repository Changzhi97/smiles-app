#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

st.title("Hello Streamlit 👋")
st.write("这是我的第一个 Streamlit 网页！")

name = st.text_input("请输入你的名字：")
if st.button("打招呼"):
    st.success(f"你好，{name}！")


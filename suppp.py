import pickle
import streamlit as st
from os import path
import numpy as np

st.title("phishing website detection app")

filename="kmodel.pk"
with open(path.join(filename),'rb') as f:
    kmodel=pickle.load(f)
    
Domain=st.text_input("insert a sepel length")
Have_IP=st.number_input("insert a sepel width")
Have_At=st.number_input("insert a petal lemgth")
URL_Length=st.number_input("insert a petal length")
URL_Depth=st.number_input("insert a petal lemgth")
Redirection=st.number_input("insert a petal lemgth")
https_Domain=st.number_input("insert a petal lemgth")
TinyURL=st.number_input("insert a petal lemgth")
Prefix_Suffix=st.number_input("insert a petal lemgth")
DNS_Record=st.number_input("insert a petal lemgth")
Web_Traffic=st.number_input("insert a petal lemgth")
Domain_Age=st.number_input("insert a petal lemgth")
Domain_End=st.number_input("insert a petal lemgth")
iFrame=st.number_input("insert a petal lemgth")
Mouse_Over=st.number_input("insert a petal lemgth")
Right_Click=st.number_input("insert a petal lemgth")
Web_Forwards=st.number_input("insert a petal lemgth")
if st.button("predict"):
    pred=kmodel.predict(np.array([[Domain,Have_IP,Have_At,URL_Length,URL_Depth,Redirection,https_Domain,TinyURL,Prefix_Suffix,DNS_Record,Web_Traffic,Domain_Age,Domain_End,iFrame,Mouse_Over,Right_Click,Web_Forwards]]))
    st.write("the website is phishing",pred[0])

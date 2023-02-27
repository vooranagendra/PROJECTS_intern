import streamlit as st

st.title(":green[PROFILE]")

btn_click = st.button("Click HERE TO SEE MY PROFILE")

if btn_click == True:
    st.subheader(":blue[NAME]")
    st.write("VOORA NAGENDRA BHASKARA SWAMY")
    st.subheader(":blue[QUALIFICATION]")
    st.write("B.TECH CSE 3 rd year")
    st.subheader(":blue[COLLEGE]")
    st.write("RGUKT Srikakulam")
    st.subheader(":blue[AREA OF EXPERTISE]")
    st.write("Python")
    st.write("C")
    st.write("MachineLearning")
    st.write("DataScience")
    st.subheader(":blue[CONTACT DETAILS]")
    st.write("phone number: 9705823166")
    st.write("mail id: vooranagendra1729@gmail.com")
    st.write("linkedin: linkedin/nagendravoora")

st.header(":green[THANKS FOR VISITING THE PAGE]")



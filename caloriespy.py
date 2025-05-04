import streamlit as st
import joblib
import pandas as pd

model=joblib.load(r'D:\data science\7)machine learning\projects\4-calories\caloriesModel.pkl')

st.title('calories calc helloooo!')
st.info('App to calc calories')
st.sidebar.header('hello input the values to calc calories')

Gender=st.sidebar.text_input('Gender')
Age=st.sidebar.text_input('Age')
Height=st.sidebar.text_input('Height')
Weight=st.sidebar.text_input('Weight')
Duration=st.sidebar.text_input('Duration')
Heart_Rate=st.sidebar.text_input('Heart_Rate')
Body_Temp=st.sidebar.text_input('Body_Temp')

df=pd.DataFrame({
    'Gender':[Gender],
    'Age':[Age],
    'Height':[Height],
    'Weight':[Weight],
    'Duration':[Duration],
    'Heart_Rate':[Heart_Rate],
    'Body_Temp':[Body_Temp]
})

button_confirm=st.button('confirm')
if button_confirm:
    result=model.predict(df)
    st.write(result)
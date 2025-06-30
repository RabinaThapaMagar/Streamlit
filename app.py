import streamlit as st
from predict import predict_diabetes



st.set_page_config(
    page_title = 'Diabetes Prediction App'
)
st.title('Diabetes Prediction')
st.header('Input your data:')

glucose = st.number_input('Glucose',min_value=0, max_value = 400, value = 20)
Blood_pressure = st.number_input('Blood Pressure', 0,200,0)
dfp = st.number_input('DFP', 0, 20)
age = st.number_input('Age',20,80,40)

if st.button('Test Diabetes'):
    input_data = [glucose,Blood_pressure,dfp,age]
    result = predict_diabetes(input_data)
    print('result')


    if result[0] == 1:
        st.warning('High probability of Diabetes')
        st.warning('See you doctor')
    else:
        st.success('Low chance of Diabetes')



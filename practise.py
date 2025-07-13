import streamlit as st

st.write('Building own app')
st.title('Cosmos college')
st.markdown('Sports')
st.header('1200ml')


st.radio('Gender',['Male','Female']) #multiselect garnaa paidenaa
st.selectbox('pick a fruit',['Apple','orange','Mango'])

st.multiselect('choose a planet',['Jupiter','Mars','Neptune'])
st.slider('pick a number', 0,50)

st.success("you did it!")

st.error("Error occured")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")

st.button('Ck=lick here')
st.number_input('enter yourinput :,0,100')



st.sidebar.title('Here it comes:') #left ma side lenchhaa yesle

st.container() #field chhutaune
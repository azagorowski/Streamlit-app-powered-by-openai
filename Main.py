import streamlit as st
from model import GeneralModel


def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("APIkey", type="password")
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip() , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Search for SP500 company and it's current closing stock price:")

        # st.write("---")

        s_example = "Google (Alphabet Inc.) stock price on 5th October 2022"
        input = st.text_area(
            "Use the example below or input your own company name and date",
            value=s_example,
            max_chars=80,
            height=20,
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")

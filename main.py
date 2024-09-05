import streamlit as st
import pandas as pd
import random
import string


# logo = st.image("budget_logo.png", use_column_width=1)


"""
# Aylıq büdcəni planla!
"""

st.divider()


operation_id = "".join(random.sample(list(string.printable[:62]), k=8))
date = st.date_input(label="Tarix:", value=None)
item = st.text_input(label="Fəaliyyət:", value=None)
expenditure = st.number_input(label="Xərc:", value=None)


df = pd.read_csv("check.csv")


if item in df["item"].unique():
    item_id = df.loc[df["item"] == item, "item_id"].iloc[0]
else:
    item_id = "".join(random.sample(list(string.printable[:62]), k=8))
    

if st.button(label="Əlavə et") and date != None and item != None and expenditure != None:
    st.text(body=f"{operation_id},{date},{item_id},{item},{expenditure}")
    with open("check.csv", mode="a") as file:
        file.write(f"{operation_id},{date},{item_id},{item},{expenditure}\n")
    file.close()


st.divider()


if st.button("Mövcud büdcə planına bax"):
    if st.button("Bağla"):
        pass
    st.dataframe(df, hide_index=True)
    # if st.button("Planda düzəliş et"):
    #     pass
    
    
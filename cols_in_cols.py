import streamlit as st

LOREM = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
LOREM = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."


def cols_in_cols110():
    subcol1, subcol2, subcol3, subcol4 = st.columns(4)
    subcol1.write(LOREM)
    subcol2.write(LOREM)
    st.write("")
    st.write(LOREM)

    subcol3.write(LOREM)
    subcol4.write(LOREM)

    st.write("")
    subcol3.write(LOREM)
    subcol4.write(LOREM)


def cols_in_cols117():
    col1, col2 = st.columns(2, gap="large")
    with col1:
        subcol1, subcol2 = st.columns(2, gap="medium")
        subcol1.write(LOREM)
        subcol2.write(LOREM)
        st.write("")
        st.write(LOREM)

    with col2:
        subcol1, subcol2 = st.columns(2, gap="medium")
        subcol1.write(LOREM)
        subcol2.write(LOREM)

        st.write("")
        subcol1, subcol2 = st.columns(2, gap="medium")
        subcol1.write(LOREM)
        subcol2.write(LOREM)

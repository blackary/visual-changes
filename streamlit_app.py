import plotly.express as px
import streamlit as st
from cols_in_cols import cols_in_cols110, cols_in_cols117

st.set_page_config("Visual Changes from Streamlit 1.10 to 1.17", page_icon="🪄")

st.title("Streamlit 1.10 to Streamlit 1.17")

version = st.sidebar.radio("Streamlit version:", ["1.10", "1.17"], horizontal=True)

sections = []


def add_section(text: str, silent: bool = False):
    if not silent:
        st.subheader(text)
    anchor = text.replace(" ", "-").lower()
    sections.append((text, anchor))


add_section("Columns in columns and column gaps")

if version == "1.17":
    cols_in_cols117()
else:
    cols_in_cols110()


add_section("Colored and full-width buttons")

if version == "1.17":
    left, right = st.columns(2)
    with left:
        st.button("Button1", use_container_width=True)
        st.button("Button2", type="primary", use_container_width=True)
    with right:
        st.button("Button3")
        st.button("Button4", type="primary")

else:
    left, right = st.columns(2)
    with left:
        st.button("Button1")
        st.button("Button2")
    with right:
        st.button("Button3")
        st.button("Button4")

add_section("Metrics with hidden labels")

if version == "1.17":
    st.write("Temperatures:")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temperature", "70 °F", label_visibility="collapsed")
    col2.metric("Temperature", "72 °F", "2 °F", label_visibility="collapsed")
    col3.metric("Temperature", "68 °F", "-5 °F", label_visibility="collapsed")
    col4.metric("Temperature", "62 °F", "-3 °F", label_visibility="collapsed")
else:
    st.write("Temperatures:")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Temperature", "70 °F")
    col2.metric("Temperature", "72 °F", "2 °F")
    col3.metric("Temperature", "68 °F", "-5 °F")
    col4.metric("Temperature", "62 °F", "-3 °F")

add_section("Streamlit theme for Altair charts")

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

if version == "1.17":
    st.plotly_chart(
        fig,
        theme="streamlit",
    )
else:
    st.plotly_chart(
        fig,
        theme=None,
        use_container_width=True,
    )


if version == "1.17":
    st.subheader(":red[Colors] in :blue[text]")
else:
    st.subheader("Colors in text")

add_section("Colors in text", silent=True)

add_section("Tabs")

if version == "1.17":
    s1, s2 = st.tabs(["Section 1", "Section 2"])

    with s1:
        st.write("**This is section 1**")
    with s2:
        st.write("**This is section 2**")

else:
    section = st.radio("Choose a section", ["Section 1", "Section 2"])

    if section == "Section 1":
        st.write("**This is section 1**")
    elif section == "Section 2":
        st.write("**This is section 2**")

for text, anchor in sections:
    st.sidebar.write(f"[{text}](#{anchor})")

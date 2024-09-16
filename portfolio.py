import streamlit as st

st.set_page_config(
    page_title="Kylian's Portfolio",
)

def introduction():
    st.title("Kylian Tarde")
    st.header("Big Data and Machine Learning Apprentice")
    st.divider()
    st.write("Hello, my name is Kylian :smile:. "
             "I am an engineering student, currently studying Data Science and Machine Leaning at EFREI."
             "I also work at Thales as a Machine Learning Engineer until August 2026.")


def formation():
    st.title("Formation")
    st.divider()
    tab1, tab2, tab3 = st.tabs(["EFREI Paris", "Sorbonne Université", "Lycée Montesquieu"])

    with tab1:
        st.header("EFREI Paris")
        st.markdown("**2024 - 2026**")
        st.markdown("**Engineering Degree - Big Data & Machine Learning**")
        st.markdown("**2023 - 2024**")
        st.markdown("**Bachelor's Degree - Software Engineering**")

    with tab2:
        st.header("Sorbonne Université")
        st.markdown("**2020 - 2023**")

    with tab3:
        st.header("Lycée Montesquieu")
        st.markdown("**2017 - 2020**")


def experience():
    st.title("Experience")
    st.divider()


def social_media():
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <a href="https://www.linkedin.com/in/tardekylian/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/900px-LinkedIn_logo_initials.png?20140125013055" width="30" />
            </a>
            """, unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <a href="https://github.com/Kykyto/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30" />
            </a>
            """, unsafe_allow_html=True
        )


page_names_to_funcs = {
    "Introduction": introduction,
    "Formation": formation,
    "Experience": experience
}

with st.sidebar:
    st.header("Portfolio")

portfolio_name = st.sidebar.selectbox("Explore my portfolio", page_names_to_funcs.keys())

with st.sidebar:
    st.header("Contact")
    st.write("Phone : +33 6 51 63 25 36")
    st.write("E-mail : Tarde.Kylian@gmail.com")
    social_media()

page_names_to_funcs[portfolio_name]()
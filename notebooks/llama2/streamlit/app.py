import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import ctransformers

# talk to llama2 model

def main():
    "main"

    st.set_page_config(
        page_title="The llama2-7b blogger",
        page_icon="📝",
        layout="centered",
        initial_sidebar_state="collapsed",
    )

    st.header("The llama2-7b blogger 📝", divider="rainbow")

    st.subheader(
        "This application generates an :red[article] based on your :green[topic] and :blue[gener]. :sunglasses:"
    )

    st.markdown("[check out the repository](https://github.com/ThivaV/llama_cookbook/tree/main/notebooks/llama2)")

    user_input = st.text_input("Enter the topic you wanted the blog")

    col_1, col_2 = st.columns([5, 5])
    with col_1:
        no_of_words = st.selectbox(
            "Number of words", ("200", "250", "300", "350", "400", "500")
        )
    with col_2:
        blog_genres = st.selectbox(
            "Genre of the blog",
            (
                "Science & Technology",
                "Business",
                "Food",
                "Music",
                "Fitness",
                "Travel",
                "Gaming",
                "Finance",
                "Sports",
                "Movie",
                "Lifestyle",
            ),
            index=0,
        )

    submit = st.button("Start Blogging")
    if submit:
        with st.spinner("Blogging started, Please wait.."):
            blog = generate_blog(user_input, no_of_words, blog_genres)
            st.write(blog)
        st.success("Done!")


if __name__ == "__main__":
    main()
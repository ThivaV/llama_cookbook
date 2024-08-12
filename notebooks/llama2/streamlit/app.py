import streamlit as st
from langchain_community.llms import CTransformers  # type: ignore
from langchain_core.prompts import PromptTemplate   # type: ignore

# talk to llama2 model
def load_model():
    """load model"""

    llm = CTransformers(model='../../../models/llama-2-7b-chat.Q8_0.gguf', 
                        model_type='llama', 
                        config={"max_new_tokens": 256, "temperature": 0})
    return llm


# request for blog content
def generate_blog(query, word_count, genre):
    """generate blog"""

    template = """
    As a you a blogger, please write a blog for the topic {query} and under gener {genre}.
    Please write the blog in {word_count} words.
    Your blog strictly should be in markdown language.
    Also, come with an appropriate title for the blog and set it at the top in bold letters.      
    """

    prompt = PromptTemplate(
        input_variables=["query", "word_count", "genre"], template=template
    )

    llama2_model = load_model()
    response = llama2_model.invoke(
        prompt.format(query=query, word_count=word_count, genre=genre)
    )
    return response


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

    st.markdown("[Check out the repository](https://github.com/ThivaV/llama_cookbook/tree/main/notebooks/llama2/streamlit)")
    st.markdown("[Playground](https://huggingface.co/spaces/thivav/llama2-blogger?logs=container)")

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
import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
import os



# Page configuration
st.set_page_config(page_title="Simple LangChain Chatbot with Groq", page_icon="🚀")




with st.sidebar:
    st.header("Settings")
    st.markdown("Configure your Groq API key and model settings here.")
    
    # API Key input
    api_key = st.text_input("Groq API Key", type="password", placeholder="Enter your Groq API key")
    
    # Model selection
    model_name = st.selectbox("Select Groq Model", options=["openai/gpt-oss-20b", "openai/gpt-oss-120b"], index=0)
    
    # Clear chat history button
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
       
   # Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

@st.cache_resource
def get_chain(api_key, model_name):
    if not api_key:
        return None
    

    # Initialize the ChatGroq model
    llm=ChatGroq(
        api_key=api_key,
        model=model_name,
        temperature=0.7,
        streaming=True
    )


    # Create a prompt template for the conversation
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant powered by Groq. Answer the user's questions clearly and accurately."),
        ("user", "{question}")
    ])

    # Create a chain
    chain = prompt_template | llm | StrOutputParser()
    return chain

# calling the chain
chain = get_chain(api_key, model_name)

# 
if not chain:
    st.warning("👆 Please enter your Groq API key in the sidebar to start chatting!")
    st.markdown("[Get your free API key here](https://console.groq.com)")

else:
    ## Display the chat messages

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    
    ## chat input
    if question:= st.chat_input("Ask me anything"):
        ## Add user message to session state
        st.session_state.messages.append({"role":"user","content":question})
        with st.chat_message("user"):
            st.write(question)

        # Generate response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # Stream response from Groq
                for chunk in chain.stream({"question": question}):
                    full_response += chunk
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                
                # Add to history
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"Error: {str(e)}")


# title and description
st.title("🚀 Simple LangChain Chat with Groq")
st.markdown("Learn LangChain basics with Groq's ultra-fast inference!")






from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

def generate_content(topic):
    # Initialize the Groq LLM client
    llm = ChatGroq(
        api_key="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",
        model_name="llama3-70b-8192",
        temperature=0.7,
    )

    messages = [
        SystemMessage(content="You are a helpful tutor."),
        HumanMessage(content=f"Explain the topic '{topic}' in simple language for college students."),
    ]

    try:
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        raise RuntimeError(f"LLM call failed: {e}")

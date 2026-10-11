def llm():
    from dotenv import load_dotenv
    from langchain_google_genai import ChatGoogleGenerativeAI

    load_dotenv()
    return ChatGoogleGenerativeAI(model="gemini-flash-lite-latest", max_tokens=1000)

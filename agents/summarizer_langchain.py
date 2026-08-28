"""Document summarizer chain."""
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_anthropic import ChatAnthropic
from langchain_core.documents import Document

llm = ChatAnthropic(model="claude-opus-4-5-20251101", max_tokens=4096)
splitter = RecursiveCharacterTextSplitter(chunk_size=4000, chunk_overlap=200)
chain = load_summarize_chain(llm, chain_type="map_reduce")


def summarize(raw_text: str) -> str:
    docs = [Document(page_content=c) for c in splitter.split_text(raw_text)]
    return chain.invoke({"input_documents": docs})["output_text"]

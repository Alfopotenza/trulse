from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
model = OllamaLLM(model = "llama3.2")
template = ("You are being asked with extracting specific information from the following text content: {dom_content}"
          "You must follow these instructions carefully: \n\n"
          "1. **EXTRACT INFORMATIONS** only extract the informations that directly match the provided description: {parse_description}"
          "2. **EXTRA CONTENT** Do not include any additional text, comments or explanations in your response"
          "3. **EMPTY RESPONSE** If no information matches the description, return an empty string: ('')"
          "4. **DIRECT DATA ONLY** Your output should contain only the data that is explicitly requested, with no additions")
def parse_with_ollama(dom_chunks, parse_desc):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start = 1):
        response = chain.invoke({"dom_content": chunk, "parse_description": parse_desc})
        print(f"Parsed batch {i} of {len(dom_chunks)}")
        parsed_results.append(response)

    return "\n".join(parsed_results)
from app.pinecones import search_query
from app.llm import generate_answer

print("\n==============================")
print(" HR Policy RAG Assistant")
print("==============================")
print("Type 'exit' to stop.\n")

# Chat history for context awareness
chat_history = ""

while True:

    query = input("Ask question: ")

    if query.lower() == "exit":
        print("\nSession ended.")
        break

    # Retrieve relevant document chunks
    context = search_query(query)

    # Combine history with context
    full_context = chat_history + "\n" + context

    # Generate answer using LLM
    answer = generate_answer(full_context, query)

    # Save conversation history
    chat_history += f"\nUser: {query}\nAssistant: {answer}\n"

    print("\nAnswer:\n")
    print(answer)

    print("\n" + "-" * 60)
import os
import chromadb
from transformers import AutoTokenizer, AutoModel
import torch
from groq import Groq
import json

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection(name="pdf_collection")

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModel.from_pretrained("distilbert-base-uncased")

def generate_query_embedding(query):

    inputs = tokenizer(query, return_tensors="pt", truncation=True, padding=True, max_length=512)

    with torch.no_grad():

        outputs = model(**inputs)

    return outputs.last_hidden_state[:, 0, :].squeeze().numpy().tolist()

def store_products():
    
    with open('products.json', 'r') as f:
        products = json.loads(f.read())

    for index in range(len(products)):
        product = products[index]
        product_text = f"Name: {product.name}\nDescription: {product.description}\nUrl: {product.url}\nImage: {product.image}\nPrice: {product.price}\nAvailability: {product.availability}\nPower: {product.power}\nVoltage: {product.voltage}"
        embedding = generate_embeddings(product_text)
        collection.add(documents=[product_text], embeddings=[embedding], ids=[str(index)])

def generate_embeddings(text):
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    with torch.no_grad():
        outputs = model(**inputs)

    return outputs.last_hidden_state[:, 0, :].squeeze().numpy().tolist()

def generate_response_from_groq(context, query):
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Your task is to recommend products to user according to his/her query. You should not give any irrelevant information. You should only give relavant products."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {query}"}
            ],
            model="llama-3.1-70b-versatile"
        )
    return chat_completion.choices[0].message.content

def chatbot_response(user_query):
    """Generate a response based on the user's query."""
    query_embedding = generate_query_embedding(user_query)
    results = collection.query(query_embeddings=[query_embedding], n_results=1)
    if len(results['documents']) == 0:
        return "No relevant information found in the documents."
    retrieved_chunk = results['documents'][0]
    response = generate_response_from_groq(retrieved_chunk, user_query)
    return response
import google.generativeai as genai

genai.configure(api_key="AIzaSyDWS1SzYlYVEOMJ3mrogKmoqJ7Vs_vdLmA")  # Replace with your actual key

model = genai.GenerativeModel("models/gemini-1.5-flash")

def ask_gemini(question, image_context):
    prompt = f"""Here is a description of a diagram:\n{image_context}\n\nQuestion: {question}\nAnswer:"""
    response = model.generate_content(prompt)
    return response.text.strip()

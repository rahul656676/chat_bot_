from google import genai

# Your API Key
API_KEY = ""

# Initialize client
client = genai.Client(api_key=API_KEY)

try:
    # List all available models
    models = client.models.list()

    print("Available Models:\n")
    for model in models:
        # Display only models that support content generation
        if "generateContent" in model.supported_actions:
            print(model.name)

except Exception as e:
    print("Error:", e)
from google import genai

client = genai.Client(api_key="AIzaSyDpuDHRveo5utcw-nmybj4V-QlJfCRgNOs")

# This will list the models using the new SDK structure
for model in client.models.list():
    print(f"Model Name: {model.name}")
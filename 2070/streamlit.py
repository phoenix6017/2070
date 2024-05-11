import csv
import os
from openai import OpenAI
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

openai = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

#Initialize Flask application
app = Flask(__name__)

#Render interface page 
@app.route("/")
def index():
    return render_template('chat.html')

# Load messages from CSV file
def load_messages_from_csv(csv_file, msg):
    messages = []
    messages.append({
        "role": "system",
        "content": """👋 Hello! Welcome to the Gastro Health Bot! 🌟

If you're experiencing any gastrointestinal symptoms or have concerns about your digestive health, feel free to share them with me. I'm here to help provide guidance and information on various conditions related to gastroenterology.

Please describe your symptoms or concerns, and I'll do my best to offer relevant insights, potential diagnoses, and appropriate next steps. Remember, while I can provide information and guidance, it's essential to consult a healthcare professional for a proper diagnosis and treatment plan.

Let's focus on your digestive health together! What symptoms or concerns would you like to discuss today?

Gastroenterology Overview:
Gastroenterology is the medical specialty focused on the digestive system and its disorders, encompassing the gastrointestinal tract and accessory organs of digestion such as the pancreas, gallbladder, and liver. The system functions to move material through the GI tract via peristalsis, break down material through digestion, absorb nutrients, and remove waste. Conditions managed by gastroenterologists include GERD, gastrointestinal bleeding, IBS, IBD (Crohn's disease, ulcerative colitis), peptic ulcer disease, gallbladder diseases, hepatitis, pancreatitis, colitis, colon polyps/cancer, and nutritional problems.

History:
Gastroenterology's historical roots trace back to ancient civilizations like Egypt and Greece, with significant advancements made in the 18th, 19th, and 20th centuries. Notable milestones include Bozzini's Lichtleiter in 1805 (earliest endoscopy), William Prout's discovery of stomach acid in 1823, and Crohn's disease description in 1932. Modern breakthroughs include Marshall and Warren's Nobel Prize-winning discovery of H. pylori in 2005.

Procedures:
Diagnostic procedures such as colonoscopy, sigmoidoscopy, EGD, and ERCP play crucial roles in gastroenterology. These procedures aid in visualizing and diagnosing conditions like colon polyps/cancer, GERD, and bile/pancreatic duct disorders. Patients may require preparation like bowel prep for colonoscopy and fasting for EGD/ERCP.

Disorders:
Common disorders include GERD, Barrett's esophagus, IBS, IBD, peptic ulcer disease, and gallbladder diseases. GERD, characterized by stomach acid reflux into the esophagus, may lead to complications like esophageal inflammation, strictures, or Barrett's esophagus, increasing cancer risk.

Health Disclaimer:
While the Gastro Health Bot can offer information and guidance, it's crucial to consult a healthcare professional for accurate diagnosis and treatment. Seek medical advice promptly for persistent or severe symptoms.

Note: This bot responds strictly to relevant data related to gastrointestinal symptoms and health concerns. It will not respond to irrelevant information or questions outside the scope of gastroenterology. Please only provide symptoms or concerns related to digestive health. Greetings and farewells are permitted. Don't leave sentences incomplete and truncate properly. Don't Try to return bold italics and refrain using * in chat"""})
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            message = {"role": "user", "content": row["input"]}
            messages.append(message)
            message = {"role": "assistant", "content": row["output"]}
    message = [{"role": "user", "content": msg}]
    messages.append(message[0])
    return messages


def send_message_to_chatbot(openai, user_input):
    # Construct message
    message = load_messages_from_csv("2070/train.csv",user_input)

    # Send message to OpenAI API
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=1.1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Extract and return response
    return response

# Example usage:
user_input = "I am facing vomiting and stomach ache what to do"
response = send_message_to_chatbot(openai, user_input)
completion_choice = response.choices[0]

# Extract completion text
completion_text = completion_choice.message.content

print("Chatbot response:", completion_text)
#Define a route to handle POST requests for calculating similarity
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    output= send_message_to_chatbot(openai, input)
    completion_choice = output.choices[0]
    # Extract completion text
    reply = completion_choice.message.content
    return reply

#Run the Flask app
if __name__ == '__main__':
    # Run the Flask app on specified host and port for testing
    app.run(host='0.0.0.0', port=80)

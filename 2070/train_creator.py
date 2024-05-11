# # import pandas as pd
# # import random

# # #defining conditions for various diseases
# # conditions_symptoms = {
# #     "Gastroesophageal reflux disease (GERD)": {
# #         "symptoms": ["heartburn", "acid reflux", "regurgitation", "chest pain"],
# #         "triage_recommendation": "Triage recommendations for GERD: Consult a gastroenterologist. Lifestyle modifications, such as dietary changes and elevation of the head during sleep, may help. Medications like proton pump inhibitors (PPIs) or H2 blockers may be prescribed.",
# #         "diagnosis": "Diagnosis for GERD: Typically diagnosed based on symptoms, medical history, and response to treatment. Tests may include endoscopy, pH monitoring, or esophageal manometry."
# #     },
# #     "Inflammatory bowel disease (IBD)": {
# #         "symptoms": ["abdominal pain", "diarrhea", "bloody stools", "weight loss"],
# #         "triage_recommendation": "Triage recommendations for IBD: Urgent referral to a gastroenterologist for further evaluation. Treatment may include medications such as corticosteroids, immunomodulators, or biologics.",
# #         "diagnosis": "Diagnosis for IBD: Based on a combination of symptoms, physical examination, laboratory tests, endoscopy, and imaging studies like CT scans or MRI enterography."
# #     },
# #     "Irritable bowel syndrome (IBS)": {
# #         "symptoms": ["abdominal pain or discomfort", "bloating", "changes in bowel habits (diarrhea or constipation)"],
# #         "triage_recommendation": "Triage recommendations for IBS: Consultation with a gastroenterologist or primary care physician. Treatment focuses on symptom management through dietary changes, stress reduction, and medications such as antispasmodics or antidepressants.",
# #         "diagnosis": "Diagnosis for IBS: Based on the Rome criteria, which includes recurrent abdominal pain at least 1 day per week in the last 3 months associated with two or more of the following: improvement with defecation, onset associated with a change in frequency of stool, or onset associated with a change in form (appearance) of stool."
# #     },
# #     "Peptic ulcer disease": {
# #         "symptoms": ["burning stomach pain", "bloating", "nausea", "vomiting", "loss of appetite", "weight loss"],
# #         "triage_recommendation": "Triage recommendations for peptic ulcer disease: Consultation with a gastroenterologist or primary care physician. Treatment involves antibiotics to eradicate H. pylori infection (if present), proton pump inhibitors (PPIs), and avoidance of NSAIDs.",
# #         "diagnosis": "Diagnosis for peptic ulcer disease: Based on symptoms, medical history, and diagnostic tests such as upper endoscopy, H. pylori testing, or imaging studies."
# #     },
# #     "Gastritis": {
# #         "symptoms": ["upper abdominal pain or discomfort", "nausea", "vomiting", "loss of appetite", "bloating", "indigestion"],
# #         "triage_recommendation": "Triage recommendations for gastritis: Consultation with a gastroenterologist or primary care physician. Treatment may involve medications to reduce stomach acid (such as PPIs or H2 blockers), avoiding irritating foods, and lifestyle changes.",
# #         "diagnosis": "Diagnosis for gastritis: Based on symptoms, medical history, and diagnostic tests such as endoscopy, blood tests for H. pylori infection, or stool tests for occult blood."
# #     },
# #     "Gallstones": {
# #         "symptoms": ["abdominal pain (particularly in the upper right side)", "nausea", "vomiting", "fever", "jaundice"],
# #         "triage_recommendation": "Triage recommendations for gallstones: Consultation with a gastroenterologist or general surgeon. Treatment may involve watchful waiting, medications to dissolve stones, or surgical removal of the gallbladder.",
# #         "diagnosis": "Diagnosis for gallstones: Based on symptoms, medical history, and diagnostic tests such as ultrasound, CT scan, or cholescintigraphy (HIDA scan)."
# #     },
# #     "Pancreatitis": {
# #         "symptoms": ["severe abdominal pain", "nausea", "vomiting", "fever", "rapid pulse", "tenderness or swelling in the abdomen"],
# #         "triage_recommendation": "Triage recommendations for pancreatitis: Immediate medical attention is required. Consultation with a gastroenterologist or emergency department. Treatment involves hospitalization, intravenous fluids, pain management, and addressing the underlying cause.",
# #         "diagnosis": "Diagnosis for pancreatitis: Based on symptoms, physical examination, blood tests (elevated pancreatic enzymes), imaging studies like CT scan or MRI, and sometimes endoscopic retrograde cholangiopancreatography (ERCP)."
# #     },
# #     "Celiac disease": {
# #         "symptoms": ["digestive symptoms (diarrhea, abdominal pain, bloating)", "fatigue", "weight loss", "anemia", "osteoporosis", "skin rash (dermatitis herpetiformis)"],
# #         "triage_recommendation": "Triage recommendations for celiac disease: Consultation with a gastroenterologist. Diagnosis involves blood tests for specific antibodies and confirmation by small intestine biopsy.",
# #         "diagnosis": "Diagnosis for celiac disease: Based on blood tests (serology) to detect specific antibodies (such as anti-tissue transglutaminase antibodies or anti-endomysial antibodies) and confirmed by small intestine biopsy showing characteristic changes."
# #     },
# #     "Hepatitis": {
# #         "symptoms": ["fatigue", "nausea", "vomiting", "abdominal pain", "jaundice", "dark urine", "pale stools"],
# #         "triage_recommendation": "Triage recommendations for hepatitis: Consultation with a gastroenterologist or infectious disease specialist. Treatment depends on the type and severity of hepatitis and may involve antiviral medications, supportive care, or liver transplantation in severe cases.",
# #         "diagnosis": "Diagnosis for hepatitis: Based on blood tests to detect viral antigens or antibodies, liver function tests, imaging studies like ultrasound or CT scan, and sometimes liver biopsy."
# #     },
# #     "Diverticulitis": {
# #         "symptoms": ["abdominal pain (usually on the left side)", "fever", "nausea", "vomiting", "change in bowel habits", "bloody stools"],
# #         "triage_recommendation": "Triage recommendations for diverticulitis: Consultation with a gastroenterologist or primary care physician. Treatment may involve antibiotics, pain management, dietary changes (such as a clear liquid diet), and in severe cases, hospitalization.",
# #         "diagnosis": "Diagnosis for diverticulitis: Based on symptoms, physical examination, blood tests (such as complete blood count), and imaging studies like CT scan or abdominal ultrasound."
# #     },
# #     "Gastroenteritis": {
# #         "symptoms": ["diarrhea", "vomiting", "abdominal cramps", "nausea", "fever", "headache"],
# #         "triage_recommendation": "Triage recommendations for gastroenteritis: Most cases resolve on their own with home care. However, consultation with a healthcare provider may be needed if symptoms are severe, persistent, or if there are signs of dehydration.",
# #         "diagnosis": "Diagnosis for gastroenteritis: Usually based on symptoms. Laboratory tests or stool cultures may be done in severe cases or outbreaks to identify the causative organism."
# #     }
# #     # Add more conditions and associated information as needed
# # }



# # data = []
# # for condition, info in conditions_symptoms.items():
# #     symptoms = info["symptoms"]
# #     triage_recommendation = info["triage_recommendation"]
# #     diagnosis = info["diagnosis"]
# #     input_text = f"I'm experiencing symptoms like {', '.join(symptoms)}. What could it be?"
# #     output_text = f"Triage Recommendations: {triage_recommendation}. Diagnosis: {diagnosis}"
# #     data.append({"input": input_text, "output": output_text})

# # # Save the dataset to a file or use it for training directly

# # # General greetings and responses
# # general_greetings = ["Hello!", "Hi there!", "Hey!", "Good day!"]
# # general_responses = [
# #     "Hello! How can I assist you with your symptoms today?",
# #     "Hi! If you're experiencing any symptoms, feel free to describe them.",
# #     "Hey! I'm here to help you with any health concerns you may have.",
# #     "Good day! If you have any symptoms you'd like to discuss, feel free to share."
# # ]

# # # Add input-output pairs for general greetings and responses
# # for greeting, response in zip(general_greetings, general_responses):
# #     data.append({"input": greeting, "output": response})

# # # Multiple responses for "bye"
# # bye_responses = [
# #     "Goodbye! Take care.",
# #     "Goodbye! If you have any more questions, feel free to reach out.",
# #     "See you later! Wishing you good health.",
# #     "Farewell! Don't hesitate to come back if you need further assistance."
# # ]

# # # Add input-output pairs for "bye" and responses
# # for response in bye_responses:
# #     data.append({"input": "Bye!", "output": response})

# # # Multiple responses for "thanks"
# # thanks_responses = [
# #     "You're welcome! If you have any further questions, feel free to ask.",
# #     "No problem! Feel free to reach out if you need more information.",
# #     "Glad I could help! Don't hesitate to contact me if you have any other concerns.",
# #     "You're welcome! Remember, your health is important, so don't hesitate to seek medical advice if needed."
# # ]

# # # Add input-output pairs for "thanks" and responses
# # for response in thanks_responses:
# #     data.append({"input": "Thanks!", "output": response})

# # # Add more input-output pairs for irrelevant data
# # additional_irrelevant_data = [
# #     {"input": "What's the capital of New Zealand?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "How many continents are there in the world?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "Who wrote the play 'Romeo and Juliet'?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "What's the boiling point of water?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "How many bones are in the human body?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "Who discovered penicillin?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "What's the diameter of Earth?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "How many days are in a week?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "Who painted 'Starry Night'?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "What's the longest river in the world?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "What's the weather like today?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "Can you recommend a good restaurant?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "How tall is the Eiffel Tower?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "Tell me a joke.", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "What's your favorite color?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "What's the capital of New Zealand?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "How many continents are there in the world?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "Who wrote the play 'Romeo and Juliet'?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "What's the boiling point of water?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "How many bones are in the human body?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "Who discovered penicillin?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "What's the diameter of Earth?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "How many days are in a week?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "Who painted 'Starry Night'?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."},
# #     {"input": "What's the longest river in the world?", "output": "I'm sorry, I'm not equipped to respond to that. If you have any health-related questions, feel free to ask."}
# # ]

# # # Add to the existing data
# # data.extend(additional_irrelevant_data)

# # # Create DataFrame
# # df = pd.DataFrame(data)
# # path="C:/Users/Acer/Dropbox/My PC (LAPTOP-91U6NI9O)/Desktop/Comding/2070/train.csv"
# # df.to_csv('train.csv', index=False)
# import csv

# # Input-output pairs
# pairs = [
#     ("I have a stomach ache and nausea.", "It sounds like you may have gastritis. Avoid spicy and acidic foods and consider taking an antacid."),
#     ("My stool is black and tarry.", "Black, tarry stool could indicate gastrointestinal bleeding. Seek medical attention immediately."),
#     ("I experience frequent bloating and gas.", "Frequent bloating and gas could be a sign of irritable bowel syndrome (IBS). Consider dietary changes and stress management techniques."),
#     ("I have a burning sensation in my chest after eating.", "A burning sensation in the chest after eating could indicate gastroesophageal reflux disease (GERD). Avoid spicy, acidic, and fatty foods, and consider elevating the head of your bed."),
#     ("I've been having diarrhea for the past two days.", "Diarrhea lasting for more than a day could be a sign of a gastrointestinal infection. Stay hydrated and consider consulting a doctor if symptoms persist."),
#     ("I feel full quickly after eating small amounts of food.", "Feeling full quickly after eating small amounts of food could be a symptom of gastroparesis. Eat smaller, more frequent meals and avoid high-fiber foods."),
#     ("I'm experiencing sharp, stabbing pains in my abdomen.", "Sharp, stabbing pains in the abdomen could indicate a variety of conditions, including appendicitis or gallstones. Seek medical attention immediately."),
#     ("I've noticed blood in my stool.", "Blood in the stool could be a sign of colorectal cancer or hemorrhoids. It's essential to see a doctor for further evaluation."),
#     ("I've been experiencing persistent heartburn.", "Persistent heartburn could be a symptom of GERD or peptic ulcer disease. Avoid trigger foods and consider over-the-counter medications or prescription treatments."),
#     ("I have a family history of Crohn's disease.", "A family history of Crohn's disease increases your risk of developing the condition. Be aware of symptoms such as abdominal pain, diarrhea, and weight loss, and consult a doctor if necessary."),
#     ("I feel extremely fatigued and have lost my appetite.", "Extreme fatigue and loss of appetite could be symptoms of several gastrointestinal conditions, including celiac disease or inflammatory bowel disease. Consult a doctor for evaluation and diagnosis."),
#     ("I've been experiencing chronic constipation.", "Chronic constipation could be a sign of underlying issues such as irritable bowel syndrome (IBS) or a thyroid disorder. Increase fiber intake, stay hydrated, and consider over-the-counter laxatives or prescription medications."),
#     ("I feel nauseous and have been vomiting.", "Nausea and vomiting can be symptoms of various gastrointestinal conditions, including gastroenteritis or food poisoning. Stay hydrated and consult a doctor if symptoms persist."),
#     ("I have a persistent cough and hoarseness.", "A persistent cough and hoarseness could be symptoms of gastroesophageal reflux disease (GERD) or aspiration pneumonia. Consult a doctor for evaluation and treatment."),
#     ("I've been experiencing excessive gas and belching.", "Excessive gas and belching could be a sign of swallowing air or underlying gastrointestinal conditions such as GERD or lactose intolerance. Avoid carbonated beverages and gas-producing foods."),
#     ("I have sharp, stabbing pains in my lower abdomen.", "Sharp, stabbing pains in the lower abdomen could indicate conditions such as diverticulitis or ovarian cysts. Seek medical attention for proper diagnosis and treatment."),
#     ("I've been feeling bloated and have noticed changes in my bowel habits.", "Feeling bloated and experiencing changes in bowel habits could be symptoms of irritable bowel syndrome (IBS). Keep a food diary and consider stress management techniques."),
#     ("I have a persistent, dry cough.", "A persistent, dry cough could be a symptom of gastroesophageal reflux disease (GERD) or laryngopharyngeal reflux (LPR). Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I've been experiencing difficulty swallowing.", "Difficulty swallowing, also known as dysphagia, could indicate a variety of conditions, including GERD, esophageal strictures, or esophageal cancer. Seek medical attention for proper evaluation and diagnosis."),
#     ("I've been experiencing difficulty breathing and chest pain.", "Difficulty breathing and chest pain could be symptoms of a serious condition such as a heart attack or pulmonary embolism. Seek emergency medical attention immediately."),
#     ("I feel a lump or mass in my abdomen.", "Feeling a lump or mass in the abdomen could indicate a variety of conditions, including abdominal hernias or tumors. Consult a doctor for evaluation and diagnosis."),
#     ("I've been experiencing persistent indigestion and bloating.", "Persistent indigestion and bloating could be symptoms of dyspepsia or gastroesophageal reflux disease (GERD). Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I have a sharp, burning pain in my upper abdomen.", "A sharp, burning pain in the upper abdomen could indicate peptic ulcer disease or gallbladder issues. Seek medical attention for proper evaluation and treatment."),
#     ("I've been feeling dizzy and lightheaded.", "Feeling dizzy and lightheaded could be symptoms of dehydration or anemia, which can be associated with gastrointestinal bleeding. Seek medical attention if symptoms persist."),
#     ("I feel a constant, dull ache in my abdomen.", "A constant, dull ache in the abdomen could indicate underlying issues such as constipation or abdominal muscle strain. Consult a doctor for proper evaluation and management."),
#     ("I've been experiencing persistent diarrhea and weight loss.", "Persistent diarrhea and unexplained weight loss could be symptoms of conditions such as inflammatory bowel disease (IBD) or malabsorption disorders. Consult a doctor for evaluation and diagnosis."),
#     ("I have a persistent sore throat and difficulty swallowing.", "A persistent sore throat and difficulty swallowing could be symptoms of conditions such as GERD or throat cancer. Seek medical attention for proper evaluation and treatment."),
#     ("I've been experiencing frequent heartburn and regurgitation.", "Frequent heartburn and regurgitation could be symptoms of gastroesophageal reflux disease (GERD). Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I have a chronic cough and hoarseness.", "A chronic cough and hoarseness could be symptoms of gastroesophageal reflux disease (GERD) or laryngopharyngeal reflux (LPR). Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I've been experiencing severe abdominal pain and bloating.", "Severe abdominal pain and bloating could be symptoms of conditions such as appendicitis or intestinal obstruction. Seek emergency medical attention immediately."),
#     ("I have a persistent feeling of fullness and nausea after eating.", "Persistent feeling of fullness and nausea after eating could indicate conditions such as gastroparesis or gallbladder issues. Consult a doctor for proper evaluation and management."),
#     ("I've been feeling extremely fatigued and have lost my appetite.", "Extreme fatigue and loss of appetite could be symptoms of several gastrointestinal conditions, including celiac disease or chronic liver disease. Consult a doctor for evaluation and diagnosis."),
#     ("I have a persistent, burning pain in my stomach after eating.", "A persistent, burning pain in the stomach after eating could be a sign of gastritis or peptic ulcer disease. Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I've been feeling extremely bloated and have noticed changes in my bowel habits.", "Feeling extremely bloated and experiencing changes in bowel habits could be symptoms of conditions such as irritable bowel syndrome (IBS) or lactose intolerance. Consult a doctor for evaluation and diagnosis."),
#     ("I feel nauseous and have been experiencing abdominal pain and diarrhea.", "Nausea, abdominal pain, and diarrhea could be symptoms of conditions such as food poisoning or gastroenteritis. Stay hydrated and consult a doctor if symptoms persist."),
#     ("I have a persistent feeling of discomfort and fullness in my abdomen.", "A persistent feeling of discomfort and fullness in the abdomen could indicate conditions such as bloating or constipation. Maintain a healthy diet and consider lifestyle changes or medications."),
#     ("I've been experiencing persistent heartburn and acid reflux.", "Persistent heartburn and acid reflux could be symptoms of gastroesophageal reflux disease (GERD). Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I feel nauseous and have been vomiting blood.", "Nausea and vomiting blood could be symptoms of serious conditions such as gastrointestinal bleeding or peptic ulcer disease. Seek emergency medical attention immediately."),
#     ("I've been experiencing severe abdominal pain and have noticed blood in my stool.", "Severe abdominal pain and blood in the stool could indicate conditions such as gastrointestinal bleeding or inflammatory bowel disease (IBD). Seek emergency medical attention immediately."),
#     ("I have a persistent, burning pain in my chest that worsens when lying down.", "A persistent, burning pain in the chest that worsens when lying down could be a symptom of gastroesophageal reflux disease (GERD) or a hiatal hernia. Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I've been feeling extremely tired and weak, and my skin and eyes appear yellowish.", "Feeling extremely tired and weak, along with yellowing of the skin and eyes (jaundice), could be symptoms of liver disease or gallbladder issues. Consult a doctor for evaluation and diagnosis."),
#     ("I have a persistent, gnawing pain in my upper abdomen that improves after eating.", "A persistent, gnawing pain in the upper abdomen that improves after eating could be a sign of peptic ulcer disease. Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I've been experiencing persistent abdominal discomfort and changes in bowel habits.", "Persistent abdominal discomfort and changes in bowel habits could be symptoms of conditions such as irritable bowel syndrome (IBS) or inflammatory bowel disease (IBD). Consult a doctor for evaluation and diagnosis."),
#     ("I feel nauseous and have been experiencing frequent burping and bloating.", "Nausea, frequent burping, and bloating could be symptoms of conditions such as GERD or dyspepsia. Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I have a persistent, burning pain in my throat and chest, especially after eating.", "A persistent, burning pain in the throat and chest, especially after eating, could be a symptom of gastroesophageal reflux disease (GERD) or laryngopharyngeal reflux (LPR). Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I've been experiencing persistent abdominal pain and cramping, along with changes in bowel habits.", "Persistent abdominal pain and cramping, along with changes in bowel habits, could be symptoms of conditions such as inflammatory bowel disease (IBD) or diverticulitis. Consult a doctor for evaluation and diagnosis."),
#     ("I feel nauseous and have been experiencing persistent abdominal discomfort and bloating.", "Nausea, persistent abdominal discomfort, and bloating could be symptoms of conditions such as gastroesophageal reflux disease (GERD) or gastroparesis. Avoid trigger foods and consider lifestyle changes or medications."),
#     ("I have a constant feeling of fullness in my abdomen and have noticed weight loss.", "A constant feeling of fullness in the abdomen, along with weight loss, could be symptoms of conditions such as stomach cancer or pancreatic cancer. Consult a doctor for evaluation and diagnosis."),
#     ("I've been feeling extremely fatigued and have noticed a yellowish tint to my skin and eyes.", "Feeling extremely fatigued and noticing a yellowish tint to the skin and eyes (jaundice) could be symptoms of liver disease or bile duct obstruction. Seek medical attention for proper evaluation and diagnosis.")
# ]

# # Define the CSV file path
# csv_file = path="C:/Users/Acer/Dropbox/My PC (LAPTOP-91U6NI9O)/Desktop/Comding/2070/rain.csv"

# # Write input-output pairs to CSV file
# with open(csv_file, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     # Write header
#     writer.writerow(['input', 'output'])
#     # Write input-output pairs
#     writer.writerows(pairs)

# print("CSV file has been created successfully.")
import csv

# Input-output pairs
pairs = [
    ("I have a stomach ache and nausea.", "It sounds like you may have gastritis. Avoid spicy and acidic foods and consider taking an antacid."),
    ("My stool is black and tarry.", "Black, tarry stool could indicate gastrointestinal bleeding. Seek medical attention immediately."),
    ("I experience frequent bloating and gas.", "Frequent bloating and gas could be a sign of irritable bowel syndrome (IBS). Consider dietary changes and stress management techniques."),
    ("I have a burning sensation in my chest after eating.", "A burning sensation in the chest after eating could indicate gastroesophageal reflux disease (GERD). Avoid spicy, acidic, and fatty foods, and consider elevating the head of your bed."),
    ("I've been having diarrhea for the past two days.", "Diarrhea lasting for more than a day could be a sign of a gastrointestinal infection. Stay hydrated and consider consulting a doctor if symptoms persist."),
    ("I feel full quickly after eating small amounts of food.", "Feeling full quickly after eating small amounts of food could be a symptom of gastroparesis. Eat smaller, more frequent meals and avoid high-fiber foods."),
    ("I'm experiencing sharp, stabbing pains in my abdomen.", "Sharp, stabbing pains in the abdomen could indicate a variety of conditions, including appendicitis or gallstones. Seek medical attention immediately."),
    ("I've noticed blood in my stool.", "Blood in the stool could be a sign of colorectal cancer or hemorrhoids. It's essential to see a doctor for further evaluation."),
    ("I've been experiencing persistent heartburn.", "Persistent heartburn could be a symptom of GERD or peptic ulcer disease. Avoid trigger foods and consider over-the-counter medications or prescription treatments."),
    ("I have a family history of Crohn's disease.", "A family history of Crohn's disease increases your risk of developing the condition. Be aware of symptoms such as abdominal pain, diarrhea, and weight loss, and consult a doctor if necessary."),
    ("I feel extremely fatigued and have lost my appetite.", "Extreme fatigue and loss of appetite could be symptoms of several gastrointestinal conditions, including celiac disease or inflammatory bowel disease. Consult a doctor for evaluation and diagnosis."),
    ("I've been experiencing chronic constipation.", "Chronic constipation could be a sign of underlying issues such as irritable bowel syndrome (IBS) or a thyroid disorder. Increase fiber intake, stay hydrated, and consider over-the-counter laxatives or prescription medications."),
    ("I feel nauseous and have been vomiting.", "Nausea and vomiting can be symptoms of various gastrointestinal conditions, including gastroenteritis or food poisoning. Stay hydrated and consult a doctor if symptoms persist."),
    ("I have a persistent cough and hoarseness.", "A persistent cough and hoarseness could be symptoms of gastroesophageal reflux disease (GERD) or aspiration pneumonia. Consult a doctor for evaluation and treatment."),
    ("I've been experiencing excessive gas and belching.", "Excessive gas and belching could be a sign of swallowing air or underlying gastrointestinal conditions such as GERD or lactose intolerance. Avoid carbonated beverages and gas-producing foods."),
    ("I have sharp, stabbing pains in my lower abdomen.", "Sharp, stabbing pains in the lower abdomen could indicate conditions such as diverticulitis or ovarian cysts. Seek medical attention for proper diagnosis and treatment."),
    ("I've been feeling bloated and have noticed changes in my bowel habits.", "Feeling bloated and experiencing changes in bowel habits could be symptoms of irritable bowel syndrome (IBS). Keep a food diary and consider stress management techniques."),
    ("I have a persistent, dry cough.", "A persistent, dry cough could be a symptom of gastroesophageal reflux disease (GERD) or laryngopharyngeal reflux (LPR). Avoid trigger foods and consider lifestyle changes or medications."),
    ("I've been experiencing difficulty swallowing.", "Difficulty swallowing, also known as dysphagia, could indicate a variety of conditions, including GERD, esophageal strictures, or esophageal cancer. Seek medical attention for proper evaluation and diagnosis."),
    ("I've been experiencing difficulty breathing and chest pain.", "Difficulty breathing and chest pain could be symptoms of a serious condition such as a heart attack or pulmonary embolism. Seek emergency medical attention immediately."),
    ("I feel a lump or mass in my abdomen.", "Feeling a lump or mass in the abdomen could indicate a variety of conditions, including abdominal hernias or tumors. Consult a doctor for evaluation and diagnosis."),
    ("I've been experiencing persistent indigestion and bloating.", "Persistent indigestion and bloating could be symptoms of dyspepsia or gastroesophageal reflux disease (GERD). Avoid trigger foods and consider lifestyle changes or medications."),
    ("I have a sharp, burning pain in my upper abdomen.", "A sharp, burning pain in the upper abdomen could indicate peptic ulcer disease or gallbladder issues. Seek medical attention for proper evaluation and treatment."),
    ("I've been feeling dizzy and lightheaded.", "Feeling dizzy and lightheaded could be symptoms of dehydration or anemia, which can be associated with gastrointestinal bleeding. Seek medical attention if symptoms persist."),
    ("I feel a constant, dull ache in my abdomen.", "A constant, dull ache in the abdomen could indicate underlying issues such as constipation or abdominal muscle strain. Consult a doctor for proper evaluation and management."),
    ("I've been experiencing persistent diarrhea and weight loss.", "Persistent diarrhea and unexplained weight loss could be symptoms of conditions such as inflammatory bowel disease (IBD) or malabsorption disorders. Consult a doctor for evaluation and diagnosis."),
    ("I have a persistent sore throat and difficulty swallowing.", "A persistent sore throat and difficulty swallowing could be symptoms of conditions such as GERD or throat cancer. Seek medical attention for proper evaluation and treatment."),
    ("I've been experiencing frequent heartburn and regurgitation.", "Frequent heartburn and regurgitation could be symptoms of gastroesophageal reflux disease (GERD). Avoid trigger foods and consider lifestyle changes or medications."),
    ("I have a chronic cough and hoarseness.", "A chronic cough and hoarseness could be symptoms of gastroesophageal reflux disease (GERD) or laryngopharyngeal reflux (LPR). Avoid trigger foods and consider lifestyle changes or medications."),
    ("I've been experiencing severe abdominal pain and bloating.", "Severe abdominal pain and bloating could be symptoms of conditions such as appendicitis or intestinal obstruction. Seek emergency medical attention immediately."),
    ("I have a persistent feeling of fullness and nausea after eating.", "Persistent feeling of fullness and nausea after eating could indicate conditions such as gastroparesis or gallbladder issues. Consult a doctor for proper evaluation and management."),
    ("I've been feeling extremely fatigued and have lost my appetite.", "Extreme fatigue and loss of appetite could be symptoms of several gastrointestinal conditions, including celiac disease or chronic liver disease. Consult a doctor for evaluation and diagnosis."),
    ("I have a persistent, burning pain in my stomach after eating.", "A persistent, burning pain in the stomach after eating could be a sign of gastritis or peptic ulcer disease. Avoid trigger foods and consider lifestyle changes or medications."),
    ("I've been feeling extremely bloated and have noticed changes in my bowel habits.", "Feeling extremely bloated and experiencing changes in bowel habits could be symptoms of conditions such as irritable bowel syndrome (IBS) or lactose intolerance. Consult a doctor for evaluation and diagnosis."),
    ("I feel nauseous and have been experiencing abdominal pain and diarrhea.", "Nausea, abdominal pain, and diarrhea could be symptoms of conditions such as food poisoning or gastroenteritis. Stay hydrated and consult a doctor if symptoms persist."),
    ("I have a persistent feeling of discomfort and fullness in my abdomen.", "A persistent feeling of discomfort and fullness in the abdomen could indicate conditions such as bloating or constipation. Maintain a healthy diet and consider lifestyle changes or medications."),
    ("I've been experiencing persistent heartburn and acid reflux.", "Persistent heartburn and acid reflux could be symptoms of gastroesophageal reflux disease (GERD). Avoid trigger foods and consider lifestyle changes or medications."),
    ("I feel nauseous and have been vomiting blood.", "Nausea and vomiting blood could be symptoms of serious conditions such as gastrointestinal bleeding or peptic ulcer disease. Seek emergency medical attention immediately."),
    ("I've been experiencing severe abdominal pain and have noticed blood in my stool.", "Severe abdominal pain and blood in the stool could indicate conditions such as gastrointestinal bleeding or inflammatory bowel disease (IBD). Seek emergency medical attention immediately."),
    ("I have a persistent, burning pain in my chest that worsens when lying down.", "A persistent, burning pain in the chest that worsens when lying down could be a symptom of gastroesophageal reflux disease (GERD) or a hiatal hernia. Avoid trigger foods and consider lifestyle changes or medications."),
    ("I've been feeling extremely tired and weak, and my skin and eyes appear yellowish.", "Feeling extremely tired and weak, along with yellowing of the skin and eyes (jaundice), could be symptoms of liver disease or gallbladder issues. Consult a doctor for evaluation and diagnosis."),
    ("I have a persistent, gnawing pain in my upper abdomen that improves after eating.", "A persistent, gnawing pain in the upper abdomen that improves after eating could be a sign of peptic ulcer disease. Avoid trigger foods and consider lifestyle changes or medications."),
    ("I've been experiencing persistent abdominal discomfort and changes in bowel habits.", "Persistent abdominal discomfort and changes in bowel habits could be symptoms of conditions such as irritable bowel syndrome (IBS) or inflammatory bowel disease (IBD). Consult a doctor for evaluation and diagnosis."),
    ("I feel nauseous and have been experiencing frequent burping and bloating.", "Nausea, frequent burping, and bloating could be symptoms of conditions such as GERD or dyspepsia. Avoid trigger foods and consider lifestyle changes or medications."),
    ("I have a persistent, burning pain in my throat and chest, especially after eating.", "A persistent, burning pain in the throat and chest, especially after eating, could be a symptom of gastroesophageal reflux disease (GERD) or laryngopharyngeal reflux (LPR). Avoid trigger foods and consider lifestyle changes or medications."),
    ("I've been experiencing persistent abdominal pain and cramping, along with changes in bowel habits.", "Persistent abdominal pain and cramping, along with changes in bowel habits, could be symptoms of conditions such as inflammatory bowel disease (IBD) or diverticulitis. Consult a doctor for evaluation and diagnosis."),
    ("I feel nauseous and have been experiencing persistent abdominal discomfort and bloating.", "Nausea, persistent abdominal discomfort, and bloating could be symptoms of conditions such as gastroesophageal reflux disease (GERD) or gastroparesis. Avoid trigger foods and consider lifestyle changes or medications."),
    ("I have a constant feeling of fullness in my abdomen and have noticed weight loss.", "A constant feeling of fullness in the abdomen, along with weight loss, could be symptoms of conditions such as stomach cancer or pancreatic cancer. Consult a doctor for evaluation and diagnosis."),
    ("I've been feeling extremely fatigued and have noticed a yellowish tint to my skin and eyes.", "Feeling extremely fatigued and noticing a yellowish tint to the skin and eyes (jaundice) could be symptoms of liver disease or bile duct obstruction. Seek medical attention for proper evaluation and diagnosis.")
]

# Define the CSV file path
csv_file = path="C:/Users/Acer/Dropbox/My PC (LAPTOP-91U6NI9O)/Desktop/Comding/2070/ra.csv"

# Write input-output pairs to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(['input', 'output'])
    # Write input-output pairs
    writer.writerows(pairs)

print("CSV file has been created successfully.")

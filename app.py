# Import required libraries
from flask import Flask, render_template, request, jsonify
# Create Flask app
app = Flask(__name__)

intents = {
    "admission": {
        "keywords": ["admission", "apply", "enroll", "join"],
        "response": "Admissions are based on merit. Please fill the online admission form."
    },
    "courses": {
        "keywords": ["course", "program", "degree", "study"],
        "response": "We offer BCA, BBA, B.Sc, MCA and MBA courses."
    },
    "fees": {
        "keywords": ["fee", "tuition", "cost", "price"],
        "response": "The fee structure varies by course. For example, BCA starts from ₹45,000 per year, BBA starts from ₹35,000, B.Sc starts from ₹60,000 per year, MCA starts from ₹1,10,000 per year and MBA starts from ₹90,000 per year."
    },
    "contact": {
        "keywords": ["contact", "phone", "email", "reach"],
        "response": "You can contact us at +91-9876543210 or email abc@college.edu"
    },
    "greeting": {
        "keywords": ["hello", "hi", "hey"],
        "response": "Hello! How can I assist you today?"
    },
    "thanks": {
        "keywords": ["thank you", "thanks", "appreciate"],
        "response": "You're welcome! If you have any more questions, feel free to ask."
    },
    "help": {
        "keywords": ["help", "assist", "support"],
        "response": "Sure! You can ask me about courses, admission, fees, or contact information."
    
    },
    "about": {
        "keywords": ["who are you", "what are you", "about"],
        "response": "I am a virtual assistant here to help you with information about our college."         
    },
    "hours": {
        "keywords": ["hours", "open", "timing", "time"],
        "response": "Our college is open from 9 AM to 5 PM, Monday to Friday."
    },
    "location": {
        "keywords": ["location", "where", "address", "place"],
        "response": "We are located at 123 College Street, Mumbai, India."
    },
    "events": {
        "keywords": ["events", "activities", "happenings", "programs"],
        "response": "We host various events throughout the year including cultural fests, sports meets, and seminars."
    },
    "scholarships": {
        "keywords": ["scholarships","scholarship" "financial aid", "grant", "funding"],
        "response": "We offer several scholarships based on merit and need. Please visit our scholarships page for more details."
    },
    "goodbye": {
        "keywords": ["bye", "goodbye", "see you", "farewell"],
        "response": "Goodbye! Have a great day!"
    },
     "hospitality": {
        "keywords": ["food", "canteen", "mess", "dining"],
        "response": "Our college provides a variety of food options in the canteen, including vegetarian and non-vegetarian meals."
    },
    "hostel": {
        "keywords": ["hostel", "accommodation", "stay", "residence"],
        "response": "We have separate hostels for boys and girls with all necessary facilities." 
    },
    "saturday": {
        "keywords": ["saturday","sunday", "weekend", "holiday"],
        "response": "Our college remains closed on 2nd Saturdays and Sundays."
    },

}

responses = {
    "courses": "We offer BCA, BBA, B.Sc, MCA and MBA courses.",
    "admission": "Admissions are based on merit. Fill the online form and submit documents.",
    "fees": "Fee structure varies by course. BCA starts from ₹45,000 per year, BBA starts from ₹35,000, B.Sc starts from ₹60,000 per year, MCA starts from ₹1,10,000 per year and MBA starts from ₹90,000 per year.",
    "contact": "You can contact us at +91-9876543210 or email abc@college.edu",
    "default": "Sorry, I didn't understand. Please ask about admission, courses, fees or contact."
}

@app.route("/")
def index():
    return render_template("index.html")
# Route for chatbot response
@app.route("/chat", methods=["POST"])
def chat():
    import re

    user_message = request.json["message"].lower()

    # 🔹 Remove punctuation
    user_message = re.sub(r"[^\w\s]", "", user_message)

    # 🔹 Split sentence into words
    words = user_message.split()

    # 🔹 Match keywords inside sentence
    for intent in intents.values():
        for keyword in intent["keywords"]:
            if keyword in words or keyword in user_message:
                return jsonify({"reply": intent["response"]})

    return jsonify({"reply": "Sorry, I didn't understand. Please ask about admission, courses, fees, or contact."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)




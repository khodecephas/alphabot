import json
import random

# Base templates per tag
tags = {
    "greeting": [
        "hello", "hi", "good morning", "hey", "howdy", "yo", "good afternoon", "good evening", 
        "hi AlphaBot", "hello there"
    ],
    "registration": [
        "when will registration start", "course registration", "registration deadline", 
        "how do I register for courses", "registration portal", "course signup", 
        "register for new semester", "registration process"
    ],
    "exam": [
        "when are exams starting", "exam timetable", "exam date", "exam schedule", 
        "exam portal", "final exams", "midterm exams"
    ],
    "fees": [
        "how do I pay school fees", "school fees payment", "pay my fees", "tuition fees", 
        "fees portal", "pay tuition", "school fees details"
    ],
    "faculty_location": [
        "where is the faculty of computing", "location of faculty of computing", 
        "faculty location", "where is my faculty", "campus location"
    ],
    "post_utme": [
        "post utme registration", "how to register for post utme", "post utme portal", 
        "post utme info", "apply for post utme"
    ],
    "results": [
        "check my results", "where can I see my results", "results portal", "exam results"
    ],
    "admission": [
        "admission letter", "how to download admission letter", "admission portal"
    ],
    "hostel": [
        "hostel application", "apply for hostel", "hostel registration", "where is hostel portal"
    ],
    "news": [
        "any news about the school", "latest news", "updates from NAUB", "news portal"
    ],
    "thanks": [
        "thanks", "thank you", "thank you so much", "thanks a lot"
    ],
    "website": [
        "main website", "official site", "naub homepage", "school website"
    ],
    "help": [
        "help me", "I need assistance", "support", "how do I do this", "can you help me"
    ]
}

# Base responses per tag
responses = {
    "greeting": [
        "Hello! Welcome to AlphaBot, your friendly NAUB student assistant.",
        "Hi there! How can I help you today? 😊",
        "Hey! How’s it going? I'm here to help with all NAUB info."
    ],
    "registration": [
        "Course registration usually starts at the beginning of the semester. Check the NAUB portal for exact dates: https://naub.edu.ng/registration",
        "You can register online via the registration portal: https://naub.edu.ng/registration"
    ],
    "exam": [
        "Exams usually begin at the end of the semester. See the academic calendar: https://naub.edu.ng/exams",
        "Check your exam schedule here: https://naub.edu.ng/exams"
    ],
    "fees": [
        "School fees can be paid through the NAUB portal or approved banks: https://naub.edu.ng/fees. Make sure to pay on time!",
        "Tuition details and payment portal: https://naub.edu.ng/fees"
    ],
    "faculty_location": [
        "The Faculty of Computing is located on the main campus, beside the library.",
        "You can find your faculty location here: https://naub.edu.ng/faculties"
    ],
    "post_utme": [
        "POST UTME registration is available here: https://naub.edu.ng/post-utme. Register early to avoid last-minute issues!"
    ],
    "results": [
        "Check your results here: https://naub.edu.ng/results. Login with your student ID."
    ],
    "admission": [
        "Download your admission letter here: https://naub.edu.ng/admission. Have your JAMB number ready."
    ],
    "hostel": [
        "Hostel application info: https://naub.edu.ng/hostel. Apply early!"
    ],
    "news": [
        "The latest news: NAUB launched a new digital library. Check here: https://naub.edu.ng/news",
        "Stay updated with school news: https://naub.edu.ng/news"
    ],
    "thanks": [
        "You're welcome! 😊", "No problem!", "Happy to help!"
    ],
    "website": [
        "Official NAUB website: https://naub.edu.ng"
    ],
    "help": [
        "Sure! Ask me anything about NAUB student life, portals, fees, or exams."
    ]
}

intents = {"intents": []}

# Generate 10,000+ patterns/responses
for tag, base_patterns in tags.items():
    tag_intent = {"tag": tag, "patterns": [], "responses": responses[tag]}
    for i in range(1000):  # 1000 variations per tag
        # pick random base pattern and add a small variation
        pattern = random.choice(base_patterns)
        # add random suffix/prefix for variety
        prefix = random.choice(["", "Hey, ", "Can you tell me ", "Please, "])
        suffix = random.choice(["?", "", " please", " asap"])
        full_pattern = f"{prefix}{pattern}{suffix}"
        tag_intent["patterns"].append(full_pattern)
    intents["intents"].append(tag_intent)

# Save JSON file
with open("intents.json", "w") as f:
    json.dump(intents, f, indent=2)

print("✅ Generated intents.json with 10,000+ friendly entries!")
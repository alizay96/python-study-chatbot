import random
from datetime import datetime

print("✨ Smart Study Bot Activated ✨")
print("Type 'bye' anytime to exit.\n")

chat_responses = {
    "hello": [
        "Hey there 😭",
        "Hellooo 💀",
        "Hi! Ready to be productive? 😎"
    ],

    "how are you": [
        "I'm doing great 😭",
        "Doing amazing 💀",
        "Ready to help you study 😎"
    ],

    "I am sad": [
        "Bad days don't last forever 😭",
        "Take a deep breath 💀",
        "You're stronger than you think 😎"
    ],

    "motivate me": [
        "Your future self will thank you 😭",
        "Small progress matters 💀",
        "Keep building your dream life 😎"
    ]
}

study_tips = [
    "Study for 25 minutes, then take a 5 minute break 😭",
    "Put your phone away while studying 💀",
    "Write short notes while learning 😎",
    "Consistency beats motivation 😭"
]

subjects = {
    "python": "Practice small projects daily 😎",
    "math": "Solve problems step by step 😭",
    "english": "Read and speak regularly 💀",
    "computer": "Focus on concepts, not memorizing 😎"
    "islamiyat": "Practice the arabic verses ♥👍"
}
while True:

    user = input("\nYou: ").lower()

    # EXIT
    if user == "bye":
        print("Bot: Byeee 😭 Keep glowing up 💀")
        break

    # TIME
    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # STUDY HELP
    elif user == "study":
        print("Bot:", random.choice(study_tips))

    # SUBJECT HELP
    elif user in subjects:
        print("Bot:", subjects[user])

    # NORMAL CHAT
    elif user in chat_responses:
        print("Bot:", random.choice(chat_responses[user]))

    # UNKNOWN
    else:
        print("Bot: I don't understand that yet 😭")
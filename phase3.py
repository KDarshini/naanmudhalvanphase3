# Import the necessary libraries
import random

# Define chatbot responses and a basic persona
responses = {
    "greetings": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
    "recommendations": {
        "restaurants": {
            "Italian": ["Carlo's Trattoria is a great Italian restaurant in Manhattan.", "You should try L'A more Italian Restaurant for a special Italian dining experience."],
            "Mexican": ["For Mexican food, try Casa de Amigos. It's a popular choice in the city.", "Mexican Food Haven in SoHo is known for its authentic flavours."],
        },
        "hotels": {
            "budget": ["The Budget Inn is an affordable hotel with good ratings.", "Check out the Traveler's Lodge for budget-friendly options."],
            "luxury": ["For a luxury stay, you can't go wrong with The Grand Hotel.", "The Riverview Suites offers a premium experience in the heart of the city."],
        },
    },
    "goodbye": ["You're welcome! If you have more questions, feel free to ask. Have a great day!", "If you need further assistance, don't hesitate to reach out. Enjoy your trip!"]
}

# Define the chatbot function
def chatbot ():
    print(random.ch(responses["greetings"])) 
 # Greet the user

    while True:
        user = input ("You: ") 
 # Get user input

        if "recommendations" in user:
            print ("Sure, I can help with recommendations. What type of recommendations are you looking for? (e.g., restaurants, hotels)")
            category = input ("You: ")

            if category in responses["recommendations"]:
                print (Great choice! For {category}, what kind of {category} are you interested in? (e.g., Italian, Mexican)")
                subcategory = input ("You: ")

                if subcategory in responses["recommendations"] [category]:
                       print(random.ch(responses["recommendations"][category][subcategory]))
                else:
                    print ("I'm sorry, I don't have information on that specific subcategory.")
            else:
                print ("I'm sorry, I can't provide recommendations for that category.")

        elif "goodbye" in user:
            print (random.ch(responses["goodbye"]))
            break

        else:
            print ("I'm sorry, I don't understand. You can ask for recommendations or say goodbye.")

# Run the chatbot
Chatbot ()
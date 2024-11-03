import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to get voice input from the user
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
            return "None"
        except sr.RequestError:
            speak("Network error. Please check your internet connection.")
            return "None"


# Function to respond to basic commands
def respond(query):
    if "hello" in query:
        speak("Hello! How can I assist you today?")

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "search" in query:
        speak("What would you like to search for?")
        search_query = listen()
        if search_query != "None":
            speak(f"Searching for {search_query} on the web.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

    else:
        speak("I can only help with basic tasks right now. Please try again.")


# Main loop for the assistant
def main():
    speak("Welcome! Say 'hello' to start.")
    while True:
        command = listen()
        if command == "None":
            continue
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break
        respond(command)


if __name__ == "__main__":
    main()

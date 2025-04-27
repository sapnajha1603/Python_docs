import pyttsx3

engine = pyttsx3.init()

# List available voices
voices = engine.getProperty('voices')
print("Available voices:")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} - {voice.id}")

# Select a voice by index (change the index as needed)
selected_voice_index = 1  # for example, choose the second voice in the list
engine.setProperty('voice', voices[selected_voice_index].id)

# Speak the text with the selected voice
engine.say("Tanmay is a good boy and tanisha is a good girl and didi is also a good girl")
engine.runAndWait()

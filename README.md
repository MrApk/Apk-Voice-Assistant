# Apk assistant 🎤🤖

This is a simple voice assistant that listens to user input through the microphone, sends the input to a chatbot API, and plays back the response using text-to-speech.

## Installation 🚀

- Install the required Python packages:
```bash
pip install -r requirements.txt
```
or
```bash
pip install speechrecognition pyttsx3 requests datetime wikipedia
```


## Usage ℹ️

1. Run the `main.py` file.
2. Speak into the microphone to ask a question or give a command.
3. The voice assistant will process your input and respond accordingly.

## Changing Owner Name or Bot Name 🔄

You can change the owner name or bot name in the code by modifying the `owner` and `botname` parameters in the `url` variable in the `answer` function. By default, the owner name is set to `apk000` and the bot name is set to `APK`.


Example:
```python
url = f"https://api.popcat.xyz/chatbot?msg={q}&owner=new_owner_name&botname=new_bot_name"
```


## Updates 🚀

### Version 2.0

- Added functionality to search and summarize information from Wikipedia based on user input.
- Improved speech recognition to provide better feedback when recognizing user input.
- Added the ability to respond with the current time when the user asks for it.
- Improved the `answer` function to use the `owner` parameter to customize the chatbot owner's name.

To update the owner name or bot name, modify the `owner` parameter in the `url` variable in the `answer` function.


## Troubleshooting ⚠️

- If you encounter any issues with the speech recognition or text-to-speech features, make sure your microphone is properly connected and working.
- Check your internet connection if the voice assistant is unable to fetch responses from the chatbot API.

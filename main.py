import pyttsx3


# If you receive errors such as No module named win32com.client,
# No module named win32, or No module named win32api, you will need to additionally install pypiwin32.

class TextToSpeech:
    def __init__(self, voice, rate: int, volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)  # Between 0 and 1

    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        self.engine.say(text)
        print('I\'m speaking...')

        if save:
            # On linux make sure that 'espeak' and 'ffmpeg' are installed
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()


    def list_available_voices(self):
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'({i + 1}) {voice.name} {voice.age}: {voice.languages[0]} ({voice.gender}) [ID: {voice.id}]')


if __name__ == '__main__':
    tts = TextToSpeech('com.apple.speech.synthesis.voice.daniel', 200, 1.0)
    # tts.list_available_voices()
    tts.text_to_speech('This will be converted to speech.', save=True, file_name='output.mp3')

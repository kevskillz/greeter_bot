import pyttsx3


class RoboResponse:
    tts = None

    def config(self):
        """ RATE"""
        rate = self.tts.getProperty('rate')  # getting details of current speaking rate
        print(rate)  # printing current voice rate
        self.tts.setProperty('rate', 125)  # setting up new voice rate

        """VOLUME"""
        volume = self.tts.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
        print(volume)  # printing current volume level
        self.tts.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

    def __init__(self):
        self.tts = pyttsx3.init()
        self.config()



    responses = []  # TODO add responses

    def say_response(self, message):

        def onEnd(name, completed):
            self.tts.endLoop()


        self.tts.connect('finished-utterance', onEnd)
        self.tts.say(message)
        self.tts.startLoop()






from playsound import playsound
import eel
from engine.config import ASSISTANT_NAME


@eel.expose
def playAssistantSound():
        music_path="www\\assets\\audio\\audio_notification.mp3"
        playsound(music_path)

def openCommand(query):
        query = query.replace(ASSISTANT_NAME, "")
        query = query.replace("open", "")
        query.lower()

        if query!= "":
                speak("Opening " + query)
                os.system('start' + query)
        else:
                speak("not found")

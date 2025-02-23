import pygame

# Initialize Pygame mixer
pygame.mixter.init()

# # Ser default volumes
volume_levels = {
    master_volume = .5,
    music_volume = .5,
    voice_volume = .5
}

# Load sound files
audio_file = os.path.join(os.path.dirname(__file__), '../assets/audio')
current_music_file = os.path.join(audio_file, "music/defultBGmusic.mp3")
current_voice_file = ""

def get_volume(type):
    """
    Get the volume level of given sound type,
    else return default .5
    """
    return volume_levels.get(type, .5)

def set_volume(type, value):
    """
    Updates the volume for the given sound type to value
    """
    volume_levels[type] = max(0, min(1, value))
    set_volume()

def set_volume():
    master = volume_levels["master_volume"]
    pygame.mixer.set
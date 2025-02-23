from enum import Enum
import os

path = os.path.join(os.path.dirname(__file__), '../assets/backgrounds/')
class Background(Enum):
    CAFETERIA = path + 'cafeteria.jpeg'
    CLASSROOM = path + 'classroom.jpeg'
    HIGHSCHOOL_STAIRS = path + 'highschool_stairs.jpg'
    ICE_CREAM_SHOP = path + 'ice_cream_shop.png'
    NURSE_OFFICE = path + 'nurse_office.jpg'
    ONSEN = path + 'onsen.jpg'
    SCHOOL_GYM = path + 'school_gym.jpg'
    SUMMER_FESTIVAL = path + 'summer_festival.jpg'
    VOLUNTEER = path + 'volunteer.jpg'

class SceneManager:
    def __init__(self):
        self.curr_bg = None 

    def set_background(self, bg: Background):
        self.curr_bg = Background[str(bg)].value

sceneManager = SceneManager()

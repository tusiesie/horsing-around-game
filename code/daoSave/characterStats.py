import json
import os

class CharacterStats:

    def __init__(self):
        self.stats = self.default_stats()
        self.filename = "savefile.json"
        self.save_game()

    def default_stats(self):
        dict =  {
            "Moneighca": 0,
            "Whorsina": 0, 
            "Kiyomi": 0,
            "Decision": 0,  # start right after decision number x
            "Arc": 0        # indicates which arc the decision is at
        }
        return dict

    def reset_game(self):
        """
        Resets the game to the start
        Used when the "New Game" button is pressed
        """
        self.stats = self.default_stats()
        self.save_game()

    def load_game(self):
        """
        Loads the game from the save file
        Used when the "Continue" button is pressed
        """
        try:
            with open(self.filesname, 'r') as file:
                self.stats = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.stats = self.default_stats()


    def save_game(self):
        """
        Saves the game from the the decision number and arc number
        """

        with open(self.filename, 'w') as file:
            json.dump(self.stats, file, indent=4)

    def get_stats(self):
        """
        Gets the stats of the all the horses, range from -100 to 100
        """
        return (self.stats.get("Moneighca"), self.stats.get("Whorsina"), self.stats.get("Kiyomi"))
    
    def get_last_save(self):
        """
        Get the numbers for the last save
        Return a tuple (decision, arc)
        """
        return (self.stats.get("Decision"), self.stats.get("Arc"))

    def add_moneighca(self, value):
        """
        Adds value to Moneighca's love meter
        """
        points = self.stats.get("Moneighca")
        points += value
        self.stats["Moneighca"] = self.check_bounds(points)
        self.save_game()

    def add_whorsina(self, value):
        """
        Adds value to Whorsina's love meter
        """
        points = self.stats.get("Whorsina")
        points += value
        self.stats["Whorsina"] = self.check_bounds(points)
        self.save_game()


    def add_kiyomi(self, value):
        """
        Add value to Kiyomi's love meter
        """
        points = self.stats.get("Kiyomi")
        points += value
        self.stats["Kiyomi"] = self.check_bounds(points)
        self.save_game()

    def check_bounds(self, value):
        """
        Makes sure that the value is in range -100 to 100
        """
        if (value > 100):
            return 100
        elif (value < -100):
            return -100
        else:
            return value

    def decision_made(self, value):
        """
        Changes the decision number of the last decision
        """
        self.stats["Decision"] = value
        self.save_game()

    def scene_at(self, value):
        """
        Changes the scene at arc number at value
        """
        self.stats["Arc"] = value
        self.save_game()
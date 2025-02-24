from enum import Enum
import os

class Arcs(Enum):
   BEGINNING = 'BEGINNING'
   NURSE_OFFICE        = 'NURSE OFFICE'         
   DETENTION           = 'DETENTION'
   VOLUNTEER           = 'VOLUNTEER'        
   GROUP_PROJECT       = 'GROUP PROJECT'  
   ICE_CREAM           = 'ICE CREAM'      
   SUMMER_FESTIVAL     = 'SUMMER FESTIVAL'
   CONFESSION          = 'CONFESSION'    
   HORSE_PROM          = 'HORSE PROM'   
   HORSE_PROM_MURDER   = 'HORSE PROM MURDER'
   ONSEN               = 'ONSEN'   

class Context:
    '''
    takes in an arc as a paramter (all caps), this will read the appropriate text from dialogues.txt
    arcs:
        - BEGINNING
        - NURSE OFFICE
        - DETENTION
        - VOLUNTEER
        - GROUP PROJECT
        - ICE CREAM
        - SUMMER FESTIVAL
        - CONFESSION
        - HORSE PROM
        - HORSE PROM MURDER
        - ONSEN
    '''
    
    def __init__(self, arc = Arcs.BEGINNING.value):
        self.arc = arc
        self.arc_chars = [] # characters for the current arc
        self.dialogue_idx = 0
        self.dialogues= []
        self.parsing = False

    def load_text(self):
        script = os.path.join(os.path.dirname(__file__), 'dialogues.txt')
        with open(script) as dialogues:

            for dialogue in dialogues:
             
                if self.arc in dialogue:
                    self.parsing = True

                if self.parsing and 'END' in dialogue:
                    self.parsing = False
                
                if self.parsing:
                    if  ':=' in dialogue:
                        character, line = dialogue.split(':=')
                        self.dialogues.insert( self.dialogue_idx, [ character, line ])

                    if dialogue == '\n':
                        self.dialogue_idx += 1

    def load_arc(self, arc: Arcs):
        self.arc = arc.value
        if len(self.dialogues) > 0:
            return

        self.load_text()

    def get_dialogue(self):
        return iter(self.dialogues)
                     




''' example usage to load the dialogues of the BEGINNING
c = Context('BEGINNING')
c.load_text()
x = c.get_dialogue()
while (y:= next(x, None)) is not None:
    print(y)

'''

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
    
    def __init__(self, arc):
        self.arc = arc
        self.arc_chars = [] # characters for the current arc
        self.dialogue_idx = 0
        self.dialogues= []
        self.parsing = False

    def load_text(self):
        with open('dialogues.txt') as dialogues:

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
    def get_dialogue(self):
        return iter(self.dialogues)
                     




''' example usage to load the dialogues of the BEGINNING
c = Context('BEGINNING')
c.load_text()
x = c.get_dialogue()
while (y:= next(x, None)) is not None:
    print(y)

'''

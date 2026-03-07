class GameState:
    def __init__(self):
        self.name = "Player"
        self.path = ""
        self.location = ""
        self.current_scene = "start"

scenes = {
    "start": {
        "text": "Welcome to Flip the Script. This is your life. \n"
                "The world you were born into already had a plan for you — shaped by your gender, your background, and the expectations of everyone around you." 
                "Some paths will be wide open. Others will be quietly closed before you ever reach them. \n"
                "There is no single correct way to live. But not every path is equally available to everyone.",
        "choices": [
            {
                "text": "Small Town",
                "next_scene": "career",
                "effects": {"location": "Small Town", "happiness": 5}
            },
            {
                "text": "Big City",
                "next_scene": "career",
                "effects": {"location": "Big City", "money": 10}
            }
        ]
    },
    "career": {
        "text": "What do you want to do next?",
        "choices": [
            {
                "text": "Go to university",
                "next_scene": "university",
                "effects":  {"path": "University"}
            },
            {
                "text": "Start working",
                "next_scene": "job",
                "effects": {"money": 20},
                "effects":  {"path": "Working"}
            }
        ]
    },
    "university": {
        "text": "You start university. A new chapter begins.",
        "choices": []
    },
    "job": {
        "text": "You start working and earning money.",
        "choices": []
    }
}


class Game:
    def __init__(self):
        self.state = GameState()

    def get_current_scene(self):
        return scenes[self.state.current_scene]

    def apply_effects(self, effects):
        for key, value in effects.items():
            current = getattr(self.state, key)
            if isinstance(current, int):
                setattr(self.state, key, current + value + "\n")
            else:
                setattr(self.state, key, value + "\n")

    def make_choice(self, choice_index):
        scene = self.get_current_scene()
        choice = scene["choices"][choice_index]

        self.apply_effects(choice.get("effects", {}))
        self.state.current_scene = choice["next_scene"]

    def get_summary(self):
        return (
            f"{self.state.name}\n"
            f"{self.state.location}"
          
            f"{self.state.path}"
        )

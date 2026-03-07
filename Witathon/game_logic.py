class GameState:
    def __init__(self):
        self.name = "Player"
        self.path = ""
        self.location = ""
        self.current_scene = "start"

scenes = {
    "start": {
        "text": "You are sixteen. You have spent your whole life being shaped by a world that had opinions about you before you could form your own. \n"
                "The clothes you were steered toward, the ambitions that were quietly encouraged or gently discouraged, the way you learned to take up less space in a room. \n"  
                "You are smart — people have always said so — but smart has never felt like enough on its own. The world wants you to also be agreeable. Likeable. Easy. \n",
        "choices": [
            {
                "text": "Go to university",
                "next_scene": "career",
                "effects": {"location": "Small Town"}
            },
            {
                "text": "Big City",
                "next_scene": "career",
                "effects": {"location": "Big City"}
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

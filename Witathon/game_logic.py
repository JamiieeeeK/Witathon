class GameState:
    def __init__(self):
        self.name = "Player"
        self.path = ""
        self.location = ""
        self.field = ""
        self.current_scene = "start"


scenes = {

    "start": {
        "text": (
            "Here is where your story begins to branch.\n\n"
            "You have finished school. The structure that held your days together is gone, "
            "and what comes next is, for the first time, something you get to choose.\n\n"
            "What do you do?"
        ),
        "choices": [
            {"text": "Go to university", "next_scene": "university_field", "effects": {"path": "University"}},
            {"text": "Enter the workforce", "next_scene": "job", "effects": {"path": "Workforce"}},
            {"text": "Start a business", "next_scene": "business", "effects": {"path": "Business"}},
            {"text": "Take time to travel and figure things out", "next_scene": "travel", "effects": {"path": "Travel"}}
        ]
    },

    "university_field": {
        "text": (
            "Choose your field:\n\n"
            "Medicine\n"
            "Engineering or Technology\n"
            "Business\n"
            "Arts, Humanities, or Education\n"
            "Law\n\n"
            "Some choices will feel natural. Others will place you in spaces where you are the exception."
        ),
        "choices": [
            {"text": "Medicine", "next_scene": "medicine", "effects": {"field": "Medicine"}},
            {"text": "Engineering or Technology", "next_scene": "engineering", "effects": {"field": "Engineering"}},
            {"text": "Business", "next_scene": "business_degree", "effects": {"field": "Business"}},
            {"text": "Arts, Humanities, or Education", "next_scene": "arts", "effects": {"field": "Arts"}},
            {"text": "Law", "next_scene": "law", "effects": {"field": "Law"}}
        ]
    },

    "medicine": {
        "text": "You choose Medicine. The path ahead is demanding and competitive.",
        "choices": [{"text": "Continue", "next_scene": "career_stage"}]
    },

    "engineering": {
        "text": "You choose Engineering or Technology. Innovation and challenge define your path.",
        "choices": [{"text": "Continue", "next_scene": "career_stage"}]
    },

    "business_degree": {
        "text": "You choose Business. Opportunity and competition shape your future.",
        "choices": [{"text": "Continue", "next_scene": "career_stage"}]
    },

    "arts": {
        "text": "You choose Arts, Humanities, or Education. Ideas and people guide your journey.",
        "choices": [{"text": "Continue", "next_scene": "career_stage"}]
    },

    "law": {
        "text": "You choose Law. Structure, argument, and power shape your career.",
        "choices": [{"text": "Continue", "next_scene": "career_stage"}]
    },

    "job": {
        "text": "You enter the workforce. Independence comes quickly.",
        "choices": [{"text": "Continue", "next_scene": "career_stage"}]
    },

    "business": {
        "text": "You start a business. Freedom and uncertainty arrive together.",
        "choices": [{"text": "Continue", "next_scene": "career_stage"}]
    },

    "travel": {
        "text": "You take time to travel and explore the world.",
        "choices": [{"text": "Continue", "next_scene": "career_stage"}]
    },

    "career_stage": {
        "text": (
            "Career (Age 22–28)\n\n"
            "Your career begins to take shape.\n\n"
            "What does your working life look like?"
        ),
        "choices": [
            {"text": "Climbing a traditional corporate structure", "next_scene": "relationships", "effects": {"career": "climbing up steadily in a company"}},
            {"text": "Building something of your own", "next_scene": "relationships", "effects": {"career": "start something new"}},
            {"text": "A creative or independent path", "next_scene": "relationships", "effects": {"career": "creative career path"}},
            {"text": "A caregiving or community-focused role", "next_scene": "relationships", "effects": {"career": "caregiving or community-focused role"}},
            {"text": "Still figuring it out — no clear direction yet", "next_scene": "relationships", "effects": {"career": "Confused"}}
        ]
    },

    "relationships": {
        "text": (
            "Relationships (Age 24–30)\n\n"
            "How you choose to build — or not build — a life with others "
            "is among the most personal decisions you'll make.\n\n"
            "What does your relationship life look like?"
        ),
        "choices": [
            {"text": "Long-term partnership leading to marriage", "next_scene": "family", "effects": {"status": "healthy relationship planning on marrage"}},
            {"text": "Long-term partnership without marriage", "next_scene": "family", "effects": {"status": "healthy long term relationship"}},
            {"text": "Multiple relationships — no single commitment", "next_scene": "family", "effects": {"status": "no commitment in relationships"}},
            {"text": "Chosen solitude — a full life without romantic partnership", "next_scene": "family", "effects": {"status": "proud to be single"}},
            {"text": "A relationship shaped by outside pressure", "next_scene": "family", "effects": {"status": "A relationship shaped by outside pressure"}}
        ]
    },

    "family": {
        "text": (
            "Family (Age 27–33)\n\n"
            "The question of children sits at the intersection "
            "of personal desire and social expectation.\n\n"
            "What path do you take?"
        ),
        "choices": [
            {"text": "Choose to have children", "next_scene": "midlife", "effects": {"home": "going to have children"}},
            {"text": "Choose not to have children", "next_scene": "midlife", "effects": {"home": "decided not to have children"}},
            {"text": "Have children earlier than planned", "next_scene": "midlife", "effects": {"home": "have children earlier than planned"}},
            {"text": "Raise children as a single parent", "next_scene": "midlife", "effects": {"home": "as single parent with children"}},
            {"text": "Build a family outside traditional structures", "next_scene": "midlife", "effects": {"home": "build a family outside traditional structures"}}
        ]
    },

    "midlife": {
        "text": (
            "Mid-Life Reflection (Age 35–40)\n\n"
            "Years have passed. The life you've built now has shape and consequence.\n\n"
            "Where do you go from here?"
        ),
        "choices": [
            {"text": "Stay the course", "next_scene": "laterlife", "effects": {"work": "stay the course"}},
            {"text": "Shift careers", "next_scene": "laterlife", "effects": {"work": "shift career"}},
            {"text": "Relocate and start fresh", "next_scene": "laterlife", "effects": {"work": "relocate and start fresh"}},
            {"text": "Revisit your identity", "next_scene": "laterlife", "effects": {"work": "revisit your identity"}},
            {"text": "Simplify and focus on what matters most", "next_scene": "laterlife", "effects": {"work": "focus on most important matters"}}
        ]
    },

    "laterlife": {
        "text": (
            "Later Life (Age 50+)\n\n"
            "The urgency of earlier decades begins to settle.\n\n"
            "How do you spend this chapter?"
        ),
        "choices": [
            {"text": "Mentorship", "next_scene": "ending", "effects": {"laterlife": "start a mentorship"}},
            {"text": "Reinvention", "next_scene": "ending", "effects": {"laterlife": "reinvention"}},
            {"text": "Rest and reflection", "next_scene": "ending", "effects": {"laterlife": "rest and reflect on earlier life"}},
            {"text": "Advocacy and pushing for change", "next_scene": "ending", "effects": {"laterlife": "advocacy and pushing for change "}}
        ]
    },

    "ending": {
        "text": (
            "Your journey has reached its conclusion.\n\n"
            "The life you built was shaped by every path you chose — "
            "and by the paths shaped for you.\n\n"
            "Some doors were open. Others were narrow.\n\n"
            "This story was yours — but it was never shaped by you alone."
        ),
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
            setattr(self.state, key, value)

    def make_choice(self, choice_index):
        scene = self.get_current_scene()
        choice = scene["choices"][choice_index]

        self.apply_effects(choice.get("effects", {}))
        self.state.current_scene = choice["next_scene"]

    def get_summary(self):
        return (
            f"{self.state.name}\n"
            f"{self.state.path}\n"
            f"{self.state.field}\n"
        )

import ollama, os, platform
class RoutineAI:
    def __init__(self, level, goals, days, exercises, body_parts, duration, preferences) -> None:
        self.level = level
        self.goals = goals 
        self.days = days 
        self.exercises= exercises 
        self.body_parts = body_parts
        self.duration = duration 
        self.preferences = preferences
    
    def generate_routine(self):
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
        print("Generating Workout Session...")
        response = ollama.chat("llama3.2:latest", messages=[{
            "role":"user",
            "content":f"""
                i want you to create a routine based on these parameters:
                current fitness level: {self.level}
                fitness goals: {self.goals}
                days per week: {7 if self.days > 7 else self.days}
                type of exercises: {self.exercises}
                prefered body parts to train: {self.body_parts}
                how long the workout needs to take: {self.duration}
                gym or home: {self.preferences}
            """
        }])
        return response.message.content
    
import os, platform
from generator import RoutineAI
def getEntries() -> list:
    while True:
        try:
            os.system("cls") if platform.system() == "Windows" else os.system("clear")
            fit_level: str = input("What is your current fitness level(Beginner, Medium, Expert): ").strip().capitalize()
            fit_goals: str = ",".join(input("What are your fitness goals(separed by commas): ").strip().split(","))
            days: int = int(input("How many days per week can you commit to training: ").strip())
            exercises: str = ",".join(input("What type of exercises do you enjoy or prefer(separed by commas): ").strip().split(","))
            body_parts: str = ",".join(input("Do you have any specific areas of your body you'd like to focus on(separed by commas): ").strip().split(",")) 
            duration: str = input("How long would you like each workout session to be: ").strip()
            preferences: str = input("Do you have access to a gym or prefer working out at home(gym/home/both): ").strip().capitalize()
            return [fit_level, fit_goals, days, exercises, body_parts, duration, preferences]
        except Exception as ex:
            print("[!] - Invalid Exception: {}".format(ex))
            print("Please enter valid entries")
            continue
level, goals, days, exercises, body_parts, duration, preferences = getEntries()
routineAI = RoutineAI(level, goals, days, exercises, body_parts, duration, preferences)
content = routineAI.generate_routine()
if content:
    with open("workout_session.md", "w") as file:
        file.write(content)
        print("[+] - workout_session.md file generated successfully")
        
import subprocess
start = input("normal mode, dungeon mode, story mode?")
if start == "normal mode":
    subprocess.run("python main.py", shell=True)
elif start == "dungeon mode":
    subprocess.run("python dungeonmode.py", shell=True)
elif start == "story mode":
    subprocess.run("python storymode.py", shell=True)
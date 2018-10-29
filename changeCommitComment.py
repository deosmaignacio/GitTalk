import os, time

os.system("git status")
os.system("git add .")
os.system("git commit -m \"tempString\" ")
os.system("git push")

time.sleep(10)

os.system("git commit --amend -m \"youtubeLink\"")
os.system("git push --force")

import os, time

os.system("git status")
os.system("git add .")
os.system("git commit -m \"tempString\" ")
os.system("git push")

time.sleep(10)

youtubeLinkId = ""
completeYoutubeLink = "https://www.youtube.com/watch?v=" + youtubeLinkId
print(completeYoutubeLink)

os.system("git commit --amend -m " + completeYoutubeLink)
os.system("git push --force")

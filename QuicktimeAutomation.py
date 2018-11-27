from subprocess import Popen, PIPE

app = "Terminal"
file = "commit_video.mov"
record = '''
    set fileName to (path to desktop as text) & "{0}"
    tell application "QuickTime Player"
        activate
        set sr to new screen recording
        start sr
        repeat while exists sr
            delay 1
        end repeat
        open for access file fileName
        tell first document
            export in fileName using settings preset "720p"
            close saving no
        end tell
    end tell
    return fileName
  '''.format(file)

proc = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
result, error = proc.communicate(record)
filepath = result.replace(":","/")
filepath = filepath.split("Macintosh HD")[1]
print(filepath)

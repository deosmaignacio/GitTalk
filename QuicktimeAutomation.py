from subprocess import Popen, PIPE

app = "Terminal"

record = '''
    tell application "QuickTime Player"
        activate
        set sr to new screen recording
        start sr
        repeat while exists sr
            delay 1
        end repeat
        set fileName to (path to desktop as text) & "newRecording.mov"
        open for access file fileName
        tell last item of documents
            export in fileName using settings preset "720p"
            close
        end tell
        return fileName
    end tell
  ''' 

proc = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
result, error = proc.communicate(record)
filepath = result.replace(":","/")
print(filepath)
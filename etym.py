import webbrowser, sys, pyperclip

sys.argv # ['etym.py', 'word']

# Check if command line args were passed

if len(sys.argv) > 1:
        # 'word' -> 'word'
        word = ' '.join(sys.argv[1:])
        
else:
    word = pyperclip.paste()

webbrowser.open("http://etymonline.com/index.php?allowed_in_frame=0&search=" + word)

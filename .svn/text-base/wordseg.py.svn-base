import subprocess
import types

# Thai word segmentation
def wordseg(text):
    """If the input is not already Unicode, it will be decoded as utf-8."""
    if type(text) != types.UnicodeType:
        text = text.decode("utf-8", "ignore")

    # swath since 0.3.4 supports unicode with option -u
    p = subprocess.Popen("echo %s | swath -b ' ' -u u,u" % text, \
                             shell=True, stdout=subprocess.PIPE)
    p.wait()
    
    return p.communicate()[0]

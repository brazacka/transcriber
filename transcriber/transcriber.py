import eyed3


def update_version(filename, version = (2,3,0)):
    song = eyed3.load(filename)
    song.tag.version = version
    song.tag.save()

def set_comment(filename, text, desc=u'Transcriber'):
    if check_version(filename) == (2,2,0):
        print "Updating to version 2.3.0"
        update_version(filename)
    song = eyed3.load(filename)
    song.tag.comments.set(text, desc)
    song.tag.save()

def check_version(filename):
    song = eyed3.load(filename)
    return song.tag.version


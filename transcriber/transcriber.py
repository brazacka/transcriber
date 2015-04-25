import eyed3

def set_comment(filename, text, desc=u'Transcriber'):
    song = eyed3.load(filename)
    song.tag.comments.set(text, desc)
    song.tag.save()


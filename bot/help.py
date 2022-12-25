text: str


def get():
    global text
    return text


def generateHelp(handlers):
    global text
    text = ""
    for handler in handlers:
        try:
            text += '{}:   {}\n'.format(min(handler[1].other.prefixes) +
                                        min(handler[1].other.commands), handler[2])
        except:
            pass

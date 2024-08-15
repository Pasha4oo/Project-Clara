stickers = []

def stickers_check(text):
    if len(list(text)) <= 10:
        for sticker in stickers:
            if ((text).upper()).find(sticker) != -1:
                print()

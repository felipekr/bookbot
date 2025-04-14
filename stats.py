import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(book_path):
    text = get_book_text(book_path)
    words = text.split()
    count = len(words)
    final_words = count
    #print(final_words)
    #print(f"{count} words found in the document")
    get_num_letters(text, count)
    return final_words
    

def get_num_letters(words_string, count):
    low_cletterse = words_string.lower()
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0
    o = 0
    p = 0
    q = 0
    r = 0
    s = 0
    t = 0
    u = 0
    v = 0
    x = 0
    y = 0
    w = 0
    z = 0
    for letter in low_cletterse:
              
        if letter == "a":
            a += 1
        elif letter == "b":
            b += 1
        elif letter == "c":
            c +=1
        elif letter == "d":
            d +=1
        elif letter == "e":
            e +=1
        elif letter == "f":
            f +=1
        elif letter == "g":
            g +=1
        elif letter == "h":
            h +=1
        elif letter == "i":
            i +=1
        elif letter == "j":
            j +=1
        elif letter == "k":
            k +=1
        elif letter == "l":
            l +=1
        elif letter == "m":
            m +=1
        elif letter == "n":
            n +=1
        elif letter == "o":
            o +=1
        elif letter == "p":
            p +=1
        elif letter == "q":
            q +=1
        elif letter == "r":
            r +=1
        elif letter == "s":
            s +=1
        elif letter == "t":
            t +=1
        elif letter == "u":
            u +=1
        elif letter == "v":
            v +=1
        elif letter == "x":
            x +=1
        elif letter == "w":
            w +=1
        elif letter == "y":
            y +=1
        elif letter == "z":
            z +=1
    
    final_dic = {
        "a": a,
        "b": b,
        "c": c,
        "d": d,
        "e": e,
        "f": f,
        "g": g,
        "h": h,
        "i": i,
        "j": j,
        "k": k,
        "l": l,
        "m": m,
        "n": n,
        "o": o,
        "p": p,
        "q": q,
        "r": r,
        "s": s,
        "t": t,
        "u": u,
        "v": v,
        "x": x,
        "y": y,
        "z": z
    }
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for doc in final_dic:
        print(f" {doc}: {final_dic[doc]}")
    print("============= END ===============")
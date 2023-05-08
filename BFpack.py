huffman = { 
    ">": "00",
    "<": "100",
    "+": "110",
    "[": "111",
    "]": "010",
    "-": "011",
    ".": "1010",
    ",": "1011"
}

def encode(code):
    o = ""
    for i in code:
        if i in "><+-[],.":
            o += huffman[i]
    return o

def decode(code):
    c = code
    o = ""
    while len(c) > 0:
        if c[:2] == '00': # >
            o += '>'
            c = c[2:]
        elif c[:3] == '100': # <
            o += '<'
            c = c[3:]
        elif c[:3] == '110': # +
            o += '+'
            c = c[3:]
        elif c[:3] == '111': # [
            o += '['
            c = c[3:]
        elif c[:3] == '010': # ]
            o += ']'
            c = c[3:]
        elif c[:3] == '011': # -
            o += '-'
            c = c[3:]
        elif c[:4] == '1010': # .
            o += '.'
            c = c[4:]
        elif c[:4] == '1011': # ,
            o += ','
            c = c[4:]
    return o

def code(invoerstring):
    code = ""
    for i in invoerstring:
        y = ord(i) + 3
        code += chr(y)
    return code
print(code('RutteAlkmaarDen Helder'))
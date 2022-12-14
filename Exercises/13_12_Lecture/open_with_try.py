try:
    file = open("some_text.txt", "r")
    print(file.read())
except IOError:
    print("An I/O error")
except:
    print("An unknown error")
else:
    file.close()

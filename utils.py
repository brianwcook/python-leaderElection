def get_file(file):
    try:
        f = open(file, 'r')
        contents = f.read()
        return contents
    except:
        print("\nCouldn't open file " + file)
        exit(1)


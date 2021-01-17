def createFile(name):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except FileNotFoundError as e:
        print(e)
        print(e.args)
        print(e.errno)
        print(e.strerror)
        name = name.replace('/', '-')
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except OSError as e:
        print(e)
        stopWords = ['?', '#', ';']
        for w in stopWords:
            name = name.replace(w, '')
        # name = name.replace('?', '')
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except Exception as e:
        print(e)
        pass

# createFile('test111')
createFile('test12345/test456')
# createFile('test?')
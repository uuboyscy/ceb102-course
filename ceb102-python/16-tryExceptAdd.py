def add(x, y):
    try:
        output = x + y
    except TypeError:
        try:
            output = int(x) + int(y)
        except ValueError:
            output = str(x) + str(y)
        except:
            print('Unexceptable exception.')
            pass
    except:
        print('Unexceptable exception.')
        pass
    else:
        print('Try successed.')
    finally:
        print('Finally executed.')
    return output

print(add(3, 5))
print('==========')
print(add('3', '5'))
print('==========')
print(add(3, '5'))
print('==========')
print(add(3, 'a'))
print('==========')

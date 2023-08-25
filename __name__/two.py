import one

print('TOP LEVEL IN TWO.PY')

one.func()

if __name__ == '__main__s':
    print('Two.py is being run directly')
else:
    print('Two.py has been imported!')
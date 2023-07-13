import os

# path1 = os.path.abspath(__file__)
# print(path1)
# path2 = os.path.dirname(path1)
# print(path2)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    print(BASE_DIR)

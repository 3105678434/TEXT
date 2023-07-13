import json
from app import BASE_DIR


def build_add_data():
    with open(BASE_DIR + '/data/add1.json') as f:
        data = json.load(f)
        return data


def build_add_data1():
    with open(BASE_DIR + '/data/add1.json') as f:
        data_list = json.load(f)
        new_list = []
        for data in data_list:
            a = data.get('a')
            b = data.get('b')
            expect = data.get('expect')
            new_list.append((a, b, expect))
        return new_list


def build_login_data():
    with open(BASE_DIR + '/data/login.json', encoding='utf-8') as f:
        data_list = json.load(f)
        new_list = []
        for data in data_list:
            username = data.get('username')
            password = data.get('password')
            expect = data.get('expect')
            new_list.append((username, password, expect))

        return new_list


# if __name__ == '__main__':
#     print(build_add_data1())

if __name__ == '__main__':
    print(build_login_data())

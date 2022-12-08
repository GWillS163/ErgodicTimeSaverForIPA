# Github: GWillS163
# User: 駿清清 
# Date: 08/12/2022 
# Time: 16:31
import pickle


def dump(data, path):
    with open(path, "wb") as f:
        pickle.dump(data, f)


def load(path):
    with open(path, "rb") as f:
        return pickle.load(f)


if __name__ == '__main__':
    dump({"a": 1, "b": 2}, "./unitTest.pytmp")
    print(load("./unitTest.pytmp"))

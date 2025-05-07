#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":

    for file_name in dir(hidden_4):
        if file_name[:2] != '__':
            print(file_name)

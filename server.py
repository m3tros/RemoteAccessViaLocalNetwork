import os
import sys
import colorama
import shlex
from colorama import Fore
from prompt_toolkit import prompt
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.cursor_shapes import CursorShape
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
colorama.init()
os.system('cls || clear')


def exit():
    print('\n{}[*]{} Completion of work...'.format(Fore.BLUE, Fore.WHITE))
    sys.exit()


def main():
    while True:
        try:
            server_ip = prompt('ip: ', auto_suggest=AutoSuggestFromHistory(
            ), cursor=CursorShape.BLINKING_BEAM)
            if server_ip.replace(' ', '').strip('\n') != '':
                server_port = prompt('port: ', auto_suggest=AutoSuggestFromHistory(
                ), cursor=CursorShape.BLINKING_BEAM)
                if server_port.replace(' ', '').strip('\n') != '':
                    break
        except KeyboardInterrupt:
            exit()
    server_socket = socket(AF_INET, SOCK_DGRAM)
    server_socket.bind((server_ip, int(server_port)))
    while True:
        (data, addr) = server_socket.recvfrom(1024)
        data = data.decode('utf-8')
        if data.lower() == 'server_exit' or data.lower() == 'server_quit':
            exit()
        elif data.lower() == 'server_clear' or data.lower() == 'server_clean' or data.lower() == 'server_cls':
            os.system('cls || clear')
        else:
            os.system(data)


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('{}[!]{} [Unknown error]: {}'.format(
            Fore.RED, Fore.WHITE, str(error)))
        sys.exit()

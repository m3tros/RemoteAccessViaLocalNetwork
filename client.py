import os
import sys
import colorama
import shlex
from colorama import Fore
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.cursor_shapes import CursorShape
from prompt_toolkit import PromptSession
from socket import socket, AF_INET, SOCK_DGRAM

colorama.init()
os.system('cls || clear')
command_list = ['terminal_exit', 'terminal_quit',
                'terminal_cls', 'terminal_clear', 'terminal_clean',
                'server_quit', 'server_exit',
                'server_clear', 'server_clean', 'server_cls']
command_list.sort()
command_list = WordCompleter(command_list)

session = PromptSession()


def exit():
    print('\n{}[*]{} Completion of work...'.format(Fore.BLUE, Fore.WHITE))
    sys.exit()


def main():
    while True:
        try:
            server_ip = prompt('ip: ', cursor=CursorShape.BLINKING_BEAM)
            if server_ip.replace(' ', '').strip('\n') != '':
                server_port = prompt(
                    'port: ', cursor=CursorShape.BLINKING_BEAM)
                if server_port.replace(' ', '').strip('\n') != '':
                    break
        except KeyboardInterrupt:
            exit()
    server_socket = socket(AF_INET, SOCK_DGRAM)
    while True:
        try:
            command = session.prompt('$ ', auto_suggest=AutoSuggestFromHistory(
            ), completer=command_list, cursor=CursorShape.BLINKING_BEAM)
        except KeyboardInterrupt:
            exit()
        if command.replace(' ', '').strip('\n') != '':
            command_slpit = shlex.split(command)
            if str(command_slpit[0]).lower() == 'terminal_exit' or str(command_slpit[0]).lower() == 'terminal_quit':
                exit()
            elif str(command_slpit[0]).lower() == 'terminal_clear' or str(command_slpit[0]).lower() == 'terminal_clean' or str(command_slpit[0]).lower() == 'terminal_cls':
                os.system('cls || clear')
            else:
                server_socket.sendto(command.encode('utf-8'),
                                     (server_ip, int(server_port)))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('{}[!]{} [Unknown error]: {}'.format(
            Fore.RED, Fore.WHITE, str(error)))
        sys.exit()

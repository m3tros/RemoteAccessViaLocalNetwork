<h1 align="center">RemoteAccessViaLocalNetwork</h1> 

## Description

Scripts in <a href="https://python.org">python</a> <a href="https://www.python.org/downloads/release/python-3104/">3.10.4</a>  for remote access over local network. Based on the <a href="https://docs.python.org/3/library/socket.html">socket</a> library.

## Installation for python3
### Libraries
- <a href="https://pypi.org/project/colorama/">colorama</a>
- <a href="https://pypi.org/project/prompt-toolkit/0.5/">prompt_toolkit</a>

```bash
git clone https://github.com/John-MetrosSoftware/RemoteAccessViaLocalNetwork/
cd RemoteAccessViaLocalNetwork
pip3 install -r requirements.txt
```

## Server start
And so, first you need to run the file `server.py`.
```bash
python3 server.py
```
After starting, you must enter the ip address. For the current machine, this is the ip address `0.0.0.0`.<br>
Then you need to enter the port, usually `5000` or `8080`.<br>
<br>Example:
```bash
ip: 0.0.0.0
port: 8080
```

## Client start
Run the file `client.py`.
```bash
python3 client.py
```
You will be asked to enter the ip address to the server if you specified the ip address `0.0.0.0` on the server, then you need to enter your ip in order to find it out, enter the ifconfig command in a separate terminal, the command will display the internal ip address of your machine, you must enter it in the client ip line.<br><br>
`That is, what ip address is indicated on the server, this must be entered in this line.`
<br><br>
Then comes the port, the port must also advise the one specified on the server.
<br><br>
Example:
```bash
ip: 0.0.0.0
port: 8080
```
After everything you have specified, all commands entered by you will be processed on the server. Specifically terminal commands. So the script can be used on different operating systems. Below are the commands that are executed in the client terminal:
### Client
```
terminal_exit terminal_quit - These commands are responsible for shutting down the client terminal.
```
```
terminal_cls terminal_clear terminal_clean - These commands are responsible for clearing the client's terminal.
```
### Server
```
server_quit server_exit - These commands are responsible for shutting down the server terminal.                
```
```
server_clear server_clean server_cls - These commands are responsible for clearing the server terminal.
```
The terminal supports auto-completion in the form of a list.


## client.py
```python3
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
```

## server.py
```python3
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
```
## Compilation
This version 1.0 is a version without saving any settings or changing them.<br>
All software is provided in English with executable files, these parameters cannot be changed.<br>
I usually compile my projects using the <a href="https://pypi.org/project/pyinstaller/">pyinstaller</a> compiler with the following parameters:

```
pyinstaller -F server.py
pyinstaller -F client.py
```


## PEP8
<a href="https://pypi.org/project/autopep8/">autopep8</a> automatically formats Python code to conform to the PEP 8 style guide. It uses the pycodestyle utility to determine what parts of the code needs to be formatted. autopep8 is capable of fixing most of the formatting issues that can be reported by pycodestyle.
```
autopep8 server.py --recursive --in-place
autopep8 client.py --recursive --in-place
```
## Developer 
Telegram : https://t.me/metrossoftware

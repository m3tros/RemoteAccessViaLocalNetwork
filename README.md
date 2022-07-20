<p align="center"> 
  <img src="https://cdn-icons-png.flaticon.com/512/7097/7097120.png" alt="RemoteAccessViaLocalNetwork" width="80" height="80">
</p>

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

## Compilation
This version `1.0` is a version without saving any settings or changing them.<br>
All software is provided in English with executable files, these parameters cannot be changed.<br>
I usually compile my projects using the <a href="https://pypi.org/project/pyinstaller/">pyinstaller</a> compiler with the following parameters:

```
pyinstaller -F server.py
pyinstaller -F client.py
```

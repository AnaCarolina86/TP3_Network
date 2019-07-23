# TP3_Network

## Description

In this practical work, we have been asked to implement a system that allows text files to be sent to a “personal folder” and to request files at any time, in addition to registering new users. Thus, I develop two programs, a client and a server, where the client makes requests to the server, such as creating new users and storing files.


The client program sends the user's messages to the server, and prints the server response on the screen according to the message sent. This way, the client does not have data structures or functions, only has what is necessary to make the connection to the server, and can always be sending messages through the keyboard and printing the response on the screen. In addition, there was a timer that counted the time to receive messages, it was removed to allow the client program to be in an infinite loop, sending messages through the user and receiving response from the server.


The server program performs file manager implementation using the Dictionary data structure and an object. Python Dictionary is an abstract data type that associates a key with a value, in this work the key represents the file name and the value, the content. Use of the object is required to associate a user with their files, along with their contents, where the object represents the user registered in the system.

The compilation of the program is as follows:

```
python servidor.py <porta>
python cliente.py <IP/nome> <porta>
```

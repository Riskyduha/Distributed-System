#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:09:52 2024

@author: widhi
"""

import socket

def client_program():
    client_socket = socket.socket()  
    # Use docker compose service DNS name
    client_socket.connect(('reqresp-server', 4444))  
    
    message = input("Enter message: ")  
    
    while message.lower().strip() != 'bye':
        try:
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError) as e:
            print('Connection error:', e)
            break

        print('Received from server:', data)

        message = input("Enter another message: ")
    
    client_socket.close()

if __name__ == '__main__':
    client_program()

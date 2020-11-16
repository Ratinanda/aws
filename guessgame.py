import random
import socket
import sys


number = random.randint(1, 100)
count = 0
points = 1000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)
while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    connection.sendall(number)
while count < 10:
    mynumber = int(input("Please enter your number:"))
    if number == mynumber:
        print("You guess it correct: you got ", points)
    if number > mynumber:
        print("you guessed too low")

        points = points - 100
    if number < mynumber:
        print("you guessed too High")
        points = points - 100
    if count < 10 and number == mynumber:
        print("You did it in ", count, "You guess it correct: you got ", points)
        exit(0)
    count = count + 1

print(number)

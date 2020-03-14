import socket
import sys

values = []

for i in range(0, 5):
    row = []
    for j in range(0, 7):
        tile = [" "," "," "," "," "]
        row.append(tile)
    values.append(row)



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def server_request(s):
    request_size = "{:<256}".format(str(len(s))).encode("ascii")
    client.send(request_size)
    client.send(s.encode("ascii"))


def server_response():
    response_size = client.recv(256).decode().replace("\x00", "")
    response = client.recv(int(response_size)).decode("ascii")
    if "error" in response:
        print(response.replace("error", "Error:"))
    if "event notify" in response:
        print(response.replace("event notify", "Server:"))
    if "event message" in response:
        print(response.replace("event message", ""))
    return response

connected = False
while connected == False:
    command = input("> ")
    if command == "quit":
        client.close()
        sys.exit()
    commandsplit = command.split(" ")
    if commandsplit[0] == "connect":
        try:
            client.connect((commandsplit[1], int(commandsplit[2])))
            server_request(command)
            if server_response() == "ok connected":
                print("Connected, please log in")
                connected = True
        except:
            print("Unable to connect to the server, check command arguments")

loggedIn = False
while loggedIn == False:
    command = input("> ")
    if command == "quit":
        client.close()
        sys.exit()
    commandsplit = command.split(" ")
    if commandsplit[0] == "login":
        if len(commandsplit) < 3:
            print("Incomplete login criteria")
        else:
            server_request(command)
            server_response()
            if server_response() == "ok login":
                print("Logged In!")
                loggedIn = True
            else:
                print("Invalid login details")
    else:
        print("Cannot invoke the command in this state")

while loggedIn == True:
    command = input("> ")
    commandsplit = command.split(" ")
    if command == "observe":
        server_request("action observe")
        e = server_response().replace("ok observe ", "").replace("(", "").replace(")", "")
        data = e.split(" ")

        for i in range(0, 5):
            for j in range(0, 7):
                data[i*7+j] = data[i*7+j].split(",")
                for m in range(0, 5):
                    values[i][j][m] = int(data[i*7+j][m])


        for i in range(0, 5):
            for j in range(0, 7):
                if i == 2 and j == 3:
                    item = "R"
                    height = "R"
                else:

                    if values[i][j][3] == 1:
                        item = "R"
                    elif values[i][j][4] == 1:
                        item = "M"
                    else:
                        item = " "
                    if values[i][j][2] < 0:
                        height = "-"
                    elif values[i][j][2] == 0:
                        height = " "
                    elif values[i][j][2] > 9:
                        height = "9"
                    else:
                        height = str(values[i][j][2])
                if j == 6 :
                    print("|{}{}|".format(item, height))
                else:
                    print("|{}{}".format(item, height), end="")

    elif commandsplit[0] == "move":
        server_request("action {}".format(command))
        e = server_response()

    elif command == "stats":
        server_request("action stats")
        i = server_response().replace("ok stats ", "").replace("(", "").replace(")", "")
        i = i.split(",")

        print("Number of tiles explored: {:}".format(i[2]))
        print("Current position: ({:},{:})".format(i[0], i[1]))


    elif commandsplit[0] == "inspect":
        server_request("action {}".format(command))
        e = server_response()
        if e == "ok inspect":
            print("Nothing interesting was found here")
        else:
            msg = e.replace("ok inspect (", "").replace(")", "")
            print("You found a note: {}".format(msg))
    elif command == "quit":
        client.close()
        sys.exit(0)

    elif commandsplit[0] == "note":
        server_request("action {}".format(command))
        e = server_response()
        if "error" in e:
            print(e.replace("error", "Error:"))

    elif commandsplit[0] == "message":
        server_request("action {}".format(command))
        e = server_response()
        if "error" in e:
            print(e.replace("error", "Error:"))
    else:
        print("invalid command")

while True:
    server_response()

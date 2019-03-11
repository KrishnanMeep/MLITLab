from threading import Thread

class Server:
    def __init__(self, max):
        self.__max_requests = max
        self.__current_requests = 0

    def request(self):
        if self.__current_requests + 1 < self.__max_requests:
            self.__current_requests += 1
            self.handle_request()
            return 0
        else:
            print("DENIED")
            return 1

    def handle_request(self, client):
        print("handling request for " + client.id)
        sleep(2)


class Client:
    def __init__(self, id):
        self.id = id

    def request_server(self, server_id):
        servers[server_id].request()

if __name__ == '__main__':
	servers = [ 
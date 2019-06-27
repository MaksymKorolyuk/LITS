import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            connection = self.request
            msg = connection.recv(1024)
            print(msg.decode('utf-8'))

            response_body = '<h1>Hello</h1>'

            response = f"""
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(response_body)}
Connection: keep-alive

{response_body}"""

            connection.sendall(response.encode())


with socketserver.TCPServer(('', 8080), Handler) as server:
    server.serve_forever()

import _thread
# import time
# from threading import Thread, Lock
#
# count = 0
# lock = Lock()
#
#
# def worker():
#     global count
#     for _ in range(5):
#         with lock:
#             count += 1
#             time.sleep(.1)
#             print(count)
#             count += 1
#
#
# threads = []
#
# for i in range(10):
#     thread = Thread(name=f'{i}', target=worker, args=())
#     threads.append(thread)
#
# for thread in threads:
#     thread.start()
#
# for thread in threads:
#     thread.join()
#
# print('count: ', count)

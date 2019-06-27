import time
import queue
import argparse

from functools import partial
from threading import Thread, Timer, Lock
from multiprocessing import Process, Queue


# def callback(i):
#     print(i)
#
#
# class SetInterval(Thread):
#     def __init__(self, callback, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.lock = Lock()
#         self.callback = callback
#         self.count = 0
#
#     def run(self):
#         while True:
#             time.sleep(.5)
#             callback = partial(self.callback, self.count)
#             with self.lock:
#                 t = Timer(.5, callback)
#                 t.start()
#                 self.count += 1
#
#
# t = SetInterval(callback, daemon=True)
# t.start()
#
# time.sleep(4)
#
# lock = Lock()
# q = queue.Queue(5)
#
#
#
# def writer_worker(q):
#     for i in range(10):
#         try:
#             time.sleep(1)
#             q.put_nowait(i)
#         except queue.Full:
#             return
#
#
# def reader_worker(q):
#     while True:
#         try:
#             time.sleep(.5)
#             item = q.get(timeout=0.5)
#             print(item)
#         except queue.Empty:
#             return
#
#
# w = Thread(target=writer_worker, args=(q, ))
# r = Thread(target=reader_worker, args=(q, ))
#
# w.start()
# r.start()
#
# w.join()
# r.join()


parser = argparse.ArgumentParser()
parser.add_argument('-l', '--len')
print(parser.parse_args().len)

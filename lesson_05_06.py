import sys
import io

# print(sys.stdin, sys.stdout, sys.stderr, sep='\n')
# hendler = open('.gitignore')
#
# for line in hendler.readline():
#     print(line)
#
#
# hendler.close()

with open('text.json') as text:
    print(text.readlines())

# try:
#     text = open('text1.json')
#     print(text.readlines())
# except:
#     print("file doesn't exist!")
# finally:
#     text.close()


# class Contex:
#     def __enter__(self):
#         self.v = 42
#         return self.v
#
#     def __exit__(self, typeErr, err, traceback):
#         pass
#
#
# with Contex as c:
#     print(c)

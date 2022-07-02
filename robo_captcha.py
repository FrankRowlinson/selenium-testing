# since this func used a lot throughout a course, I wanted to implement it as a simple module

from math import log, sin


def calc(x):
  return str(log(abs(12 * sin(int(x)))))


if __name__ == '__main__':
    print("My first module, lol")
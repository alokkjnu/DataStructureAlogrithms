# Keeping the last N items
from collections import deque


def search(lines, pattern, history=5):
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_line


if __name__ == '__main__':
    with open('msg.txt') as f:
        for line, prevline in search(f, 'Python', 5):
            for pline in prevline:
                print(pline, end='')
            print(line, end='')
            print('_' * 20)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
print(q)

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
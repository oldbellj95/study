def put(item):
    queue.append(item)

def get():
    target = queue[0]
    queue.remove(queue[0])
    return target 

if __name__ == '__main__':
    queue = []
    put(1)
    put(2)
    put(3)
    put(4)
    
    while queue:
        print(get())
        print("큐에 남은 데이터 수 : " + str(len(queue)))
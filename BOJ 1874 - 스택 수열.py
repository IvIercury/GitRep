# Stack Data Structure!
# .append() = push
# .pop() = pop

def is_stack(length, ansList):

    nextnum = 1
    stack = [] #실제 Stack
    ansStack = [] #부호 담을 리스트

    while (ansList):
        target = ansList[0]
        if nextnum <= target: #만약 nextnum이 target보다 같거나 작으면?
            stack.append(nextnum) #stack에 nextnum 삽입
            ansStack.append('+') #삽입했으므로 + append
            nextnum += 1 #nextnum을 하나 증가

        else: # nextnum이 target보다 크면?
            if len(stack) == 0: #만약 stack이 empty하다면...?
                return 'NO'
            it = stack.pop()
            if it != target:
                return 'NO'
            else: #it == ansList[0]:
                ansList.pop(0)
                ansStack.append('-')
    return ansStack


ansList = []
N = int(input()) # List길이
for x in range(N):
    ansList.append(int(input()))

ans = is_stack(N, ansList)
if ans == 'NO':
    print("NO")
else:
    for elem in ans:
        print(elem)

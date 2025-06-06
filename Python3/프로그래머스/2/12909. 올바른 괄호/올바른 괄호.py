def solution(s):
    answer = True

    stackList = []

    for i in s:
        if i == "(":
            stackList.append(i)
        elif i == ")":
            if len(stackList) == 0:
                answer = False
                break
            removeList = stackList.pop()
            if removeList != "(":
                answer = False
                break
    if len(stackList) != 0:
        answer = False

    return answer
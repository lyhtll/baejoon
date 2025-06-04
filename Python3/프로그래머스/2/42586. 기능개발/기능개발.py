def solution(progresses, speeds):
    answer = []
    rt = [0]
    for i in progresses:
        idx = progresses.index(i)
        answer.append(0)
        while progresses[idx] < 100:
            progresses[idx] += speeds[idx]
            answer[idx] += 1
    f = answer[0]
    id = 0
    for i in answer:
        if i > f:
            f = i
            rt.append(1)
            id += 1
        else:
            rt[id] +=1
    return rt
def solution(array, commands):
    answer = []

    for c in commands:
        f = c[0]
        e = c[1]
        k = c[2] -1
        new = sorted(array[f-1:e])
        answer.append(new[k])

    return answer
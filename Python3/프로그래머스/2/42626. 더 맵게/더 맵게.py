import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) >= 2 and scoville[0] < K:
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        add = f + s*2
        heapq.heappush(scoville, add)
        answer += 1

    return answer if scoville[0] >= K else -1
import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> sequence = new ArrayList<>();
        sequence.add(n);

        while (n != 1) {
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = 3 * n + 1;
            }
            sequence.add(n);
        }

        // 리스트를 배열로 변환
        return sequence.stream().mapToInt(i -> i).toArray();
    }
}
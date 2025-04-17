class Solution {
    public int solution(int a, int b, int c, int d) {
        int score = 0;
        
        if (a == b && b == c && c == d) {
            // 1. 네 개가 모두 같은 경우
            score = 1111 * a;
        } else if (a == b && b == c) {
            // 2. a, b, c가 같고 d는 다름
            score = (int)Math.pow(10 * a + d, 2);
        } else if (a == b && b == d) {
            // 2. a, b, d가 같고 c는 다름
            score = (int)Math.pow(10 * a + c, 2);
        } else if (a == c && c == d) {
            // 2. a, c, d가 같고 b는 다름
            score = (int)Math.pow(10 * a + b, 2);
        } else if (b == c && c == d) {
            // 2. b, c, d가 같고 a는 다름
            score = (int)Math.pow(10 * b + a, 2);
        } else if (a == b && c == d) {
            // 3. 두 쌍 (a=b, c=d)
            score = (a + c) * Math.abs(a - c);
        } else if (a == c && b == d) {
            // 3. 두 쌍 (a=c, b=d)
            score = (a + b) * Math.abs(a - b);
        } else if (a == d && b == c) {
            // 3. 두 쌍 (a=d, b=c)
            score = (a + b) * Math.abs(a - b);
        } else if (a == b) {
            // 4. a=b, 나머지 c, d 다름
            score = c * d;
        } else if (a == c) {
            // 4. a=c, 나머지 b, d 다름
            score = b * d;
        } else if (a == d) {
            // 4. a=d, 나머지 b, c 다름
            score = b * c;
        } else if (b == c) {
            // 4. b=c, 나머지 a, d 다름
            score = a * d;
        } else if (b == d) {
            // 4. b=d, 나머지 a, c 다름
            score = a * c;
        } else if (c == d) {
            // 4. c=d, 나머지 a, b 다름
            score = a * b;
        } else {
            // 5. 전부 다름
            // 가장 작은 수 찾기
            int min = a;
            if (b < min) min = b;
            if (c < min) min = c;
            if (d < min) min = d;
            score = min;
        }
        
        return score;
    }
}
class Solution {
    public int solution(int a, int b) {
        int answer = 0;

        String n1 = Integer.toString(a);
        String n2 = Integer.toString(b);

        if (Integer.parseInt(n1+n2) >= Integer.parseInt(n2+n1)){
            answer = Integer.parseInt(n1+n2);
        }else{
            answer = Integer.parseInt(n2+n1);
        }

        return answer;
    }
}
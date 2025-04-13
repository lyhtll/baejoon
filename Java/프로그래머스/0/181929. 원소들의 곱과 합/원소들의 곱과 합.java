class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int sum = 0;
        int mult = 1;
        for (int i : num_list){
            sum += i;
            mult *= i;
        }
        if (sum * sum > mult) {
            answer = 1;
        }
        
        
        return answer;
    }
}
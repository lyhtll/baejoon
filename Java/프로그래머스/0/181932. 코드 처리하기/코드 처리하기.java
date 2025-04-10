class Solution {
    public String solution(String code) {
        String answer = "";

        int mode = 0;
        for (int i = 0; i < code.length(); i++) {
            char ch = code.charAt(i);
            if (String.valueOf(ch).equals("1")) {
                mode = mode == 0 ? 1:0;
                continue;
            }
            if (mode == 1){
                if ((i+1) % 2 == 0){
                    answer += ch;
                }
            }else {
                if ((i+1) % 2 != 0){
                    answer += ch;
                }
            }
        }
        if (answer.length() == 0){
            answer = "EMPTY";
        }

        return answer;
    }
}
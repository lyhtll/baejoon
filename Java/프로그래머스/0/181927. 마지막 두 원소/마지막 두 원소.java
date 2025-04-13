class Solution {
    public int[] solution(int[] num_list) {
        int len = num_list.length;
        int last = num_list[len - 1];
        int secondLast = num_list[len - 2];

        int valueToAdd;
        if (last > secondLast) {
            valueToAdd = last - secondLast;
        } else {
            valueToAdd = last * 2;
        }

        int [] list = new int[len+1];
        for (int i = 0 ; i < len ; i++) {
            list[i] = num_list[i];
        }
        list[len] = valueToAdd;
        return list;
    }
}
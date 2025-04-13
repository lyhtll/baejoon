class Solution {
        public int[] solution(int[] arr, int[][] queries) {

            for (int i = 0; i < queries.length; i++) {
                int idxi = queries[i][0];  // 이건 이미 인덱스라고 가정함
                int idxj = queries[i][1];

                // 값 교환
                int temp = arr[idxi];
                arr[idxi] = arr[idxj];
                arr[idxj] = temp;
            }

            return arr;  // arr 자체가 수정되었으니 그대로 반환
        }
    }

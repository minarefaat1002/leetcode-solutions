class Solution {
    public int sumOfUnique(int[] nums) {
        int sum = 0;
        int[] values = new int[101];
        Arrays.fill(values,0);
        for(int num: nums){
            values[num]++;
        }
        for(int i = 0; i<values.length;i++){
            if(values[i]==1) sum+=i;
        }
        return sum;
    }
}
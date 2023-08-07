class Solution {
    public int sumOfUnique(int[] nums) {
        // int sum = 0;
        // int[] values = new int[101];
        // Arrays.fill(values,0);
        // for(int num: nums){
        //     values[num]++;
        // }
        // for(int i = 0; i<values.length;i++){
        //     if(values[i]==1) sum+=i;
        // }
        // return sum;
        int sum = 0;
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int num:nums){
            if(map.containsKey(num)) map.put(num, map.get(num)+1);
            else map.put(num,1);
        }
        for(Map.Entry<Integer,Integer> entry : map.entrySet()){
            if(entry.getValue()==1){
                sum+= entry.getKey();
            }
        }
        return sum;
    }
}
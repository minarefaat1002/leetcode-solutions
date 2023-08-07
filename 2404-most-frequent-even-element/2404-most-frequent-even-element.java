class Solution {
    public int mostFrequentEven(int[] nums) {
        int curRepetitions = 0;
        int maxRepetitions = 0;
        int mostRepeated = -1;
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i = 0; i < nums.length; i++){
            if(nums[i]%2 == 0){
                if(map.containsKey(nums[i])) map.put(nums[i],map.get(nums[i])+1);
                else map.put(nums[i],1);
            }
        }
        for(Map.Entry<Integer,Integer> entry: map.entrySet()){
            if(entry.getValue() > maxRepetitions){
                maxRepetitions = entry.getValue();
                mostRepeated = entry.getKey();
            } else if(entry.getValue() == maxRepetitions && entry.getKey() < mostRepeated){
                mostRepeated = entry.getKey();
            }
        }
        return mostRepeated;
    }
}
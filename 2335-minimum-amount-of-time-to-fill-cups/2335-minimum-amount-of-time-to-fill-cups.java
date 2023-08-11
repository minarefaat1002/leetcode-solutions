class Solution {
    public int fillCups(int[] amount) {
        int seconds = 0;
        Arrays.sort(amount);
        while(amount[2] != 0){
            amount[2] -= 1;
            amount[1] -= 1;
            seconds += 1;
            Arrays.sort(amount);
        }
        return seconds;  
    }
}
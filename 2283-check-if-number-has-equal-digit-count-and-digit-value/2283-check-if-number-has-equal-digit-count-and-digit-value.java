class Solution {
    public boolean digitCount(String num) {
        // count = [0]*10
        // for digit in num:
        //     count[int(digit)]+=1
        // for i,digit in enumerate(num):
        //     if int(digit) != count[i]:
        //         return False
        // return True   
        int[] count = new int[10];
        Arrays.fill(count,0);
        for(int i=0;i<num.length();i++){
            count[Character.getNumericValue(num.charAt(i))]++;
        }
        for(int i=0;i<num.length();i++){
            if (Character.getNumericValue(num.charAt(i)) != count[i]) return false;
        }
        return true;
    }
}
class Solution {
    public int[] diStringMatch(String s) {
        int l = 0;
        int r = s.length();
        int[] res = new int[s.length()+1];
        for (int i = 0; i < s.length();i++){
            res[i] = s.charAt(i) == 'I' ? l++ : r--;
        }
        res[s.length()] = r;
        return res;
    }
}
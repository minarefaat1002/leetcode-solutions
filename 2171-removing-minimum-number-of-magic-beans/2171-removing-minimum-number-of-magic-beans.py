class Solution {
    public long minimumRemoval(int[] beans) {
        long totalBeans = 0;
        for(int b:beans) totalBeans+=b;
        Arrays.sort(beans);
        long minRemoved = Long.MAX_VALUE;
        for(int i=0;i<beans.length;i++){
            minRemoved = Math.min(minRemoved,totalBeans-(beans.length-i)*(long)beans[i]);
        }
        return minRemoved;
    }
}
class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        Map<Integer, String> map = new HashMap<>();
        for (int i = 0; i < names.length; i++) {
            map.put(heights[i], names[i]);
        }
        Arrays.sort(heights); // sorted in ascending order
        String[] res = new String[names.length];
        for (int i = 0; i < names.length; i++) {
            res[res.length - 1 - i] = map.get(heights[i]);
        }
        return res;
    }
}
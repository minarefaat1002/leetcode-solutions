class Solution {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        ArrayList<String> numbers = new ArrayList<String>();
        for(String s: words){
            String[] temp = s.split("["+ separator + "]");
            for(String number: temp){
                if(!number.equals("")) numbers.add(number);
            }
        }
        return numbers;
    }
}
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> mp = new HashMap<>();
        for (String word: strs){
            char[] s_word = word.toCharArray();
            Arrays.sort(s_word);
            String s_string = new String(s_word);

            if (!mp.containsKey(s_string)){
                mp.put(s_string, new ArrayList<>());
                mp.get(s_string).add(word);
            }
            else{
                mp.get(s_string).add(word);
            }
        }
        List<List<String>> res = new ArrayList<>();
        for (List<String> l_str: mp.values()){
            res.add(l_str);
        }
        return res;
    }
}

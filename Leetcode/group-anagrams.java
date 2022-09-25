class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> output = new ArrayList<>();
        Map<String, List<String>> hm = new HashMap<>();
        for (String s: strs){
            int[] count = new int[26];
            for (char c: s.toCharArray()) count[c - 'a']++;
            String hash = Arrays.toString(count);
            if (!hm.containsKey(hash)){
                hm.put(hash, new ArrayList<>());
            }
            hm.get(hash).add(s);
        }
        
        return new ArrayList<>(hm.values());
        
    }
}
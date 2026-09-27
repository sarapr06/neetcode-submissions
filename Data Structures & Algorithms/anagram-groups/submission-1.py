class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        anagramdict = defaultdict(list)
        for string in strs:
            #turn it into characters
            L=[]
            char_list = list(string)
            char_sorted= "".join(sorted(char_list))
            anagramdict[char_sorted].append(string)
        return list(anagramdict.values())
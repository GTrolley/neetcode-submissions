class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        temp_list = [] #List of temporary hashmap
        temp = {} #Temporary hashmap to count frequency of each character in each string

        result_list = [] #Temporary group of anagram
        result = []
        
        for i in strs:
            for j in i:
                if j not in temp:
                    temp[j] = 1
                else:
                    temp[j] += 1

            temp_list.append(temp)
            temp = {}

        seen = [False] * len(strs)

        for i in range(len(temp_list)):
            if seen[i]: 
                continue
            result_list.append(strs[i])

            for j in range(i+1, len(temp_list)):
                if temp_list[i] == temp_list[j]:
                    result_list.append(strs[j])
                    seen[i] = True
                    seen[j] = True

            result.append(result_list)
            result_list = []

        return result
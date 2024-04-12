# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """

#          if len(strs) == 0:
#             return [strs]
        # creates a map to store answers
        # key will be string after converting array to string
#         answerMap = {}

        # create the unique signature of characters by using a-z alphabets
#         for word in strs:
#             key_signature = [0] * 26
            
            # for each character, increase the frequency using ASCII ord() 
#             for char in word:
#                 index_position = ord(char) - ord('a')
#                 key_signature[index_position] += 1
            
            # get the unique signature from the array
            # if it is anagram, it will have the same signature
#             key_signature = ' '.join(str(char) for char in key_signature)

#             if key_signature in answerMap:
#                 answerMap[key_signature].append(word)
#             else:
#                 answerMap[key_signature] = [word]
        
#         return answerMap.values()

from collections import defaultdict

## this seems to be a faster approach and less code
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        if len(strs) == 0:
            return [strs]
        
        ## using python libraries to create a dictionary, with value of type arrays
        answerMap = defaultdict(list)

        # similarly, initialize the unique key signature based on ASCII
        for word in strs:
            key_signature = [0] * 26
            
            for char in word:
                key_signature[ord(char) - ord('a')] += 1
            
            # reason for casting the array into tuple is because tuples are immutable
            # in python dictionaries, Keys must be immutable type
            # but this seems take slightly more memory space
            # however, execution time seems to be faster too
            answerMap[tuple(key_signature)].append(word)
        
        return answerMap.values()


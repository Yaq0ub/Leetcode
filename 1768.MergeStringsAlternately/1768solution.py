class Solution:
    def mergeStrings(self, word1: str, word2: str) -> str:
        '''
        Step 1: Initilize a placeholder array for the merged string
        Step 2: Iterate over both strings until we reach the end of both
        Step 3: On each iteration add a character from word1 then word2
        Step 4: return the joined placeholder array as string
        '''

        #Step 1
        merged = []

        #Step 2
        for i in range(max(len(word1), len(word2))):
            #Step 3
            if(i < len(word1)):
                merged.append(word1[i])

            if(i < len(word2)):
                merged.append(word2[i])
            print(merged)
        return ''.join(merged)


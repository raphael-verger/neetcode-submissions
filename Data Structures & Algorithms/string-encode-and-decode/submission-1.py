class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for s in strs:
            result+= str(len(s)) + '#' + s
        return result



    def decode(self, s: str) -> List[str]:
        result=[]
        pointer=0
        while(pointer<len(s)):
            s_length=''
            c = s[pointer]
            while(c!='#'):
                s_length+=s[pointer]
                pointer+=1
                c = s[pointer]
            
            pointer += 1  # Skip the '#' delimiter
            result.append(s[pointer:(pointer+int(s_length))])
            pointer = (pointer+int(s_length))
        return result



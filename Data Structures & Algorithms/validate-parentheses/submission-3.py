class Solution:
    def isValid(self, s: str) -> bool:
        
        stk = []

        for x in s :

            if x == "}" or x == "]" or x == ")" :
                if len(stk) != 0 :
                    match x :
                        case "}" :
                            if stk [-1] != "{":
                                return False
                            else :
                                stk.pop()
                        case "]" :
                            if stk[-1] != "[":
                                return False
                            else :
                                stk.pop()
                        case ")" :
                            if stk[-1] != "(" :
                                return False 
                            else :
                                stk.pop()
                else :
                    stk.append(x)
            else:
                stk.append(x)
        return len(stk) == 0

# #LeetCode Q20 Stack
# class solution:
#     def isValid(self, s:str) -> bool:
#         pair_dict = {")":"(", "}":"{", "]":"["}
#         stack_list = []
#         for char in s:
#             print('char is:', char)
#             if char in pair_dict:
#                 if len(stack_list)==0:
#                     print("closing char is found but stack is empty")
#                     return False
                
#                 top = stack_list[-1]
#                 print("the last (top) one in stack is:", top)

#                 if top != pair_dict[char]:
#                     print("opening is:", top)
#                     print("closing is:", char)
#                     return False
                
#                 stack_list.pop()
#                 print("remove last char", top)
#                 print(stack_list)

#             else:
#                 stack_list.append(char)
#                 print("add char on top")
#                 print(stack_list)
        
#         return True
    
# sol = solution()
# #sol.isValid("[{(3)}]")

##########
#Practice
class solution:
    def isValid(self, s:str) -> bool:
        pair_dict = {")":"(", "}":"{", "]":"["}
        stack_list = []
        for char in s:
            if char in pair_dict.values():
                stack_list.append(char)
                print(stack_list)
            elif char in pair_dict:
                print('char is ',char)
                if len(stack_list) == 0:
                    return False
                elif stack_list[-1] == pair_dict[char]:
                    print(stack_list[-1])
                    print(pair_dict[char])
                    stack_list.pop()
                else:
                    print("It's false")
                    return False

            else:
                print("continue")
                continue

        print(stack_list)
        print('Hello')
        print(len(stack_list)==0)
        return len(stack_list)==0
    
sol = solution()
#sol.isValid("[{(3)}]")
sol.isValid("(()")
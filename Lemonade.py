class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cnt5 = 0
        cnt10 = 0
        cnt20 = 0
        for i in bills:
            if(i == 5):
                cnt5 += 1
            elif(i == 10):
                if (cnt5 > 0):
                    cnt5 -= 1
                    cnt10 += 1
                else: 
                    return False
            elif(i == 20):
                if((cnt10 > 0) and (cnt5 > 0)):
                    cnt10 -= 1
                    cnt5 -= 1
                elif(cnt5 >= 3):
                    cnt5 -= 3
                else:
                    return False
        return True
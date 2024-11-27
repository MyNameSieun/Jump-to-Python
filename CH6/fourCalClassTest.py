# fourCalClassTest.py
from FourCal import FourCal

class SafeFourCal(FourCal):
    def div(self):
        if self.second==0: # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second 

a=SafeFourCal(4,0)
print(a.div()) # 0
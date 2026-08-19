# Pair of Elements

class PairofElements:
    def twosum(self,num1,target):
        vlookup = {}
        sum = 0
        for index,value in enumerate(num1):
            sum = sum + value
            print(sum)
            vlookup[index] = sum
            if sum >= target:
                print(vlookup)
                return index
        return False

num = (10,20,30,40,50,607,80)
target = 120
obj1 = PairofElements()
print("The index number for the given ",obj1.twosum(num,target))
class Solution:
    def intToRoman(self, num: int) -> str:
        nums = list(map(int, str(num)))
        res = ''
        relate ={
            0: 'I',
            0.5: 'V',
            1: 'X',
            1.5: 'L',
            2: 'C',
            2.5: 'D',
            3:'M'
        }
        for i in range(len(nums)):
            place = (len(nums) - 1) - i 
            if nums[i] < 4:
                res += relate[place] * nums[i]
            elif nums[i] > 4:
                if nums[i] == 5:
                    res += relate[place+0.5] 
                else:
                    if nums[i] == 9:
                        res += relate[place] + relate[place + 1]
                    else:
                        res += relate[place+0.5] +(relate[place] * (nums[i] - 5))
            else:
                res +=  relate[place] + relate[place + 0.5]
                
        return res
        
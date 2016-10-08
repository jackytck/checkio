#!/usr/bin/python
def checkio(stair_values):
    dp1 = stair_values[0]
    if len(stair_values) == 1:
        return 0 if dp1 < 0 else dp1
    dp2 = max(dp1 + stair_values[1], stair_values[1])
    stair_values.append(0)
    for i in range(2, len(stair_values)):
        dp1, dp2 = dp2, max(dp1 + stair_values[i], dp2 + stair_values[i])
    return dp2

if __name__ == '__main__':
   assert checkio([5,6,-10,-7,4]) == 8, 'First'
   assert checkio([-11, 69, 77, -51, 23, 67, 35, 27, -25, 95])==393, 'Second'
   assert checkio([-21, -23, -69, -67, 1, 41, 97, 49, 27])==125, 'Third'
   assert checkio([5,-3,-1,2]) == 6, 'Fifth'
   print('All ok')

class Solution(object):
    def maxProfit(self, inventory, orders):
        """
        :type inventory: List[int]
        :type orders: int
        :rtype: int
        """
        iYu = 1000000000+7
        newList = sorted(inventory, reverse=True)
        newList.append(0)

        iIndex = 0
        iSubSum = 0
        while iIndex < len(newList) - 1:
            iThis = newList[iIndex]
            iNext = newList[iIndex+1]
            iSub = iThis - iNext
            if iSubSum + (iIndex+1)*iSub <= orders:
                iSubSum += (iIndex+1)*iSub
                iIndex += 1
            else:
                break
        
        iLast = newList[iIndex] + 1
        
        iNewIndex = 0

        iSum = 0
        iOrders = 0
        while iNewIndex < iIndex:
            iSum += (iLast+newList[iNewIndex])*(newList[iNewIndex]-iLast+1)/2
            iOrders += (newList[iNewIndex]-iLast+1)
            iNewIndex += 1
        
        iSubOrder = orders - iOrders
        iDiv = iSubOrder/(iIndex+1)
        iMod = iSubOrder%(iIndex+1)

        iSum += (iIndex+1)*((newList[iIndex] + newList[iIndex] - iDiv + 1)*iDiv/2)

        iSum += (iMod*(newList[iIndex]-iDiv))

        return iSum%iYu

# 作者：XvarX
# 链接：https://leetcode-cn.com/problems/sell-diminishing-valued-colored-balls/solution/jie-ji-ya-fa-by-xvarx-mw3e/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
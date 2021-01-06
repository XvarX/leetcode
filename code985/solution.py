class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        lstResult = []
        iTempSum = 0
        for iTemp in A:
            if iTemp % 2 == 0:
                iTempSum += iTemp
        for tempInfo in queries:
            iVal = tempInfo[0]
            iIndex = tempInfo[1]

            iOldValue = A[iIndex]
            A[iIndex] += iVal

            if iOldValue % 2 == 1:
                if A[iIndex] % 2 == 0:
                    iTempSum += A[iIndex]
            else:
                if A[iIndex] % 2 == 0:
                    iTempSum += iVal
                else:
                    iTempSum -= iOldValue
            
            lstResult.append(iTempSum)
        return lstResult
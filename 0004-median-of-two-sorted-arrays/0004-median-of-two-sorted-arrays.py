class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2

        def step(k, n1_start, n1_end, n2_start, n2_end):
            # return the corresponding element in other array because:
            # ran out of elements in nums1 
            if n1_start > n1_end:
                return nums2[k - n1_start]
            # ran out of elements in nums2
            if n2_start > n2_end:
                return nums1[k - n2_start]

            # Get middle indices and values of nums1 and nums2
            mpi_n1, mpi_n2 = (n1_start + n1_end) // 2, (n2_start + n2_end) // 2 # floor
            n1_value, n2_value = nums1[mpi_n1], nums2[mpi_n2]

            # If k is in the right half of nums1 and nums2, remove the ignorable smaller left half
            if k > (mpi_n1 + mpi_n2):
                if n1_value > n2_value:
                    return step(k, n1_start, n1_end, mpi_n2 + 1, n2_end)
                else:
                    return step(k, mpi_n1 + 1, n1_end, n2_start, n2_end)
                
            # If k is in the left half of nums1 and nums2, remove the ignorable larger right half
            else:
                if n1_value > n2_value:
                    return step(k, n1_start, mpi_n1 - 1, n2_start, n2_end)
                else:
                    return step(k, n1_start, n1_end, n2_start, mpi_n2 - 1)

        if n % 2:
            # ODD COUNT ELEMENTS, REMAINDER 1
            return step(k=n // 2, # floor
                        n1_start=0, 
                        n1_end=n1 - 1, 
                        n2_start=0, 
                        n2_end=n2 - 1) 
        else:
            # EVEN COUNT ELEMENTS, REMAINDER 0, return midpoint
            return 0.5 * (
                step(k=n/2 - 1,
                     n1_start=0,
                     n1_end=n1 - 1,
                     n2_start=0,
                     n2_end=n2 - 1) +
                step(k=n/2,
                     n1_start=0, 
                     n1_end=n1 - 1, 
                     n2_start=0, 
                     n2_end=n2 - 1)
            )
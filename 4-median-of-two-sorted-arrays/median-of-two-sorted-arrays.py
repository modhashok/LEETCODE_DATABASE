class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Make sure nums1 is the smaller array (to binary search on it)
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # +1 so it works nicely for odd lengths too

        left, right = 0, m  # binary search on nums1 indices

        while left <= right:
            i = (left + right) // 2          # cut position in nums1
            j = half - i                     # cut position in nums2

            # Handle edges with +/- infinity
            left1  = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i]     if i < m else float('inf')

            left2  = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j]     if j < n else float('inf')

            # Check if we have a correct partition
            if left1 <= right2 and left2 <= right1:
                # We found the perfect partition
                if total % 2 == 1:
                    # Odd length -> median is max of left side
                    return float(max(left1, left2))
                else:
                    # Even length -> average of middle two
                    return (max(left1, left2) + min(right1, right2)) / 2.0

            elif left1 > right2:
                # We went too far right in nums1, move left
                right = i - 1
            else:
                # We went too far left in nums1, move right
                left = i + 1

        # This should never be hit if input constraints are valid
        raise ValueError("Input arrays are not valid")

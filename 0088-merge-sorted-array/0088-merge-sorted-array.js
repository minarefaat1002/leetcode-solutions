/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
        let i = m-1;
        let j = n-1;
        while (i>=0 && j>=0){
            if (nums2[j] > nums1[i]) nums1[i+j+1] = nums2[j--];
            else nums1[i+j+1] = nums1[i--];
        }
        if (j>=0) for(let x = j; x >= 0;x--) nums1[x] = nums2[x];
};
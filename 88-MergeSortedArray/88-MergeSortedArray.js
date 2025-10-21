// Last updated: 10/21/2025, 2:03:27 PM
/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var c;
var merge = function(nums1, m, nums2, n) {
    nums1.length=m;
    while(nums2.length>0){
        c=0;
        while(nums2[0]>nums1[c]){
            if(nums2[0]<nums1[c]) {break;}
            c+=1;
        }
        nums1.splice(c,0,nums2[0]);
        nums2.shift();
    }
};
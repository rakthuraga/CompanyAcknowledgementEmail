#include <iostream>
#include <vector>
int slidingWindow(const std::vector<int>& nums, int k);

int main() {

  std::vector<int> nums = {10,5,2,6};
  int k = 100;
  int biggestLength = slidingWindow(nums, k);
  std::cout << biggestLength << std::endl;
}

int slidingWindow(const std::vector<int>& nums, int k) {
  int left = 0;
  int right = 0;
  int counter = 0;
  int current = 0;

  for (right = 0; right < nums.size(); right++) {
    if(right == 0)
    {
      current += nums[right];
    }
    else
    {
      current *= nums[right];
    }

    while (current >= k) {
      current /= nums[left];
      left++;
      
    }

    if(current < k)
      {
        counter += ((right - left) + 1);
      } 
  }

  return counter;
}
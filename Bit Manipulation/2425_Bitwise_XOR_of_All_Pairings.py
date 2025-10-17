def xor_all_pairings(nums1, nums2):
    # Write Code
    result = 0
    if len(nums1) % 2 == 1:
        for n in nums2:
            result ^= n
        
    if len(nums2) % 2 == 1:
        for n in nums1:
            result ^= n

    return result


# Test
def run_tests():
    test_cases = [
        ([2,1,3], [10,2,5,0], 13),
        ([1,2], [3,4], 0),
        ([0], [0], 0),
        ([1, 1, 1], [1, 1, 1], 0),
        ([1], [2, 3, 4], 4),
    ]
    
    for i, (nums1, nums2, expected) in enumerate(test_cases):
        try:
            result = xor_all_pairings(nums1, nums2)
            assert result == expected
            print(f"✅ Test case {i+1} passed")
        except AssertionError:
            print(f"❌ Test case {i+1} failed: Expected {expected}, got {result}")
        except Exception as e:
            print(f"💥 Test case {i+1} error: {str(e)}")

run_tests()

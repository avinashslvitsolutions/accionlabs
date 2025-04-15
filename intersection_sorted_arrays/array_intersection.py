from typing import List

class SortedArrayIntersection:
    
    def __init__(self, arr1: List[int], arr2: List[int]):
        """
        Initialize the intersector with two sorted arrays.
        """
        self.arr1 = arr1
        self.arr2 = arr2
        self._validate_input()
        self.intersection = None
    
    def _validate_input(self):
        """Validate that input arrays are sorted in non-decreasing order."""
        for i in range(len(self.arr1) - 1):
            if self.arr1[i] > self.arr1[i + 1]:
                raise ValueError("First array is not sorted")
                
        for i in range(len(self.arr2) - 1):
            if self.arr2[i] > self.arr2[i + 1]:
                raise ValueError("Second array is not sorted")
    
    def find_intersection(self) -> List[int]:
        """
        Find the intersection of the two sorted arrays without duplicates.
        """
        if self.intersection is not None:
            return self.intersection
            
        result = []
        i, j = 0, 0
        len1, len2 = len(self.arr1), len(self.arr2)
        
        while i < len1 and j < len2:
            if self.arr1[i] < self.arr2[j]:
                i += 1
            elif self.arr1[i] > self.arr2[j]:
                j += 1
            else:
                # Found common element
                if not result or result[-1] != self.arr1[i]:
                    result.append(self.arr1[i])
                i += 1
                j += 1
        
        self.intersection = result
        return result


def get_sorted_array(prompt: str) -> List[int]:
    """
    Helper function to get and validate a sorted array from user input.
    
    If input cannot be converted to integers or if array isn't sorted
    """
    while True:
        try:
            input_str = input(prompt)
            if not input_str.strip():
                return []
            
            arr = list(map(int, input_str.split()))
            # Verify the array is sorted
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    raise ValueError("Array must be sorted in non-decreasing order")
            return arr
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


if __name__ == "__main__":
    print("Find Intersection of Two Sorted Arrays")
    print("Enter elements separated by spaces (e.g., '1 2 3 4')")
    print("Note: Arrays must be sorted in non-decreasing order\n")
    
    try:
        # Get user input for both arrays
        arr1 = get_sorted_array("Enter first sorted array: ")
        arr2 = get_sorted_array("Enter second sorted array: ")
        
        # Find and display intersection
        intersector = SortedArrayIntersection(arr1, arr2)
        common_elements = intersector.find_intersection()
        
        print("\nResults:")
        print(f"Array 1: {arr1}")
        print(f"Array 2: {arr2}")
        print(f"Intersection: {common_elements}")
        
    except ValueError as e:
        print(f"Error: {e}")

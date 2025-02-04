# QuickSelect and Median of Medians

This repository contains implementations of two well-known selection algorithms:

1. **QuickSelect** – An efficient algorithm for finding the k-th smallest element in an unsorted list using a randomized pivot selection.
2. **Median of Medians (MoM)** – A more robust selection algorithm that provides a worst-case linear time complexity.

## Features
- Implements QuickSelect for fast k-th order statistics retrieval.
- Implements the Median of Medians algorithm to ensure a more balanced pivot selection.
- Compares execution times of the two algorithms against sorting-based selection.
- Supports large input sizes (up to hundreds of millions of elements).

## Algorithm Details

### QuickSelect
- Works similarly to QuickSort but only recurses on the relevant partition.
- Uses a random pivot to divide the input list into three sublists:
  - Elements smaller than the pivot.
  - Elements equal to the pivot.
  - Elements greater than the pivot.
- Recursively processes the relevant partition until the k-th smallest element is found.

### Median of Medians (MoM)
- Divides the array into chunks of size `k`.
- Computes the median of each chunk and recursively selects the median of medians.
- Partitions the original array based on the selected pivot and finds the k-th order statistic.
- Provides worst-case **O(n)** time complexity.

## Performance Comparison
The script compares the performance of:
1. **QuickSelect**
2. **Median of Medians**
3. **Sorting-based Selection**

Execution times are printed for large input sizes.

## Usage
### Running the Script
Execute the script using Python:
```bash
python3 selection_algorithms.py
```

### Example Output
```
15 th largest from mom:  98765432   Time:  0.35s
15 th largest from sort: 98765432   Time:  1.02s
15 th largest from select: 98765432   Time:  0.15s
MOM-Sort Ratio:  0.34
```

## Dependencies
- Python 3.x
- NumPy (for generating large random datasets)

Install dependencies using:
```bash
pip install numpy
```

## Notes
- The implementation handles large datasets efficiently.
- QuickSelect is generally faster but can have poor performance in the worst case.
- Median of Medians is slower in practice but guarantees worst-case **O(n)** performance.

## License
This project is open-source and available under the MIT License.
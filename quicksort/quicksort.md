p.153 algo 1 

Problem 5.6 Implement the QuickSort algorithm in your favorite programming language. Experiment with the performance of diﬀerent ways of choosing the pivot element.

One approach is to keep track of the number of comparisons between input array elements made by QuickSort. 31 For several diﬀerent input arrays, determine the number of comparisons made with the following implementations of the ChoosePivot subroutine:

1. Always use the ﬁrst element as the pivot.

2. Always use the last element as the pivot.

3. Use a random element as the pivot. (In this case you should run the algorithm 10 times on a given input array and average the results.)

4. Use the median-of-three as the pivot element. The goal of this rule is to do a little extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.

In more detail, this implementation of ChoosePivot considers the ﬁrst, middle, and ﬁnal elements of the given array. (For an array with even length 2k, use the kth element for the “middle” one.) It then identiﬁes which of these three elements is the median (i.e., the one whose value is in between the other two), and returns this as the pivot.32 

For example, with the input array

8 3 2 5 1 4 7 6

the subroutine would consider the ﬁrst (8), middle (5), and last (6) elements. It would return 6, the median of the set { 5, 6, 8 } , as the pivot element.

See www.algorithmsilluminated.org for test cases and challenge data sets.
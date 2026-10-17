/**
 * Merge Sort in Java (JDK 17+)
 * 
 * Time Complexity: O(n log n)
 * Space Complexity: O(n)
 */

package sorting;

public class MergeSort {

    public static void sort(int[] arr) {
        if (arr == null || arr.length <= 1) return;
        int[] helper = new int[arr.length];
        mergeSort(arr, helper, 0, arr.length - 1);
    }

    private static void mergeSort(int[] arr, int[] helper, int left, int right) {
        if (left >= right) return;
        int mid = left + (right - left) / 2;
        // TODO: mergeSort(arr, helper, left, mid);
        // TODO: mergeSort(arr, helper, mid + 1, right);
        // TODO: merge(arr, helper, left, mid, right);
    }

    private static void merge(int[] arr, int[] helper, int left, int mid, int right) {
        // TODO: Copy to helper array
        // TODO: Merge back into arr[left..right]
    }

    public static void main(String[] args) {
        int[] arr = {38, 27, 43, 3, 9, 82, 10};
        // sort(arr);
    }
}

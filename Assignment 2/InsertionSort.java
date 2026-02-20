import java.util.*;
public class InsertionSort {
    public static void main (String args[]) {
		Scanner scan = new Scanner(System.in);

		int size = scan.nextInt();

		int arr[] = new int[size];

		for (int index = 0; index < size; index++)
			arr[index] = scan.nextInt();

		for (int i = 1; i < size; i++) {
			int key = arr[i];
			int j = i - 1;

			while (j >= 0 && key < arr[j]) {
				arr[j + 1] = arr[j];
				j--;
			}

			arr[j + 1] = key;
		}	

		for (int i = 0; i < size; i++)
			System.out.print(arr[i] + " ");

        scan.close();
    }
}
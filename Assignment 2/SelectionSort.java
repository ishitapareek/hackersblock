import java.util.*;
public class SelectionSort {
    public static void main (String args[]) {
		Scanner scan = new Scanner(System.in);

		int size = scan.nextInt();

		int arr[] = new int[size];

		for (int i = 0; i < size; i++)
			arr[i] = scan.nextInt();

		for (int i = 0; i < size - 1; i++) {
			int minIndex = i;

			for (int j = i + 1; j < size; j++) {
				if (arr[j] < arr[minIndex]) 
					minIndex = j;
			}

			int temp = arr[i];
			arr[i] = arr[minIndex];
			arr[minIndex] = temp;
		} 

		for (int i = 0; i < size; i++) 
			System.out.print(arr[i] + " ");

    }
}
import java.util.*;
public class BubbleSort {
    public static void main (String args[]) {
		Scanner scan = new Scanner(System.in);
		int size = scan.nextInt();

		int arr[] = new int[size];

		for (int i = 0; i < size; i++) 
			arr[i] = scan.nextInt();

		for (int i = 0; i < size - 1; i++) {
			boolean hasBeenSwapped = false;
			for (int j = 0; j < size - i - 1; j++) {
				if (arr[j] > arr[j + 1]) {
					int temp = arr[j];
					arr[j] = arr[j + 1];
					arr[j + 1] = temp;
					hasBeenSwapped = true;
				}
			}
			if (hasBeenSwapped == false)
				break;
		}

		for (int i = 0; i < size; i++) 
			System.out.print(arr[i] + " ");  

		scan.close();
    }
}  
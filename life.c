#include stdio.h
#include stdlib.h
#include math.h


int main()
{
    int num = 0, i  = 0;
    int arr[INT_MAX];

    while(num != 42){
     scanf(%d,&num);
     arr[i] = num;
     i++;
    }
    quickSort(arr,arr[0],arr[i])
    while(j != i){
        printf("%d",arr[j]);
    }

}

void quickSort(arr[], low, high)
{
    if (low < high)
    {
        /* pi is partitioning index, arr[pi] is now
           at right place */
        pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);  // Before pi
        quickSort(arr, pi + 1, high); // After pi
    }
}
int partition (int arr[],int low, int high)
{
    // pivot (Element to be placed at right position)
    pivot = arr[high];  
 
    i = (low - 1)  // Index of smaller element

    for (j = low; j <= high- 1; j++)
    {
        // If current element is smaller than the pivot
        if (arr[j] < pivot)
        {
            i++;    // increment index of smaller element
            swap (arr[i],arr[j]);
        }
    }
    swap (arr[i + 1],arr[high]);
    return (i + 1)
}
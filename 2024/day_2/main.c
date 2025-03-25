#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int* remove_element(int arr[], int *size, int index) {
    // ensure validity
    if (index < 0 || index >= *size) {
        fprintf(stderr, "Index out of bounds\n");
        return NULL;
    }

    // allocate memory for new array
    int* newArr = (int*)malloc((*size - 1) * sizeof(int));
    if (newArr == NULL) {
        fprintf(stderr, "Memory alloc failed\n");
        return NULL;
    }

    int q = 0;
    for (int p = 0; p < *size; p++) {
        if (p != index) {
            newArr[q] = arr[p];
            q++;
        }
    }

    // decrease array size for some reason?
    (*size)--;
    return newArr;
}



void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int asc_or_desc(int a, int b) {
    int asc;

    int c = a - b;
    if (c > 0 && c < 4) {
        asc = 1;
    }
    else if (c < 0 && c > -4) {
        asc = -1;
    }
    else { // = 0
        asc = 999;
    }
    return asc;

}

int safe_or_unsafe(int arr[] , int i, int dampener)
{   
    
    // take the string and process if its safe or not
    int asc = 0; // 0 = default, 1 = asc, -1 = desc
    int asc_2 = 0; // for the second time round
    int* newArr; // just in case cause its stupid
    for (int j = 1; j < i; j++) {
        if (j == 1) {
            asc = asc_or_desc(arr[j-1], arr[j]);
            asc_2 = asc;
        } 
        else {
            asc_2 = asc_or_desc(arr[j-1], arr[j]);
        }
        /*
        // In case of first loop, extract comparison
        if (j == 1) {
           printf("First loop through\n");
           asc = asc_or_desc(arr[j], arr[j - 1]); 
           asc_2 = asc; 
        } // All other cases, compare asc_2 to asc 
        else if (j > 1) {
           asc_2 =  asc_or_desc(arr[j], arr[j - 1]); 
        }*/
        // If they don't align, check the next set
        if (asc_2 != asc) {
           printf("Non-alignment between i: %d and j: %d\n asc: %d and asc_2: %d\n", arr[j], arr[j-1], asc, asc_2);
          if (dampener == 1) {
                return 1;
           }
           // stupid catch case for if its first element
           if (j == 2 && dampener == 0) {
                int* newArr = remove_element(arr, &i, 0);
                printf("Removing first element\n");
                printArray(newArr, i);
                //printArray(arr, i+1);
                if (safe_or_unsafe(newArr, i, 1) == 0)
                {   
                    printf("First element removal worked!\n");
                    return 0;
                }
                printf("First element removal didn't work, continuing with normal method...\n=======================");
                // saving the array later from destruction (stupid coding)
                i += 1;
           }

           // stupid catch case for if its last element
           if (j == (i - 1)) {
                printf("Removing last element\n");
                int* newArr = remove_element(arr, &i, i-1);
                printArray(newArr, i);
                if (safe_or_unsafe(newArr, i, 1) == 0)
                {   
                    printf("Last element removal worked!\n");
                    return 0;
                }
                printf("Last element removal didn't work, continuing with normal method...\n=======================");
                // saving the array later from destruction (stupid coding)
                i += 1;

                 
           }


           int* newArr = remove_element(arr, &i, (j-1));
          
           printf("removed element array now:\n");
           printArray(newArr, i);
           return safe_or_unsafe(newArr, i, 1); 
        }

    }

    // if you make it here, return 0
    return 0;
}



int main() {
    
    int SAFE = 0;
    char report[25];
    int arr[8];
    FILE *file;

    // open file
    //file = fopen("example_input.txt", "r");
    file = fopen("input_1.txt", "r");
    // read in
    if (file != NULL)
    {
        while (fgets(report, sizeof(report), file)) {
            printf("%s", report);

            int i = 0;
            char *token = strtok(report, " ");           
            // if shit broke, go to next iteration
            if (atoi(token) == 0) {
                printf("DEAD CHANNEL CONTINUE\n");
                continue;    
            }
            while (token != NULL) {
                // place in array for comparisons
                arr[i] = atoi(token);
                i++;
                token = strtok(NULL, " ");
            }
            if (safe_or_unsafe(arr, i, 0) == 0) {
                printf("SAFE\n");
                SAFE +=1;
                printf("Safe value %d\n", SAFE);
            }
            else {
                printf("UNSFE\n");
            }
            printf("=====================\n\n");
                    
        }

        // close
        fclose(file);
    }
    else
    {
        fprintf(stderr, "File broke\n");
    }

    printf("\nNUMBER OF SAFE: %d\n", SAFE);
    return 0;
}

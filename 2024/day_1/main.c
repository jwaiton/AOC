#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
       
    int *list1 = NULL;
    int *list2 = NULL;
    int *comparison_list = NULL;
    int count = 0;
    int num1, num2;
    FILE *file;
    
    // open file
    file = fopen("input_1.txt", "r");
    if (file == NULL) {
        // return error if file opening fails
        fprintf(stderr, "Could not open the file.\n");\
        return 1;
    }

    // allocate memory dynamically to take all the data
    list1 = (int *)malloc(sizeof(int)); // 1 element
    list2 = (int *)malloc(sizeof(int)); // 1 element
     
    if (list1 == NULL || list2 == NULL) {
        // check for memory allocation failure
        fprintf(stderr, "Memory allocation failed.\n");
        return 1;
    }
    while (fscanf(file, "%d   %d", &num1, &num2) == 2) {
        // resize arrays
        list1 = (int *)realloc(list1, (count + 1) * sizeof(int));
        list2 = (int *)realloc(list2, (count + 1) * sizeof(int));


        if (list1 == NULL || list2 == NULL) {
            // check for memory allocation failure
            fprintf(stderr, "Memory allocation failed.\n");
            fclose(file);
            return 1;
        }
        
        // store in lists
        list1[count] = num1;
        list2[count] = num2;
        count++;

        printf("Read: %d %d\n", num1, num2); 
    }

    // close the file
    fclose(file);

    printf("First elements (list1):\n");
    for (int i = 0; i < count; i++) {
        printf("%d", list1[i]);
    }
    printf("\n");

    printf("Second elements (list2):\n");
    for (int i = 0; i < count; i++) {
        printf("%d", list2[i]);
    }
    printf("\n\n");

    // sort
    qsort(list1, count, sizeof(int), comp);
    qsort(list2, count, sizeof(int), comp);

    printf("Sorted elements (list1):\n");
    for (int i = 0; i < count; i++) {
        printf("%d", list1[i]);
    }
    printf("\n");

    printf("Sorted elements (list2):\n");
    for (int i = 0; i < count; i++) {
        printf("%d", list2[i]);
    }

    printf("\n\n");
    //free(list1);
    //free(list2);
    // take the comparison
    comparison_list = (int *)malloc(count * sizeof(int)); 
    int total_sum = 0;

    for (int i = 0; i < count; i++) {
        comparison_list[i] = abs(list1[i] - list2[i]);
        total_sum += comparison_list[i];
    }
    printf("Total difference: %d\n", total_sum);
    
    free(list1);
    free(list2);
    free(comparison_list);
    return 0;
} 

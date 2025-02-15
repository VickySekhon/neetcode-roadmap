#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


bool containsDuplicate(int *array, int Len) {
     for (int i = 0; i < Len - 1; i++) {
          for (int j = i + 1; j < Len; j++) {
               if (array[i] == array[j]) {
                    return true;
               }
          }
     }
     return false;
}


int main() {

     int *a[] = {1,2,3};

     bool ans = containsDuplicate(a, 3);
     printf("%d\n", ans);

    return 0; 
}
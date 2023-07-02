#include <bits/stdc++.h> 

using namespace std;

long long getInversions(long long *arr, vector<long long> &temp, int low, int mid, int high) {
    long long inv_count = 0;
    int i = low, j = mid + 1, k = low;
    while(i <= mid && j <= high) {
        if(arr[i] <= arr[j]) temp[k++] = arr[i++];
        else {
            temp[k++] = arr[j++];
            inv_count+= mid - i;
        }
    }
    while(i <= mid) temp[k++] = arr[i++];
    while(j <= high) temp[k++] = arr[j++];
    for(int i = low; i <= high; i++) arr[i] = temp[i];
    return inv_count;
}
long long getInversions(long long *arr, vector<long long> &temp, int low, int high) {
    if(low >= high) return 0;
    long long inv_count = 0;
    int mid = (low + high) >> 1;
    inv_count+= getInversions(arr, temp, low, mid);
    inv_count+= getInversions(arr, temp, mid + 1, high);
    return inv_count;
}
long long getInversions(long long *arr, int n){
    // Write your code here.
    vector<long long> temp(n);
    return getInversions(arr, temp, 0, n - 1);
}

int main() {}
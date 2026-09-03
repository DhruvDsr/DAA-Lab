// Program 1: Matrix Multiplication and Strassen's Algorithm

#include <iostream>
#include <vector>
using namespace std;
typedef vector<vector<int>> Matrix;
Matrix multiply(Matrix& A, Matrix& B) {
int n = A.size();
Matrix C(n, vector<int>(n, 0));
for (int i = 0; i < n; i++) {
for (int j = 0; j < n; j++) {
for (int k = 0; k < n; k++) {
C[i][j] += A[i][k] * B[k][j];
}

}
}
return C;
}
int main() {
Matrix A = {{1, 2}, {3, 4}};
Matrix B = {{5, 6}, {7, 8}};
Matrix C = multiply(A, B);
return 0;
}
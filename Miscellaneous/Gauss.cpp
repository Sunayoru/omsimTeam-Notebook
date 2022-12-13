bool gaussJordan(double A[][]) {
    int n = A.length(), m = A[0].length();
    bool singular = false;
    // double determinant = 1;
    for (int i=0, p=0; i<n && p<m; i++, p++) {
        for (int k = i + 1; k < n; k++) {
            if (fabs(A[k][p]) > 1e-9) { // swap
            // determinant *= -1;
            // double t[]=A[i]; A[i]=A[k]; A[k]=t;
                swap(A[i], A[k]);
            break;
            }
        }
        // determinant *= A[i][p];
        if (fabs(A[i][p]) < 1e-9)
            { singular = true; i--; continue; }
        
        for (int j = m-1; j >= p; j--) A[i][j]/= A[i][p];
        
        for (int k = 0; k < n; k++) {
            if (i == k) continue;
            for (int j = m-1; j >= p; j--)
                A[k][j] -= A[k][p] * A[i][j];
        }
    } return !singular; }

// A[0][n]

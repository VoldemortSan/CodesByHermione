#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool isSafe(int board[][10], int row, int col, int n) {
    // check if there is a queen in the same row
    for (int i = 0; i < n; i++) {
        if (board[row][i] == 1) {
            return false;
        }
    }
    // check if there is a queen in the same column
    for (int i = 0; i < n; i++) {
        if (board[i][col] == 1) {
            return false;
        }
    }
    // check if there is a queen on the diagonal
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == 1) {
            return false;
        }
    }
    for (int i = row, j = col; i >= 0 && j < n; i--, j++) {
        if (board[i][j] == 1) {
            return false;
        }
    }
    // it's safe to place a queen at (row, col)
    return true;
}

bool BackTrack(int board[][10], int row, int n, vector<vector<int>>& solutions) {
    if (row == n) {
        vector<int> solution;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                solution.push_back(board[i][j]);
            }
        }
        solutions.push_back(solution);
        return false; // to find all solutions
    }
    bool foundSolution = false;
    for (int col = 0; col < n; col++) {
        if (isSafe(board, row, col, n)) {
            board[row][col] = 1;
            foundSolution = BackTrack(board, row + 1, n, solutions) || foundSolution;
            board[row][col] = 0; // backtrack
        }
    }
    return foundSolution;
}

void solveNQueens(int n) {
    int board[10][10] = {0};
    vector<vector<int>> solutions;
    BackTrack(board, 0, n, solutions);
    if (solutions.empty()) {
        cout << "No solution found." << endl;
    } else {
        cout << "All possible solutions:" << endl;
        for (auto& solution : solutions) {
            for (int i = 0; i < n * n; i++) {
                if (i % n == 0 && i != 0) {
                    cout << endl;
                }
                if (solution[i] == 0) {
                    cout << "_ ";
                } else {
                    cout << "Q ";
                }
            }
            cout << endl << endl;
        }
    }
}

int main() {
    int n;
    cout << "Enter the size of the chessboard: ";
    cin >> n;
    
    solveNQueens(n);
    
    return 0;
}

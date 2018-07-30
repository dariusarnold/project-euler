#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

/**
 * Read the matrix file with filename into a 2D vector
 * @param fileName
 * @param output Reference in which the matrix will be stored
 */
void readMatrixFile(std::string fileName, std::vector<std::vector<int>>& output){
    std::ifstream matrixFile(fileName);
    std::string line;
    std::string num;
    if (matrixFile.is_open()){
        // read a line, ending on newline
        while (std::getline(matrixFile, line)) {
            std::vector<int> row;
            std::stringstream ss(line);
            while (std::getline(ss, num, ',')) {
                // break the line on commas, convert to int and append to vector
                row.push_back(std::stoi(num));
            }
            output.push_back(row);
        }
    }
    matrixFile.close();
}

/**
 * Calculate minimal path in matrix by adding the values along backwards.
 * @param matrix
 * @return git reset 
 */
int calcMinimalPath(std::vector<std::vector<int>>& matrix){
    // calculate lowest row
    int row = matrix.size() - 1;
    for (int col = matrix[0].size()-2; col >= 0; col--){
        matrix[row][col] += matrix[row][col+1];
    }
    // calculate left most row
    int col = matrix[0].size() - 1;
    for (int row = matrix.size()-2; row >= 0; row--){
        matrix[row][col] += matrix[row+1][col];
    }
    // calculate inner rows
    for (int row = matrix.size()-2; row >= 0; row--){
        for (int col = matrix[row].size()-2; col >= 0; col--){
            matrix[row][col] += std::min(matrix[row+1][col], matrix[row][col+1]);
        }
    }
    return matrix[0][0];
}

void printMatrix(const std::vector<std::vector<int>>& matrix){
    for (auto x : matrix){
        for (auto column : x){
            std::cout << column << " ";
        }
        std::cout << std::endl;
    }
}

int main() {
    std::vector<std::vector<int>> matrix;
    readMatrixFile("/home/darius/git/project-euler/081_minimal-path-sum/matrix.txt", matrix);
    std::cout << calcMinimalPath(matrix) << std::endl;
    //printMatrix(matrix);
    return 0;
}
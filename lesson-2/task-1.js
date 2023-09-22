// След матрицы: структурный
const matrix = [
    [1, 2, 3],
    [3, 5, 8],
    [7, 9, 3],
]

let trace = 0;

for (let i = 0; i < matrix.length; i++) {
    trace += matrix[i][i];
}
console.log(trace);

// След матрицы: процедурный
function getTrace(matrix) {
    const diagonalLength =
     matrix.length < matrix[0].length ? matrix.length : matrix[0].length;
    let trace = 0;

    for (let i = 0; i < diagonalLength; i++) {
        trace += matrix[i][i];
    }
    return trace;
};

const matrixTwo = [
    [1, 2, 3],
    [3, 5, 8],
    [7, 9, 3],
    [17, 19, 3],
];

console.log(getTrace(matrixTwo));
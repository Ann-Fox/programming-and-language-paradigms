// Структурный
let decimalNumber = 14;
let result = "";

while (decimalNumber > 0) {
    result = decimalNumber % 2 + result;
    decimalNumber = Math.floor(decimalNumber / 2);
}
console.log('solution - structure');
console.log(result);

// Процедурный метод
function decimalToBinary(decimal) {
    let result = "";

    while (decimal > 0) {
        result = decimal % 2 + result;
        decimal = Math.floor(decimal / 2);
    }  
    return result;
}

let decimalNum = 14;

console.log('solution - procedure');
console.log(decimalToBinary(decimalNum));
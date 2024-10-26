function filter(numberArr) {
    let evenNUmbers = [];
    for(let i of numberArr) {
        if (numberArr[i] % 2 === 0) {
            evenNUmbers.push(numberArr[i]);
        }
    }
    return evenNUmbers;
}

console.lof(filter([1, 2, 3, 4, 5, 6, 7,]))
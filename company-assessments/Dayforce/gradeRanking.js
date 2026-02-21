// rank the grades below (should return: [2,2,2,1,5])
//const grades: number[] = [75,75,75,96,23];
const grades = [96, 75, 75, 75, 96, 23];
//                       [1, 3, 3, 3,,1 , 6]
// const newArr: number[] = new Array(grades.length).fill(0);
const newArr = [...Array(grades.length).keys()];
const uniqueGrades = new Set(grades);
let map = {};
let size = uniqueGrades.size + 1;
for (let i = 1; i < size; i++) {
    let highest = Math.max(...uniqueGrades);
    map[i] = highest;
    uniqueGrades.delete(highest);
}
console.log(map);
let currentRank = 1;
for (let rank in map) {
    const grade = map[rank];
    // more than one same grade
    if (grades.filter((x) => x === grade).length > 1) {
        console.log(grade, currentRank);
        if (currentRank > Number(rank)) {
            rank = String(currentRank);
        }
        for (let i = 0; i < grades.length; i++) {
            if (grades[i] === grade) {
                newArr[i] = Number(rank);
                currentRank++;
            }
        }
        // one grade
    }
    else {
        console.log(currentRank);
        if (currentRank > Number(rank)) {
            newArr[grades.indexOf(grade)] = currentRank;
            currentRank++;
        }
        else {
            newArr[grades.indexOf(grade)] = Number(rank);
            currentRank = Number(rank) + 1;
        }
    }
}
console.log(newArr);

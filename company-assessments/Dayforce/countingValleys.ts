function countingValleys(steps: number, path: string) {
     let level: number = 0;
     let valleys: number = 0;
     let down: boolean = false;
     for (let i = 0; i < steps; i++) {
          if (level === 0) {
               if (path[i] === "D") {
                    down = true;
               } else {
                    down = false;
               }
          }
          if (path[i] === "D") {
               level--;
          } else {
               level++;
          }
          if (level === 0 && down) {
               valleys += 1;
          }
     }
     return valleys;
}
/* 
function countingValleys(steps: number, path: string) {
     let stepsDown: number = 0;
     let stepsUp: number = 0;
     let i: number = 0;

     while (i < steps) {
          if 
     }
     
          if (path[i] === "D") {
               level--;
          } else {
               level++;
          }
     
}
 */
let x = countingValleys(8, "DDUUUUDD");
console.log(x);
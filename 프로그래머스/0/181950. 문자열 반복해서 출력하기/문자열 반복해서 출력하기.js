const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    str = input[0];
    n = Number(input[1]);
    var ans = str;
    for (var i=0; i<n-1; i++){
        ans = ans + str;
    }
    console.log(ans)
});
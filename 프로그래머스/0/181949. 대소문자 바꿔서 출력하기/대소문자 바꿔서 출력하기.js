const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    var ans = '';
    for (var i=0; i<str.length; i++){
        if (str[i] === str[i].toUpperCase()){
            ans = ans + str[i].toLowerCase();
        }
        else {
            ans = ans + str[i].toUpperCase();
        }
    }
    console.log(ans);
});
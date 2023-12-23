/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    s = s.split(' ')
    s = s.filter(st => st != '')
    res = s[s.length - 1]
    for(let i = s.length - 2; i >= 0; i--){
        if(s[i] !== ''){
            res += ' ' + s[i]
        }
    }
    return res
};
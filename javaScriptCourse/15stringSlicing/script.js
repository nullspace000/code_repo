//string.slice(start, end)
//end excludes the las character 
//const fullName = 'david coleman';

//let firstName = fullName.slice(0, 5);
//console.log(firstName);
//let lastName = fullName.slice(6);
//console.log(lastName);

//let fistChar = fullName.slice(0,1);
//console.log(firstName);
//let lastChar = fullName.slice(-1);
//console.log(lastChar);

const fullName = 'David Martinez';

let firstName = fullName.slice(0,fullName.indexOf(' '));
let lastName = fullName.slice(fullName.indexOf(' ') + 1, ); //we dont need a closing index since we want the last character
console.log(firstName);
console.log(lastName);

const email = 'david.martinez@gmail.com';
let username = email.slice(0, email.indexOf('@'));
console.log(username);

let extention = email.slice(email.indexOf('@') + 1, );
console.log(extention);
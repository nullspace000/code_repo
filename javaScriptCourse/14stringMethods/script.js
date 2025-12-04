let userName = 'david ';
console.log(userName.charAt(0));
console.log(userName.indexOf('d'));
console.log(userName.lastIndexOf('d'));
console.log(userName.length);
console.log(userName.startsWith(' '));

let endsWithSpace = userName.endsWith(' ');
if(endsWithSpace == true){
    userName = userName.trim();
}

let includesSpace = userName.includes(' ');
if(includesSpace == true){
    console.log("your username can't include empty spaces!");
}

userName = '   david  ';
userName = userName.trim();
console.log(userName);

userName = userName.toUpperCase();
console.log(userName);

userName = userName.repeat(3);
console.log(userName);

let phoneNumber = "123-456-789";
phoneNumber = phoneNumber.replaceAll('-','/');
console.log(phoneNumber);

//pad start of string with '0' untill the string is 20 characters long
phoneNumber = phoneNumber.padStart(20, '0');
console.log(phoneNumber);
//padEnd does the same but at the end
phoneNumber = phoneNumber.padEnd(30, '0');
console.log(phoneNumber);



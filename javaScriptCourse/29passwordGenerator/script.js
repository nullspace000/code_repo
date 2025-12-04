function generatePassword(passwordlength, includeLowercase, includeUppercase, includeNumbers, includeSymbols ){

    const lowercaseChars = 'abcdefghkjylmnopqrxruvwxyz';
    const uppercaseChars = 'ABCDEFGHKJYLMNOPQRXRUVWXYZ';
    const numberChars = '1234567890';
    const symbolChars = '!@#$%&*()_+-=[]{};":/?.>,<';
    
    let allowedChars = '';
    let password = '';

    allowedChars += includeLowercase ? lowercaseChars: '';
    allowedChars += includeUppercase ? uppercaseChars: '';
    allowedChars += includeNumbers ? numberChars: '';
    allowedChars += includeSymbols ? symbolChars : '';

    for(let i=0;i<=passwordlength;i++){
        password = password + allowedChars[Math.floor(Math.random() * allowedChars.length)]; 
    }

    return password;
}

const passwordlength = 12;
const includeLowercase = true;
const includeUppercase = true;
const includeNumbers = true;
const includeSymbols = true;

const password = generatePassword(passwordlength, includeLowercase, includeUppercase, includeNumbers, includeSymbols );

console.log(`Generated password: ${password}`);


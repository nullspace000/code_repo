//take user username
// trim spaces
// make first letter uppercase
// make the rest of the characters lowercase
// display output


let username = 'undefined'; 
const submitBtn = document.getElementById('submitBtn');

// WITH NO METHOD CHAINING
submitBtn.onclick = function(){
    username = document.getElementById("userInput").value;    
    console.log(username);

    username = username.trim();
    console.log(username);

    let firstLetter = username.charAt(0);
    firstLetter = firstLetter.toUpperCase();
    console.log(firstLetter);

    username = username.slice(1, );
    console.log(username);

    username = username.toLowerCase();
    console.log(username);

    username = firstLetter + username;
    console.log(username);
}


// WITH METHOD CHAINING
submitBtn.onclick = function(){
    username = document.getElementById("userInput").value;
    username = username.trim().charAt(0).toUpperCase() + username.slice(1,).toLowerCase();    
    console.log(username);
}
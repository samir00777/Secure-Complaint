function validatePassword()
  {
    // alert("Validating Password");
    p=document.getElementById("pass").value;
    const regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).*$/;

    // if (p.length < 8) 
    // {
        if(regex.test(p))
        {
            alert("Valid Password");
        }
        else
        {
            alert("wrong password")
        }
    // }
    // else
    // {
    //     alert("Password must be at least 8 characters long.");
    // }
}
// let checks = 0;
// if (/[a-z]/.test(password)) checks++;       // lowercase
// if (/[A-Z]/.test(password)) checks++;       // uppercase
// if (/[0-9]/.test(password)) checks++;       // number
// if (/[!@#$%^&*]/.test(password)) checks++;  // special char

// if (checks < 3) return false;


// if (/(.)\1\1/.test(password)) return false;

// return true;



// console.log(validatePassword("Aa1!abcd"));   // true
// console.log(validatePassword("aaaAAA11"));   // false (3 same chars)
// console.log(validatePassword("abc123"));
//      // false (length < 8)
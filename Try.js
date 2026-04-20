function validatePassword(event) {
    event.preventDefault();

    const password = document.getElementById("password").value;

    if (password.length < 8) {
        alert("❌ Password must be at least 8 characters long");
        return false;
    }

    let checks = 0;
    if (/[a-z]/.test(password)) checks++;        // lowercase
    if (/[A-Z]/.test(password)) checks++;        // uppercase
    if (/[0-9]/.test(password)) checks++;        // number
    if (/[!@#$%^&*]/.test(password)) checks++;  // special char

    if (checks < 3) {
        alert("❌ Password must contain at least 3 of:\nLowercase, Uppercase, Number, Special character");
        return false;
    }

    alert("✅ Password is valid!");
    return true;
}
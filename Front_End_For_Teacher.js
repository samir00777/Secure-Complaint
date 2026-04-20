document.querySelector("form").addEventListener("submit", function (e) {

    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone_no").value.trim();
    const password = document.getElementById("password").value.trim();

    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
      alert("Invalid Email Address");
      e.preventDefault();
      return;
    }

    // Phone number validation (Indian)
    const phonePattern = /^[6-9]\d{9}$/;
    if (!phonePattern.test(phone)) {
      alert("Invalid Phone Number (Must be 10 digits & start with 6-9)");
      e.preventDefault();
      return;
    }

    // Password validation
    const passwordPattern =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    if (!passwordPattern.test(password)) {
      alert(
        "Password must be at least 8 characters and include uppercase, lowercase, number & special character"
      );
      e.preventDefault();
      return;
    }

  });
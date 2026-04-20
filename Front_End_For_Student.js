document.querySelector("form").addEventListener("submit", function (e) {

    let email = document.getElementById("email").value.trim();
    let phone = document.getElementById("phone_no").value.trim();
    let password = document.getElementById("password").value.trim();

    // Email validation
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("Please enter a valid email address");
      e.preventDefault();
      return;
    }

    // Phone validation (India)
    let phoneRegex = /^[6-9]\d{9}$/;
    if (!phoneRegex.test(phone)) {
      alert("Phone number must be 10 digits and start with 6-9");
      e.preventDefault();
      return;
    }

    // Password validation
    let passRegex =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    if (!passRegex.test(password)) {
      alert(
        "Password must contain Uppercase, Lowercase, Number & Special character (min 8 chars)"
      );
      e.preventDefault();
      return;
    }

  });
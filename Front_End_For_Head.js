document.querySelector("form").addEventListener("submit", function (e) {

    const phone = document.querySelector('input[name="Phone_no"]').value.trim();
    const email = document.querySelector('input[name="Email_Id"]').value.trim();
    const password = document.querySelector('input[name="password"]').value.trim();

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert("Invalid Email Address");
      e.preventDefault();
      return;
    }

    // Phone validation (Indian)
    const phoneRegex = /^[6-9]\d{9}$/;
    if (!phoneRegex.test(phone)) {
      alert("Phone number must be 10 digits and start with 6-9");
      e.preventDefault();
      return;
    }

    // Password validation
    const passRegex =
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    if (!passRegex.test(password)) {
      alert(
        "Password must have uppercase, lowercase, number & special character (min 8 chars)"
      );
      e.preventDefault();
      return;
    }

  });
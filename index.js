function setRole(role, btn){
    document.getElementById("option").value = role;

    // active UI
    document.querySelectorAll(".role-box button")
      .forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
}
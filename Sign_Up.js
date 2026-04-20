function roleSelected() {
  document.getElementById("method").classList.remove("hidden");
}

function methodSelected(v) {
  document.getElementById("phoneBox").classList.add("hidden");
  document.getElementById("emailBox").classList.add("hidden");

  if (v === "phone") {
    document.getElementById("phoneBox").classList.remove("hidden");
  } else if (v === "email") {
    document.getElementById("emailBox").classList.remove("hidden");
  }
}
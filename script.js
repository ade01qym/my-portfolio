
/* Welcome message in the browser console */
console.log("Welcome to Adeeba's Portfolio! 🚀");

/* Update the footer year automatically */
const yearElement = document.getElementById("year");

if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
}

/* Mobile navigation menu */
const menuButton = document.getElementById("menu-button");
const navigation = document.getElementById("navigation");

if (menuButton && navigation) {
  menuButton.addEventListener("click", () => {
    const isOpen = navigation.classList.toggle("show");
    menuButton.setAttribute("aria-expanded", isOpen);
  });

  navigation.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      navigation.classList.remove("show");
      menuButton.setAttribute("aria-expanded", "false");
    });
  });
}

/* Back-to-top button */
const topButton = document.getElementById("back-to-top");

if (topButton) {
  topButton.addEventListener("click", () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  });
}

document.addEventListener("DOMContentLoaded", function () {
  const dropdown = document.querySelector(".dropdown");
  const menu = document.querySelector(".dropdown-menu");

  dropdown.addEventListener("mouseenter", () => {
    menu.classList.add("show");
  });

  dropdown.addEventListener("mouseleave", () => {
    menu.classList.remove("show");
  });
});

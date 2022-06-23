// MOBILE NAV MENU ANIMATION
// The .burger div has a click event listener that toggles the .nav-active and .burger-active classes on and off.
const toggleNav = () => {
    const nav = document.querySelector('.nav-links');
    const burger = document.querySelector('.burger');
    // Slide in and out navigation menu
    nav.classList.toggle('nav-active');
    // Toggle burger icon
    burger.classList.toggle('burger-active');
};

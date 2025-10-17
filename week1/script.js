const navMenu = document.querySelector('.nav-menu');
const menuToggle = document.querySelector('.menu-toggle');
const cross = document.querySelector('.cross');


menuToggle.addEventListener('click', () => {
    navMenu.classList.add('active');
});

cross.addEventListener('click', () => {
    navMenu.classList.remove('active');
})

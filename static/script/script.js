function adjustFooter() {
    const footer = document.querySelector('footer');
    if (document.body.scrollHeight <= window.innerHeight) {
        footer.classList.add('fixed-footer');
    } else {
        footer.classList.remove('fixed-footer');
    }
}

window.addEventListener('load', adjustFooter);
window.addEventListener('resize', adjustFooter);

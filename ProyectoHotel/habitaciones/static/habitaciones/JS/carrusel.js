let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("slides")[0];
    let dots = document.getElementsByClassName("dot");
    slides.style.transform = "translateX(" + (-slideIndex * 100) + "%)";
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    dots[slideIndex].className += " active";
    slideIndex++;
    if (slideIndex >= dots.length) { slideIndex = 0; }
    setTimeout(showSlides, 5000); // Cambia la imagen cada 3 segundos
}

function currentSlide(n) {
    slideIndex = n - 1;
    showSlides();
}

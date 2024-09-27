document.addEventListener("DOMContentLoaded", function() {
    const slides = document.querySelectorAll('.slide');
    const dots = document.querySelectorAll('.dot');
    const slidesContainer = document.querySelector('.slides');
    let currentSlideIndex = 0;
    
    // Obtener el campo oculto del formulario para actualizar el habitacion_id
    const habitacionIdInput = document.querySelector('input[name="habitacion_id"]');
    
    // Función para mostrar una diapositiva específica
    function showSlide(index) {
        if (index >= slides.length) {
            currentSlideIndex = 0;  // Volver al inicio si el índice excede el número de slides
        } else if (index < 0) {
            currentSlideIndex = slides.length - 1;  // Ir al último si el índice es negativo
        } else {
            currentSlideIndex = index;
        }

        // Mover las slides con animación
        slidesContainer.style.transform = `translateX(-${currentSlideIndex * 100}%)`;

        // Actualizar los puntos (dots)
        dots.forEach((dot, i) => {
            if (i === currentSlideIndex) {
                dot.classList.add('active');  // Clase para marcar el punto activo
            } else {
                dot.classList.remove('active');
            }
        });

        // Obtener el ID de la habitación de la diapositiva activa
        const habitacionId = slides[currentSlideIndex].dataset.habitacionId;
        
        // Actualizar el campo oculto si habitacionId está disponible
        if (habitacionId) {
            habitacionIdInput.value = habitacionId;
            console.log("Habitación seleccionada ID:", habitacionId);  // Para depuración
        }
    }

    // Mostrar la primera diapositiva al cargar la página
    showSlide(currentSlideIndex);

    // Función para mover a la diapositiva actual al hacer clic en los puntos
    window.currentSlide = function(index) {
        showSlide(index);
    };

    // Función para cambiar la diapositiva automáticamente cada 3 segundos
    const autoChangeSlide = () => {
        showSlide(currentSlideIndex + 1);  // Avanzar a la siguiente diapositiva
    };

    // Cambio automático de diapositivas cada 3 segundos
    setInterval(autoChangeSlide, 2000);  // Cambia cada 3 segundos
});

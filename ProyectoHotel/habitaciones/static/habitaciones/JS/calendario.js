document.addEventListener('DOMContentLoaded', function() {
    // Inicializar Flatpickr
    flatpickr("#calendar-container", {
        inline: true,             // Mostrar el calendario siempre visible
        enableTime: false,        // No habilitar selección de tiempo
        dateFormat: "Y-m-d",      // Formato de la fecha
        mode: "range",            // Seleccionar un rango de fechas
        onChange: function(selectedDates, dateStr, instance) {
            if (selectedDates.length === 2) {
                // Obtener las fechas seleccionadas y actualizar los campos ocultos
                document.getElementById('start-date').value = selectedDates[0].toISOString().split('T')[0];
                document.getElementById('end-date').value = selectedDates[1].toISOString().split('T')[0];
            }
        }
    });

    // Validar el formulario antes de enviarlo
    document.querySelector('form').addEventListener('submit', function(event) {
        // Obtener las fechas seleccionadas
        let startDate = document.getElementById('start-date').value;
        let endDate = document.getElementById('end-date').value;

        if (!startDate || !endDate) {
            event.preventDefault();  // Evitar el envío del formulario si faltan fechas
            alert('Por favor, selecciona las fechas antes de reservar.');
        }
    });
});
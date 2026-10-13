document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("form-contacto");
    if (!form) return;

    form.addEventListener("submit", (e) => {
        const mensaje = document.getElementById("mensaje").value.trim();
        if (mensaje.length < 10) {
            e.preventDefault();
            alert("El mensaje debe tener al menos 10 caracteres.");
        }
    });
});

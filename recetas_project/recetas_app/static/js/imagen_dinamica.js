function triggerFileInput() {
    document.getElementById('id_imagen').click();
}

document.addEventListener('DOMContentLoaded', function() {
    const imagenInput = document.getElementById('id_imagen');
    
    if (imagenInput) {
        imagenInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    document.getElementById('preview').src = e.target.result;
                };
                reader.readAsDataURL(file);
            }
        });
    }
});

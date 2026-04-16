function previewEncode(event) {
    const file = event.target.files[0];
    const preview = document.getElementById('encodePreview');

    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            preview.src = reader.result;
            preview.style.display = "block";
        }
        reader.readAsDataURL(file);
    }
}

function previewDecode(event) {
    const file = event.target.files[0];
    const preview = document.getElementById('decodePreview');

    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            preview.src = reader.result;
            preview.style.display = "block";
        }
        reader.readAsDataURL(file);
    }
}

document.querySelectorAll("input[type='file']"),forEach(input => {
    input.addEventListener("change", function() {
        const filename = this.files[0]?.name || "No file chosen";
        this.parentElement.nextElementSibling.textContent = filename;
    });
});
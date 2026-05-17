function handlePreview(file, previewElement) {
    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            previewElement.src = reader.result;
            previewElement.style.display = "block";
            
            // Add a little pop animation
            previewElement.style.transform = "scale(0.95)";
            setTimeout(() => {
                previewElement.style.transition = "transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)";
                previewElement.style.transform = "scale(1)";
            }, 50);
        }
        reader.readAsDataURL(file);
    } else {
        previewElement.style.display = "none";
        previewElement.src = "";
    }
}

function previewEncode(event) {
    const file = event.target.files[0];
    const preview = document.getElementById('encodePreview');
    handlePreview(file, preview);
}

function previewDecode(event) {
    const file = event.target.files[0];
    const preview = document.getElementById('decodePreview');
    handlePreview(file, preview);
}

function previewDetect(event) {
    const file = event.target.files[0];
    const preview = document.getElementById('detectPreview');
    handlePreview(file, preview);
}

// Ensure the DOM is fully loaded before attaching listeners
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll("input[type='file']").forEach(input => {
        input.addEventListener("change", function() {
            const filename = this.files[0]?.name || "No file chosen";
            // Navigate to the next sibling which is the file-name span in our structure
            const fileNameDisplay = this.closest('.file-upload-wrapper').querySelector('.file-name');
            if (fileNameDisplay) {
                fileNameDisplay.textContent = filename;
            }
        });
    });
});
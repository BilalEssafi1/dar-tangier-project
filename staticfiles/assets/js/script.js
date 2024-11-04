// JavaScript for the gallery modal
document.addEventListener('DOMContentLoaded', function () { 
    const images = [
        "/static/assets/images/restaurant.avif",
        "/static/assets/images/restaurant-image-1.jpg",
        "/static/assets/images/restaurant-image-2.jpg",
        "/static/assets/images/restaurant-image-3.jpg"
    ];

    let currentIndex = 0;

    const galleryImage = document.getElementById('galleryImage');
    const prevButton = document.getElementById('prevButton');
    const nextButton = document.getElementById('nextButton');

    function updateImage() {
        galleryImage.src = images[currentIndex];
    }

    // When the modal opens, set the initial image
    const galleryModal = document.getElementById('galleryModal');
    galleryModal.addEventListener('show.bs.modal', function () { 
        currentIndex = 0;
        updateImage();
    });

    // Event listeners for the navigation buttons
    prevButton.addEventListener('click', function () {
        if (currentIndex > 0) {
            currentIndex--;
            updateImage();
        }
    });

    nextButton.addEventListener('click', function () {
        if (currentIndex < images.length - 1) {
            currentIndex++;
            updateImage();
        }
    });
});

// JavaScript for avoicing empty contact submissions
document.getElementById('contact-form').addEventListener('submit', function(event) {
    const messageField = document.getElementById('message');
    if (messageField.value.trim() === '') {
        alert('Please enter a message before submitting.');
        messageField.focus();
        event.preventDefault();
    }
});

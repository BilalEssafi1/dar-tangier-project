// Function to send the contact form input to dartangier email
function sendEmail(event) {
    event.preventDefault();

    // Get the email and message input values
    const userEmailInput = document.getElementById('exampleInputEmail1');
    const userMessageInput = document.getElementById('message');
    const userEmail = userEmailInput.value;
    const userMessage = userMessageInput.value;

    // Define the email parameters
    const templateParams = {
        from_email: userEmail,
        message: userMessage,
    };

    // Send the email using EmailJS service
    emailjs.send('service_vw98n3z', 'template_pstu1wi', templateParams)
        .then(function(response) {
            console.log('SUCCESS!', response.status, response.text);
            alert('Message sent successfully!');
            
            // Clear the form fields after successful submission
            userEmailInput.value = '';
            userMessageInput.value = '';
        }, function(error) {
            console.log('FAILED...', error);
            alert('There was an error sending your message.');
        });
}

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
    if (form) {
        form.addEventListener('submit', sendEmail);
    }
});
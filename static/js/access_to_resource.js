// Get the form and submit button by their IDs
const form = document.getElementById('access_to_resource');
const submitButton = document.getElementById('submitButton');

// Flag to track whether the form is already submitted
let isFormSubmitted = false;

// Function to handle form submission
function handleSubmit(event) {
  event.preventDefault(); // Prevent the default form submission

  if (isFormSubmitted) {
    alert('Form already submitted. Please wait.');
    return;
  }

  // Perform form submission logic here (e.g., AJAX request)
  // For demonstration, we'll just simulate a delay with a setTimeout
  // Replace this with your actual form submission code
  setTimeout(function () {
    alert('Form submitted successfully!');
    isFormSubmitted = true;
    submitButton.disabled = true; // Disable the submit button
  }, 2000); // Simulated 2-second delay

  // You can also reset the form if needed
  // form.reset();
}

// Add an event listener to the form for submission
form.addEventListener('submit', handleSubmit);

document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registration-form');
  const nameInput = document.getElementById('name');
  const emailInput = document.getElementById('email');
  const contactInput = document.getElementById('contact');
  const submitBtn = document.getElementById('submit');

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      if (!nameInput.value.trim() || !emailInput.value.trim() || !contactInput.value.trim()) {
        alert('Please fill in all required fields (Name, Email, Contact Number).');
        return;
      }

      const originalText = submitBtn.textContent;
      submitBtn.textContent = 'Submitting...';
      submitBtn.disabled = true;

      setTimeout(() => {
        alert(`Welcome, ${nameInput.value.trim()}! Form successfully submitted.`);
        form.reset();
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
      }, 600);
    });
  }
});

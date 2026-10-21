document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registration-form');
  const nameInput = document.getElementById('name');
  const emailInput = document.getElementById('email');
  const contactInput = document.getElementById('contact');
  const statusCard = document.getElementById('status-card');
  const statusDesc = document.getElementById('status-desc');

  const validateEmail = (email) => {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  };

  const validatePhone = (phone) => {
    // Allows optional +, spaces, dashes, parentheses and at least 7 digits
    const digits = phone.replace(/\D/g, '');
    return digits.length >= 7 && digits.length <= 15;
  };

  const setGroupState = (input, isValid) => {
    const formGroup = input.closest('.form-group');
    if (!formGroup) return;
    if (isValid) {
      formGroup.classList.remove('has-error');
    } else {
      formGroup.classList.add('has-error');
    }
  };

  // Real-time validation clearing
  [nameInput, emailInput, contactInput].forEach(input => {
    if (!input) return;
    input.addEventListener('input', () => {
      setGroupState(input, true);
    });
  });

  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      let isValid = true;

      // Name validation
      if (!nameInput.value.trim()) {
        setGroupState(nameInput, false);
        isValid = false;
      } else {
        setGroupState(nameInput, true);
      }

      // Email validation
      if (!validateEmail(emailInput.value.trim())) {
        setGroupState(emailInput, false);
        isValid = false;
      } else {
        setGroupState(emailInput, true);
      }

      // Contact validation
      if (!validatePhone(contactInput.value.trim())) {
        setGroupState(contactInput, false);
        isValid = false;
      } else {
        setGroupState(contactInput, true);
      }

      if (isValid) {
        if (statusCard && statusDesc) {
          statusDesc.textContent = `Thank you, ${nameInput.value.trim()}! Details verified and submitted successfully.`;
          statusCard.classList.remove('hidden');
          statusCard.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
        form.reset();
      }
    });
  }
});

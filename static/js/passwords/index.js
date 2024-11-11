/**
 * Copies the password to the clipboard when
 * the user clicks the copy password button
 */
document.addEventListener('DOMContentLoaded', function () {
  const copyPasswordButtons = document.querySelectorAll(
    '#copy-password-button'
  );

  copyPasswordButtons.forEach((button) => {
    button.addEventListener('click', function () {
      const password = this.getAttribute('data-password');

      navigator.clipboard.writeText(password).then(() => {
        this.textContent = 'Copied';
        this.classList.add('opacity-50', 'cursor-not-allowed');
        this.classList.remove('hover:bg-gray-900/80');
        this.disabled = true;

        setTimeout(() => {
          this.textContent = 'Copy';
          this.classList.remove('opacity-50', 'cursor-not-allowed');
          this.classList.add('hover:bg-gray-900/80');
          this.disabled = false;
        }, 2000);
      });
    });
  });
});

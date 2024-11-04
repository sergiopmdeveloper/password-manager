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
        this.disabled = true;

        setTimeout(() => {
          this.textContent = 'Copy';
          this.classList.remove('opacity-50', 'cursor-not-allowed');
          this.disabled = false;
        }, 2000);
      });
    });
  });
});

/**
 * Removes the delete password modal overlay
 */
function removeDeletePasswordModalOverlay() {
  const overlay = document.querySelector(
    '.bg-gray-900\\/50.dark\\:bg-gray-900\\/80.fixed.inset-0.z-40'
  );

  if (overlay) {
    overlay.remove();
  }
}

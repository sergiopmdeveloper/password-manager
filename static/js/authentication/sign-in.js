/**
 * Handles sign in form submission
 * @param {Event} event - Form submission event
 */
async function handleSignIn(event) {
  event.preventDefault();

  const email = event.target.email.value;
  const password = event.target.password.value;

  signInUser(email, password);
}

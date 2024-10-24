/**
 * Signs in a user with the given email and password
 * @param {string} email - The email of the user
 * @param {string} password - The password of the user
 * @param {string} csrfToken - The CSRF token
 * @returns {Promise<void | Object>} - Nothing or the validation errors
 */
async function signIn(email, password, csrfToken) {
  const requestInit = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify({ email, password }),
  };

  const response = await fetch(URLS.signIn, requestInit);

  if (response.ok) {
    return;
  }

  if (response.status === 400) {
    let errors = await response.json();
    errors['unexpected_error'] = undefined;
    return errors;
  }

  return {
    email_error: undefined,
    password_error: undefined,
    invalid_credentials_error: undefined,
    unexpected_error: UNEXPECTED_ERROR,
  };
}

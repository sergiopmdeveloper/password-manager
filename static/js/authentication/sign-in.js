/**
 * Handles sign in form submission
 * @param {Event} event - Form submission event
 * @returns {void}
 */
async function handleSignIn(event) {
  event.preventDefault();

  const email = event.target.email.value;
  const password = event.target.password.value;
  const csrfToken = event.target.csrf_token.value;
  const button = event.target.querySelector('button');

  const signInErrors = document.getElementById('sign-in-errors');

  button.disabled = true;
  button.classList.remove('hover:bg-gray-900/90');
  button.classList.add('cursor-wait', 'opacity-50');

  const errors = await signIn(email, password, csrfToken);

  if (!errors) {
    window.location.href = '/user';
    return;
  }

  const errorTypes = {
    email: 'email-error',
    password: 'password-error',
    invalid_credentials: 'invalid-credentials-error',
    unexpected_error: 'unexpected-error',
  };

  Object.keys(errorTypes).forEach((errorType) => {
    const errorElement = document.getElementById(errorTypes[errorType]);

    if (errorElement && !errors[errorType]) {
      errorElement.remove();
    }
  });

  if (errors) {
    signInErrors.classList.remove('hidden');

    const emailError = errors['email'];
    const passwordError = errors['password'];
    const invalidCredentialsError = errors['invalid_credentials'];
    const unexpectedError = errors['unexpected_error'];

    if (emailError) {
      let emailErrorElement = document.getElementById(errorTypes['email']);

      if (!emailErrorElement) {
        emailErrorElement = document.createElement('li');
        emailErrorElement.id = errorTypes['email'];
        emailErrorElement.textContent = emailError;
        signInErrors.appendChild(emailErrorElement);
      }
    }

    if (passwordError) {
      let passwordErrorElement = document.getElementById(
        errorTypes['password']
      );

      if (!passwordErrorElement) {
        passwordErrorElement = document.createElement('li');
        passwordErrorElement.id = errorTypes['password'];
        passwordErrorElement.textContent = passwordError;
        signInErrors.appendChild(passwordErrorElement);
      }
    }

    if (invalidCredentialsError) {
      let invalidCredentialsErrorElement = document.getElementById(
        errorTypes['invalid_credentials']
      );

      if (!invalidCredentialsErrorElement) {
        invalidCredentialsErrorElement = document.createElement('li');
        invalidCredentialsErrorElement.id = errorTypes['invalid_credentials'];
        invalidCredentialsErrorElement.textContent = invalidCredentialsError;
        signInErrors.appendChild(invalidCredentialsErrorElement);
      }
    }

    if (unexpectedError) {
      let unexpectedErrorElement = document.getElementById(
        errorTypes['unexpected_error']
      );

      if (!unexpectedErrorElement) {
        unexpectedErrorElement = document.createElement('li');
        unexpectedErrorElement.id = errorTypes['unexpected_error'];
        unexpectedErrorElement.textContent = unexpectedError;
        signInErrors.appendChild(unexpectedErrorElement);
      }
    }
  }

  button.disabled = false;
  button.classList.remove('cursor-wait', 'opacity-50');
  button.classList.add('hover:bg-gray-900/90');
}

function togglePassword(button) {
    let divPai = button.parentElement;
    let passwordInput = divPai.querySelector('input');
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}

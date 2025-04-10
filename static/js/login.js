function checkpassword() {
    let xs = document.getElementsByClassName('pw');
    for (let x of xs) {
        x.type = (x.type === "password") ? "text" : "password";
    }
}
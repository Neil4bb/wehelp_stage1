//不需要在html加onsubmit的寫法
document.getElementById("sign-form").addEventListener("submit", function(event){
    
    event.preventDefault(); //防止送出

    let form = event.target; 

    let username = form.username.value;
    let email = form.email.value;
    let password = form.password.value;

    if (username ===""||email === ""||password === "") {
        alert("不可空白");
        return; //不送出
    }

    form.submit(); //驗證成功 手動送出

});

document.getElementById("login-form").addEventListener("submit", function(event){
    
    event.preventDefault(); //防止送出

    let form = event.target; 

    let email = form.email.value;
    let password = form.password.value;

    if (email === ""||password === "") {
        alert("不可空白");
        return; //不送出
    }

    form.submit(); //驗證成功 手動送出

});


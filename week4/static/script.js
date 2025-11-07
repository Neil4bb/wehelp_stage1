function checkForm() {
    const checkbox = document.getElementById("agree");
    if (!checkbox.checked) {
        alert("請勾選同意條款");
        return false;
    }
    return true;
}

document.getElementById("checkBtn").addEventListener("click", function() {
   //取得使用者輸入的值
    const id = parseInt(document.getElementById("hotelNum").value.trim(), 10);

    if(Number.isInteger(id) && id >0) {
    window.location.href = `/hotel/${id}`;
    //跳轉到hotel網頁
    } else {
        alert("請輸入正整數");
    }
});
//week7 task2

let searchInput = document.getElementById("searchInput");
let searchBtn = document.getElementById("searchBtn");
let searchResult = document.getElementById("searchResult");

searchBtn.addEventListener('click', function(){
    
    //console.log("按鈕成功觸發");

    let id = searchInput.value;
    let url = "/api/member/" + id; 
    
    // 清空舊結果
    //searchResult.textContent = "";
    
    fetch(url)
        .then(response => response.json())
        .then(result => {

            let member = result.data;

            if (member !== null) {
                searchResult.innerHTML = `${member.name}&nbsp;&nbsp;(${member.email})`;
            } else {
                searchResult.textContent = "No Data";
            }


    });

    
});


let newNameInput = document.getElementById("newNameInput");
let newNameBtn = document.getElementById("newNameBtn");
let newNameResult = document.getElementById("newNameResult");

newNameBtn.addEventListener('click', function(){

    let url = "/api/member";
    let newName = newNameInput.value;

    fetch(url, {
        method: "PATCH",
        headers: {
            "Conten-Type": "application/json"
        },
        body: JSON.stringify({ name: newName })

    })
        .then(response => response.json())
        .then(result => {
            
            if (result.ok === true) {
                newNameResult.innerHTML = `更新成功，新的姓名為${newName}`;
            }else {
                newNameResult.innerHTML = "Failed to Update";
            }

        });



});

let querylist = document.getElementById("querylist");
let loadBtn = document.getElementById("loadQueryBtn");

function loadQueries() {

    fetch("/api/queries")
        .then(response => response.json())
        .then(result =>{

            records = result.queries;

            if (!records || records.length === 0) {
                querylist.textContent = "目前無查詢紀錄";
                return;
            }

            querylist.innerHTML = "";

            records.forEach(r => {
                let newdiv = document.createElement("div");
                newdiv.textContent = `${r.name}(${r.time})`;
                querylist.appendChild(newdiv);
            });

        });

}

window.addEventListener("DOMContentLoaded", loadQueries);

loadBtn.addEventListener("click",loadQueries);
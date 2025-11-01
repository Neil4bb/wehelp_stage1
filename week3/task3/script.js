const navMenu = document.querySelector('.nav-menu');
const menuToggle = document.querySelector('.menu-toggle');
const cross = document.querySelector('.cross');


menuToggle.addEventListener('click', () => {
    navMenu.classList.add('active');
});

cross.addEventListener('click', () => {
    navMenu.classList.remove('active');
})

var datatext, datapics;

Promise.all([
fetch("https://cwpeng.github.io/test/assignment-3-1").then(r => r.json()),
fetch("https://cwpeng.github.io/test/assignment-3-2").then(r => r.json())
]).then(([data1, data2]) => {
    const datatext = data1.rows;
    const datapics = data2.rows;

    console.log(datapics);
    console.log(datatext);

const picsBySerial = {};
for (const item of datapics) {
    const firstpic = item.pics.match(/.*?\.jpg/);

    picsBySerial[item.serial] = firstpic[0];
}

const bars = document.querySelectorAll(".bars .bar");

for (let i=0; i<bars.length; i++) {
    const img = bars[i].querySelector("img");
    const p = bars[i].querySelector("p");


    p.textContent = datatext[i].sname;
    const serial = datatext[i].serial;
    const picPath = picsBySerial[serial];
    img.src = "https://www.travel.taipei/" + picPath;
    
}

const content = document.querySelectorAll(".content .block");

for (let i=0; i<content.length; i++) {
    const img = content[i].querySelector("img.main");
    const textbox = content[i].querySelector(".text-box");


    textbox.textContent = datatext[i+bars.length].sname;
    const serial = datatext[i+bars.length].serial;
    const picPath = picsBySerial[serial];
    img.src = "https://www.travel.taipei/" + picPath;
    
}











});
    


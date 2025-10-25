//task 1
console.log("------------task 1------------");

const 貝吉塔 = { cara:"貝吉塔", x: -4, y:- 1, z: 0 }; // 貝吉塔
const 辛巴 = { cara:"辛巴", x: -3, y: 3, z: 0 }; // 辛巴
const 丁滿 = { cara:"丁滿", x: -1, y: 4, z: 1 }; // 丁滿 
const 悟空 = { cara:"悟空", x: 0, y: 0, z: 0 }; // 悟空
const 特南克斯 = { cara:"特南克斯", x: 1, y: -2, z: 0 }; // 特南克斯
const 弗利沙 = { cara:"弗利沙", x: 4, y: -1, z: 1 }; // 弗利沙

const list = [貝吉塔, 辛巴, 丁滿, 悟空, 特南克斯, 弗利沙];

const map = {貝吉塔, 辛巴, 丁滿, 悟空, 特南克斯, 弗利沙};

function func1(name){ 
 // your code here 

    const target = map[name];
    const a = target.x;
    const b = target.y;
    const c = target.z;
    let n = "", f = "";
    let dis, min = Infinity, max = 0;

    for (let i=0; i<6; i++) {
        dis = Math.abs(list[i].x-a) + Math.abs(list[i].y-b);

        if (c != list[i].z) {
            dis +=2;        
        }

        if (dis == 0) {
            continue;
        } else if (dis > max) {
            max = dis;
            f = list[i].cara;
        } else if (dis === max) {
            f +="、"+list[i].cara;
        } 
        
        if (dis < min) {
            min = dis;
            n = list[i].cara;
        } else if (dis === min) {
            n += "、"+list[i].cara;
        }

    }

    console.log("最遠" + f + ";最近" + n);
 } 
 func1("辛巴");  // print 最遠弗利沙；最近丁滿、⾙吉塔
 
 func1("悟空");  // print 最遠丁滿、弗利沙；最近特南克斯
 
 func1("弗利沙");  // print 最遠辛巴，最近特南克斯
 
 func1("特南克斯");  // print 最遠丁滿，最近悟空


// task 2
console.log("------------task 2------------");

// your code here, maybe 
// 初始化時間表
let bookings = {
  S1: [],
  S2: [],
  S3: []
};

// 每當有新預約 檢查是否與既有時段重疊
function isAvailable(service, start, end) {
  for (let b of bookings[service]) {
    if (!(end <= b.start || start >= b.end)) return false;
  }
  return true;
}

  
 function func2(ss, start, end, criteria){ 
 // your code here 
    let splits;
    
    if (criteria.includes("name")) {
        splits = criteria.split("=");
    } else {
        splits = criteria.split(/(>=|<=)/);  
        //正則表達式(RegExp) 的 捕獲群組(capturing group) 
        //捕獲群組會把分隔符保留於array中 
    }

    if (splits[0] == "name") {
        //for迴圈比較service名字
        //符合的情況比較時間
        //時間符合的話 print SX
        let flag = false;

        for (let i=0 ; i<3 ; i++) {
            if (services[i]["name"]==splits[1] && isAvailable(services[i]["name"], start, end) ) {
                bookings[services[i]["name"]].push({ start, end });
                console.log(services[i]["name"]);
                flag = true;
                break;
            } 
        }

        if(!flag) {
            console.log("Sorry");
        }
        
    } else if (splits[0] == "r") {
        //r的情況
        //剔除不符合的
            //無符合>>print sorry
        //取與splits[1]的絕對值最小的
        //查看時間區段
        let ava = null, gap = Infinity;
            if (splits[1] == "<=") {
                for (let i=0 ; i<3 ; i++) {
                    if (services[i]["r"] <= Number(splits[2]) && 
                        Math.abs(services[i]["r"] - Number(splits[2])) < gap ) {
                        if (isAvailable(services[i]["name"], start, end)) {
                            ava = services[i]["name"];  //時間符合才換
                            gap = Math.abs(services[i]["r"] - Number(splits[2]));
                        }
                    }
                }
                
            } else {  //>=的情況
                for (let i=0 ; i<3 ; i++) {
                    if (services[i]["r"] >= Number(splits[2]) && 
                        Math.abs(services[i]["r"] - Number(splits[2])) < gap ) {
                        if (isAvailable(services[i]["name"], start, end)) {
                            ava = services[i]["name"];  //時間符合才換
                            gap = Math.abs(services[i]["r"] - Number(splits[2]));
                        }
                    }
                }
            }
            //print 結果 if 有ava print ava 無 print sorry
            if (ava === null) {
                console.log("Sorry");
            } else {
                bookings[ava].push({ start, end });
                console.log(ava);
            }

    } else {
        //c的情況
        let ava = 0, gap = Infinity;
            if (splits[1] == "<=") {
                for (let i=0 ; i<3 ; i++) {
                    if (services[i]["c"] <= Number(splits[2]) && 
                        Math.abs(services[i]["c"] - Number(splits[2])) < gap ) {
                        if (isAvailable(services[i]["name"], start, end)) {
                            ava = services[i]["name"];  //時間符合才換
                            gap = Math.abs(services[i]["c"] - Number(splits[2]));
                        }
                    }
                }
                
            } else {  //>=的情況
                for (let i=0 ; i<3 ; i++) {
                    if (services[i]["c"] >= Number(splits[2]) && 
                        Math.abs(services[i]["c"] - Number(splits[2])) < gap ) {
                        if (isAvailable(services[i]["name"], start, end)) {
                            ava = services[i]["name"];  //時間符合才換
                            gap = Math.abs(services[i]["c"] - Number(splits[2]));
                        }
                    }
                }
            }
            //print 結果 if 有ava print ava 無 print sorry
            if (ava === null) {
                console.log("Sorry");
            } else {
                bookings[ava].push({ start, end });
                console.log(ava);
            }
    }



 } 
 const services=[ 
 {"name":"S1", "r":4.5, "c":1000}, 
 {"name":"S2", "r":3, "c":1200}, 
 {"name":"S3", "r":3.8, "c":800} 
 ]; 
 func2(services, 15, 17, "c>=800");  // S3 
 func2(services, 11, 13, "r<=4");  // S3 
 func2(services, 10, 12, "name=S3");  // Sorry 
 func2(services, 15, 18, "r>=4.5");  // S1 
 func2(services, 16, 18, "r>=4");  // Sorry 
 func2(services, 13, 17, "name=S1");  // Sorry 
 func2(services, 8, 9, "c<=1500");  // S2
 func2(services, 8, 9, "c<=1500"); // S1 新增條件


//task 3
console.log("------------task 3------------");

function func3(index){ 
// your code here 
//數字四組為一個循環
//頭一個 數字形成的數列是 25, 23, 21.... (-2)i+25
//第二個數字形成的數列是 23, 21, 19.... (-2)j+23
//第三第四個數字形成的數列是 20, 21, 18, 19, 16, 17..... 
//第三個數字形成的數列是 20, 18, 16 (-2)k +20
//第四個數字形成的數列是 21, 19, 17  N3+1

    let rem = index % 4;
    let result = index / 4;
    let quo = Math.floor(result);
    let num = null;

    if (rem == 0) {
        num = (-2)*quo + 25;
    } else if (rem == 1) {
        num = (-2)*quo + 23;
    } else if (rem == 2) {
        num = (-2)*quo + 20;
    } else {
        num = (-2)*quo + 21;
    }

    console.log(num);

} 


func3(1);  // print 23 
func3(5);  // print 21 
func3(10);  // print 16 
func3(30);  // print 6

//task 4
console.log("------------task 4------------");

function func4(sp, stat, n){ 
// your code here 

    let car = null, gap = Infinity;

    for (let i=0 ; i<sp.length; i++) {
        if (!Number(stat[i])) {
            if (Math.abs(sp[i]-n) < gap) {
                gap = Math.abs(sp[i]-n);
                car = i;
            }
        }
    }

    console.log(car);

} 
func4([3, 1, 5, 4, 3, 2], "101000", 2);  // print 5 
func4([1, 0, 5, 1, 3], "10100", 4);  // print 4 
func4([4, 6, 5, 8], "1000", 4);  // print 2
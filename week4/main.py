from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
import urllib.request, json
# task4 調取hotel資料

url_ch = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-ch"
with urllib.request.urlopen(url_ch) as f:
    data_ch = json.load(f)
    hotels_ch = data_ch["list"]

url_en = "https://resources-wehelp-taiwan-b986132eca78c0b5eeb736fc03240c2ff8b7116.gitlab.io/hotels-en"
with urllib.request.urlopen(url_en) as f:
    data_en = json.load(f)
    hotels_en = data_en["list"]

def normalize_ch(item):
    return {
        "_id": item.get("_id"),
        "name_ch": item.get("旅宿名稱","").strip(),
        "phone" : item.get("電話或手機號碼","").strip()
    }

def normalize_en(item):
    return{
        "_id": item.get("_id"),
        "name_en": item.get("hotel name","").strip()
    }

merged = []

en_by_id = {item["_id"]: normalize_en(item) for item in hotels_en}

for ch_item in hotels_ch:
    ch = normalize_ch(ch_item)
    en = en_by_id.get(ch["_id"], {})
    merged.append({**ch, **en})


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(SessionMiddleware, secret_key="secret_key")
#secret_key 為任意字串 用來加密cookie

templates = Jinja2Templates(directory="templates")

#@app.get("/items/{id}", response_class= HTMLResponse)
#async def read_item(request: Request, id: str):
#    return templates.TemplateResponse(
#        request=request, name="item.html", context={"id": id}
#    )
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/login")
async def login(request:Request, email: str = Form(...), password: str = Form(...)):
    if not email or not password:
        request.session["LOGGED_IN"] = False
        return RedirectResponse(url="/error?message=請輸入信箱和密碼", status_code=303)
    if email == "abc@abc.com" and password == "abc":
        request.session["LOGGED_IN"] = True
        return RedirectResponse(url="/member", status_code=303)
    else:
        request.session["LOGGED_IN"] = False
        return RedirectResponse(url="/error?message=信箱或密碼輸入錯誤", status_code=303)

@app.get("/member")
async def member(request: Request):
    if not request.session.get("LOGGED_IN"):
        return RedirectResponse(url="/", status_code=303)
    #如果登入檢驗未過 返回首頁
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/error")
async def error(request: Request, message: str ="發生未知錯誤"):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})

@app.get("/logout")
async def logout(request: Request):
    request.session["LOGGED_IN"] = False 
    # 可使用request.session.clear()完全清除session資料 .get結果為 None
    return RedirectResponse(url="/", status_code=303)

@app.get("/hotel/{id}", response_class= HTMLResponse)
async def hotel_info(request: Request, id: str):
    #id = int(id)
    #index = id - 1
    #if index < 0 or index >= len(merged):
    #    hotel =None
    #else:
    #    hotel = merged[index]

    #id存在判斷
    try:
        hotel = merged[int(id)-1]
    except (ValueError, IndexError):
        hotel = None
    #if int(id)-1 in merged:
    #這邊不能用這種if判斷
    #檢查「list 中是否包含某個值」（不是索引判斷）
    #dict中可檢查 key是否存在

    return templates.TemplateResponse("hotel.html", {
        "request":request,
        "hotel": hotel
    })
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from db import get_connection



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

@app.get("/member")
async def member(request: Request):
    user = request.session.get("USER")

    if not user:
        return RedirectResponse("/", status_code=303)
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
                   SELECT 
                        member.name AS name,
                        message.content AS content,
                        member.id AS m_id,
                        message.id AS msg_id
                   FROM member
                   JOIN message ON message.member_id = member.id
                   ORDER BY message.time DESC;
                   """)
    messages = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return templates.TemplateResponse(
        "member.html",
        {"request": request, "banana": user["name"], "messages":messages, "user_id": user["id"]}
    )
#    if not request.session.get("LOGGED_IN"):
#        return RedirectResponse(url="/", status_code=303)
#    #如果登入檢驗未過 返回首頁
#    return templates.TemplateResponse("member.html", {"request": request})


@app.get("/ohoh")
async def error(request: Request, message: str ="發生未知錯誤"):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})


@app.post("/signup")
async def signup(request: Request,
                 username: str = Form(...),
                 email: str = Form(...),
                 password: str = Form(...)
):
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # 1. 檢查 email 是否存在
        cursor.execute("SELECT * FROM member WHERE email=%s", (email,))
        #cursor.execute 的第二個參數一定要是一組資料（tuple/list），
        #而 tuple 如果只有一個元素，就一定要加逗號。
        result = cursor.fetchone()

        if result:
            # email 重複 → 跳 error page
            url = request.url_for("error").include_query_params(message="重複的電子郵件")
            return RedirectResponse(url=url, status_code=302)

        # 2. 不重複 → 插入資料
        cursor.execute(
            "INSERT INTO member(name, email, password) VALUES(%s, %s, %s)",
            (username, email, password)
        )
        conn.commit()

        # 3. 成功 → 回首頁
        return RedirectResponse("/", status_code=302)
    
    finally:  #python會先跑finally才return
        cursor.close()
        conn.close()


@app.post("/login")
async def login(request:Request, email: str = Form(...), password: str = Form(...)):
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute(
        "SELECT id, name ,email FROM member WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()

    if user:
        request.session["USER"] = {
            "id" : user["id"],
            "name" : user["name"],
            "email" : user["email"]
        }
        return RedirectResponse(url="/member", status_code=303)
    else:
        url = request.url_for("error").include_query_params(message="電子郵件或密碼錯誤")
        return RedirectResponse(url=url, status_code=303)


@app.get("/logout")
async def logout(request: Request):
    #request.session["LOGGED_IN"] = False 
    # 可使用request.session.clear()完全清除session資料 .get結果為 None
    request.session.clear()
    return RedirectResponse(url="/", status_code=303)


@app.post("/createMessage")
async def leaveMessage(request:Request, message: str = Form(...)):
    user = request.session.get("USER")

    if not user:
        return RedirectResponse(url="/", status_code=302)
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    user_id = user["id"]
    content = message

    cursor.execute(
        "INSERT INTO message(member_id, content) VALUES(%s, %s)",
        (user_id, content)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return RedirectResponse(url="/member", status_code=302)

#    
#    if not email or not password:
#        request.session["LOGGED_IN"] = False
#        return RedirectResponse(url="/ohoh?message=請輸入信箱和密碼", status_code=303)
#    if email == "abc@abc.com" and password == "abc":
#        request.session["LOGGED_IN"] = True
#        return RedirectResponse(url="/member", status_code=303)
#    else:
#        request.session["LOGGED_IN"] = False
#        return RedirectResponse(url="/ohoh?message=信箱或密碼輸入錯誤", status_code=303)

@app.post("/deleteMessage")
async def delete(request:Request, message_id: str = Form(...)):
    user = request.session.get("USER")


    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("SELECT member_id FROM message WHERE id=%s",(message_id,))
        writer = cursor.fetchone()

        if not writer: #查找不到 message id 的情況
            url = request.url_for("error").include_query_params(message="此留言不存在")
            return RedirectResponse(url=url, status_code=303)


        if writer["member_id"] == user["id"]:  #使用者id 與留言者比對
            cursor.execute("DELETE FROM message WHERE id=%s",(message_id,))
            conn.commit()
        else:
            url = request.url_for("error").include_query_params(message="非此帳號留言，不允許刪除")
            return RedirectResponse(url=url, status_code=303)

    finally:
        cursor.close()
        conn.close()

    return RedirectResponse(url="/member", status_code=302)


@app.get("/api/member/{member_id}")
def query_member(member_id: int, request: Request):

    user = request.session.get("USER")
    if not user:
        return JSONResponse({"data":None})

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email FROM member WHERE id=%s",(member_id,))
    target_member = cursor.fetchone()

    

    if not target_member:
        cursor.close()
        conn.close()
        return JSONResponse({"data":None})
    
    # 新增查詢紀錄
    if user["id"] != target_member["id"]:
        cursor.execute(
            "INSERT INTO query_record (searcher_id, target_id) VALUES (%s, %s)",
            (user["id"], target_member["id"])
        )
        conn.commit()

    cursor.close()
    conn.close()

    return JSONResponse({"data":target_member})


@app.patch("/api/member")
async def update_member(request: Request):

    # 確認用戶登入
    user = request.session.get("USER")
    if not user:
        return JSONResponse({"error": True})
    
    # 接收JSON資料
    # request.json()，只是request的其中一種用法，用於取body(JSON)
    # request有很多用法，是工具箱並非只是JSON字串
    body = await request.json()
    new_name = body.get("name")
    
    # 避免new_name 是空值
    # 加入.strip() 避免空白字元通過判定
    if not new_name or not new_name.strip():
        return JSONResponse({"error": True})
    
    conn = get_connection()
    cursor = conn.cursor()

    sql = "UPDATE member SET name=%s WHERE id=%s"
    cursor.execute(sql, (new_name, user["id"]))
    conn.commit()

    cursor.close()
    conn.close()

    #更新session
    user["name"] = new_name
    request.session["USER"] = user

    return JSONResponse({"ok": True})


@app.get("/api/queries")
async def view_queries(request: Request):
    
    user = request.session.get("USER")
    if not user:
        return JSONResponse({"queries":None})
    
    current_user_id = user["id"]
    
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    sql ="""
    SELECT m.name, q.time 
    FROM query_record AS q
    JOIN member AS m
    ON q.searcher_id = m.id
    WHERE q.target_id = %s
    ORDER BY q.time DESC
    LIMIT 10;
    """
    cursor.execute(sql, (current_user_id,))
    records= cursor.fetchall()

    cursor.close()
    conn.close()

    for r in records:
        r["time"] = r["time"].strftime("%Y-%m-%d %H:%M:%S")

    return JSONResponse({"queries": records})
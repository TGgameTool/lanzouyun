import requests
import re
import sys
import os
import subprocess
from tkinter import messagebox


def get_lzy_file():
    # 要检测的节点列表
    # 找到最佳节点
    best_node = "kedaya798.lanzoui.com"
    url = f"https://{best_node}/b0w85nacb"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    cookies = {"codelen": "1"}
    response = requests.get(
        url,
        cookies=cookies,
        headers=headers,
        impersonate="chrome",
    )
    if response.status_code != 200:
        response = messagebox.askyesno(
            "更新提示",
            "获取更新失败，请检查网络连接！\n点击 [确认] 重试\n点击 [取消] 关闭更新",
        )
        if response:
            return get_lzy_file()
        else:
            print("Update canceled.")
            return os.path.basename(sys.argv[0]), ""
    response_text = response.text
    match = re.search(r"'fid':(\d+)", response_text)
    if match:
        fid_value = match.group(1)
    match = re.search(r"'uid':'(\d+)'", response_text)
    if match:
        uid_value = match.group(1)
    match = re.search(r"'t':(\w+)", response_text)
    if match:
        t_value = match.group(1)
        print(t_value)  # 输出 iay4nb
    match = re.search(r"'k':(\w+)", response_text)
    if match:
        k_value = match.group(1)
        print(k_value)  # 输出 iay4nb
    t_match = re.search(rf"var {t_value}\s*=\s*'(\d+)'", response_text)
    if t_match:
        t_value = t_match.group(1)
        print(t_value)
    k_match = re.search(rf"var {k_value}\s*=\s*'([a-f0-9]+)'", response_text)
    if k_match:
        k_value = k_match.group(1)
        print(k_value)
    cookies = {
        "codelen": "1",
    }
    headers = {
        "Accept": "application/json, text/javascript, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": f"https://{best_node}",
        "Referer": f"https://{best_node}/b0w85nacb",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }
    params = {
        "file": fid_value,
    }

    data = {
        "lx": "2",
        "fid": fid_value,
        "uid": uid_value,
        "pg": "1",
        "rep": "0",
        "t": t_value,
        "k": k_value,
        "up": "1",
        "ls": "1",
        "pwd": "kedaya",
    }
    print(data)
    response = requests.post(
        f"https://{best_node}/filemoreajax.php",
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    if response.status_code != 200:
        response = messagebox.askyesno(
            "更新提示",
            "获取更新失败，请检查网络连接！\n点击 [确认] 重试\n点击 [取消] 关闭更新",
        )
        if response:
            return get_lzy_file()
        else:
            print("Update canceled.")
            return os.path.basename(sys.argv[0]), ""
    response_json = response.json()
    print(response_json)
    text = response_json["text"]
    最新文件 = text[0]
    url = f"https://{best_node}/{最新文件['id']}"
    print(url)
    return 最新文件["name_all"], url


def lzy_download_url(url, passwd):
    # 提取基础 URL
    match = re.match(r"(https://[^/]+)", url)
    if match:
        base_url = match.group(1)
    else:
        raise ValueError("未找到基础 URL")
    # 设置 cookies 和 headers
    cookies = {
        "codelen": "1",
        "pc_ad1": "1",
    }

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    response = requests.get(
        url=url,
        cookies=cookies,
        headers=headers,
        impersonate="chrome",
    )
    response_text = response.text
    # 正则表达式模式
    pattern = r"<title>(.*?) -"

    # 查找匹配
    match = re.search(pattern, response_text)

    if match:
        title = match.group(1)
        print("Title:", title)
    else:
        print("未找到")
    # 正则表达式模式
    pattern = r'src="/fn\?([^"]+)"'
    # 查找匹配
    match = re.search(pattern, response_text)
    if match:
        result = match.group(1)
        print("result", result)

    response = requests.get(
        url=f"https://kedaya798.lanzoui.com/fn?{result}",
        cookies=cookies,
        headers=headers,
        impersonate="chrome",
    )
    response_text = response.text

    # 正则表达式模式
    pattern = r"'(action|signs|sign|websign|websignkey|kd)':\s*([^,\s}]+)"
    results = {}
    for field in ["action", "signs", "sign", "websign", "websignkey", "kd"]:
        match = re.search(rf"'{field}':\s*([^,\s}}]+)", response_text)
        if match:
            results[field] = match.group(1).strip().strip("'")
    for key in results:
        print(f"{key}:", results[key])
        match = re.search(rf"var\s+{results[key]}\s*=\s*'([^']+)';", response_text)
        if match:
            results[key] = match.group(1)
            print(f"{key}:", results[key])
        else:
            print("未找到")
    if not results:
        raise ValueError("未找到")

    pattern = r"file=(\d+)"
    match = re.search(pattern, response_text)
    if match:
        file_id = match.group(1)
        print(file_id)

    # 设置新的 headers 和 params
    headers = {
        "Accept": "application/json, text/javascript, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": base_url,
        "Referer": url,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    params = {
        "file": file_id,
    }

    data = f'action={results["action"]}&signs={results["signs"]}&sign={results["sign"]}&websign={results["websign"]}&websignkey={results["websignkey"]}&ves=1&kd=1'

    response = requests.post(
        url=f"{base_url}/ajaxm.php",
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )

    response_json = response.json()

    if not os.path.exists(f"./{title}"):
        request_file_data = requests.get(
            url=f'{response_json["dom"]}/file/{response_json["url"]}',
            headers=headers,
            impersonate="chrome",
        )
        file_data = request_file_data.content
        with open(f"./{title}", "wb", encoding="utf-8") as save_file:
            # 保存文件数据
            save_file.write(file_data)
            save_file.close()
        # subprocess.Popen(title, creationflags=subprocess.CREATE_NEW_CONSOLE)
        response = messagebox.askyesno(
            "更新提示", "更新完毕\n即将删除旧版本 即将打开新版本"
        )
        if response:
            create_bat_file(title)
        return
    else:
        response = messagebox.askyesno("更新提示", f"新版本你好像下有了 {title}")
        # subprocess.Popen(title, creationflags=subprocess.CREATE_NEW_CONSOLE)
        if response:
            create_bat_file(title)
        return


def create_bat_file(title):
    # 生成临时 bat 文件的完整路径
    bat_file_path = os.path.join(os.getcwd(), "up.bat")

    # 获取当前运行 exe 文件的完整路径
    exe_file_path = os.path.abspath(sys.argv[0])

    # 创建批处理文件用于删除当前运行的 exe 文件
    bat_content = f"""
@echo off
start "" "{os.path.join(os.getcwd(), title)}"
:loop
ping 127.0.0.1 -n 3 >nul
del "{exe_file_path}"
if exist "{exe_file_path}" (
    goto loop
) else (
    del %0
)
"""

    # 写入 bat 文件
    with open(bat_file_path, "w", encoding="utf-8") as f:
        f.write(bat_content.strip())

    # 使用 subprocess 启动批处理文件
    subprocess.Popen(bat_file_path, creationflags=subprocess.CREATE_NEW_CONSOLE)

    # 确保当前程序退出
    sys.exit()

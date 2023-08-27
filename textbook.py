import requests
import re
import json
import subprocess
import platform
import argparse
# 请自行安装requests re模块，若为Linux,还需安装wget包

# 获取操作系统名称
os = platform.system()
linux = "Linux"
windows = "Windows"

# 使用wget方式获取文件，参数使其只显示进度条
def wget_file(download_url, rename):
    subprocess.run(['wget', '-q', '--show-progress', download_url, '-O', rename])

# 输入智慧教育平台链接并获取contentId
def get_id():
    textbook_link=input("输入网页链接>\n")

    try:
        contentId_rule=re.compile(r"&contentId=([^&]+)")
        contentId=contentId_rule.search(textbook_link)
        contentId=contentId.group(1)
    except AttributeError:
        print("链接有误。")
    else:

        return contentId
contentId=get_id()

# 获取文件名
def get_filename(contentId):
    try:
        response = requests.get(f"https://s-file-1.ykt.cbern.com.cn/zxx/ndrv2/resources/tch_material/details/{contentId}.json")
        file_name = json.loads(response.text)["title"]
        return file_name
    except KeyError:
        pass
file_name=get_filename(contentId)

# 下载pdf文件，默认下载在当前文件夹下
download_url=f"https://r1-ndr.ykt.cbern.com.cn/edu_product/esp/assets_document/{contentId}.pkg/pdf.pdf"
f=requests.get(download_url)

# 如果系统为Linux,使用wget
if os == linux:
    try:
        wget_file(download_url, file_name +".pdf")
    except TypeError:
        print("链接参数有误。")
else:
    with open (f"{file_name}.pdf","wb") as file1:
        file1.write(f.content)
        print(file_name + ".pdf" + " 下载完成。")

import requests
import re
import json
#请自行安装requests re模块

#输入智慧教育平台链接并获取contentId
def get_id():
    textbook_link=input("请输入网页链接:>\n")
    contentId_rule=re.compile(r"&contentId=([^&]+)")
    contentId=contentId_rule.search(textbook_link)
    contentId=contentId.group(1)
    return contentId
contentId=get_id()
while not bool(contentId):
    print("您输入的链接有误，请重新输入")
    get_id()

#获取文件名
def get_filename(contentId):
    response = requests.get(f"https://s-file-1.ykt.cbern.com.cn/zxx/ndrv2/resources/tch_material/details/{contentId}.json")
    file_name = json.loads(response.text)["title"]
    return file_name
file_name=get_filename(contentId)

#下载pdf文件，默认下载在当前文件夹下
download_url=f"https://r1-ndr.ykt.cbern.com.cn/edu_product/esp/assets/{contentId}.pkg/pdf.pdf"
f=requests.get(download_url)
print(download_url)
with open (f"{file_name}.pdf","wb") as file1:
    file1.write(f.content)
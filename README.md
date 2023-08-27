# 课本下载器


## 原理：
通过网页链接获取到contentId，并获取到下载链接进行下载pdf格式可编辑课本  

部分功能代码（获取文件原始名）借鉴于[tchMaterial-parser](https://github.com/happycola233/tchMaterial-parser)大佬
特此鸣谢

## 使用方法
+ 打开[全国中小学智慧教育平台](https://basic.smartedu.cn/tchMaterial?defaultTag=dfb9da8a-2ae2-4b2e-a733-687e0252443f%2F8c9f2e5c-e403-4f55-812c-289021ac66a0%2F9d7edc22-dfc0-4653-95a5-cbe7e4908755%2F0e4e66fc-ae0b-451e-9a91-9b7d86c0752e)
+ 找到自己需要的课本，获得课本链接（会提示登录，但并不需要登录）
  > 例如 义务教育教科书·道德与法治一年级上册 获取到的链接就是
  https://basic.smartedu.cn/tchMaterial/detail?contentType=assets_document&contentId=bdc00134-465d-454b-a541-dcd0cec4d86e&catalogType=tchMaterial&subCatalog=tchMaterial
+ 复制课本链接复制到命令行中
+ 默认下载在当前工作目录下


## TODO
1. 批量下载等功能
2. 可自行更改下载目录功能

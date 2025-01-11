# 基于WIN11TOAST的开机自启提醒工具
图片:
![image](https://user-images.githubusercontent.com/56122690/147819999-d5d5d57d-d55d-477d-876d-d5d9d5d5d5d5.png)
## 没啥用的代码
纯粹是用来提醒自己的和方便听歌和打开浏览器的，不过可以作为参考，增加自动签到什么的脚本或者获取回调结果。
## 安装教程
1.有Pyton环境
2.安装依赖库
```
pip install requests
pip install beautifulsoup4
pip install win11toast
```
3.
将开机自启.bat的{快捷方式}复制到Windows的启动目录(C:\Users\你的Windows账户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup)下
example: C:\Users\你的Windows账户名\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\
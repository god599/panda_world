import json
import requests


if __name__ == '__main__':
	url = "https://v0.yiketianqi.com/api?unescape=1&version=v62&appid=43864799&appsecret=4KsVBglA&cityid=101230101"
 	ret = requests.get(url)
 	if ret.status_code == 200:
  		text = json.loads(ret.text)
  		print(text)

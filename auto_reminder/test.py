import requests

url = "http://zentao.baby-bus.com/index.php?m=company&f=browse&dept=28"

payload={}
headers = {
  'Authorization': 'Basic d3VsaW54dTp3dWxpbnh1MTIzNjU0',
  'Cookie': 'bugModule=0; device=desktop; lang=zh-cn; lastProduct=28; preBranch=0; preProductID=28; qaBugOrder=id_desc; theme=default; zentaosid=24bc333840923b0d9b91f954bb151d69'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
import requests


url = "https://search.lionairthai.com/SL/Flight.aspx/GetFlightSearch"
headers ={
'Host': 'search.lionairthai.com',
'Connection': 'keep-alive',
'Content-Length': '11',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'X-Requested-With': 'XMLHttpRequest',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
'Content-Type': 'application/json; charset=UTF-8',
'Origin': 'https://search.lionairthai.com',
'Sec-Fetch-Site': 'same-origin',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Dest': 'empty',
'Referer': 'https://search.lionairthai.com/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Cookie': '_ga=GA1.2.852679234.1607316485; _gid=GA1.2.1570953683.1607316485; _gcl_au=1.1.2081614385.1607316485; _fbp=fb.1.1607316486036.2138079385; _ts_yjad=1607316486591; __utmc=78513033; __utmz=78513033.1607316488.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __cfduid=da068b7da566e61649c18fe94bf3e01f21607316569; __utma=78513033.852679234.1607316485.1607316488.1607325714.2; __utmt=1; __utmb=78513033.1.10.1607325714; cf_chl_prog=a19; cf_clearance=59f08429a499b8a1b8e8e4c6bc27b15c3669c79e-1607325878-0-250; ASP.NET_SessionId=pwflfdg04emnckceet4hb25d; AWSELB=F3BBC79B045A402DF4C90E4686D51681E3D3302EB8A05241562F0A898AF13D3357F387AEE915059872D23438E7BA519A35E800137F58F02084CEC01902A1A687C9058F6E11; AWSELBCORS=F3BBC79B045A402DF4C90E4686D51681E3D3302EB8A05241562F0A898AF13D3357F387AEE915059872D23438E7BA519A35E800137F58F02084CEC01902A1A687C9058F6E11; _ga=GA1.3.852679234.1607316485; _gid=GA1.3.1570953683.1607316485; ref=refer=https://search.lionairthai.com/; CurrentCustomerInfo=CurrentEncryptCustomer=17Dck4bhvKyYuayH/v/XPEoZmmwLN5gE; CustomerInfo=CustomerUserID=207&Culture=en-GB&isAF=1&CurrentEncryptCustomer=17Dck4bhvKyYuayH/v/XPEoZmmwLN5gE&B2BID=0&UserLoginID=0&QueryString=YWlkPTIwNyZkZXBDaXR5PUNOWCZhcnJDaXR5PURNSyZKdHlwZT0yJmRlcERhdGU9MzElMmYxMiUyZjIwMjAmYXJyRGF0ZT0wMSUyZjAxJTJmMjAyMSZhZHVsdDE9MSZjaGlsZDE9MCZpbmZhbnQxPTAmcHJvbW90aW9uY29kZT0mZGY9VUsmYWZpZD0wJmIyYj0wJlN0PWZhJkRGbGlnaHQ9ZmFsc2Umcm9vbWNvdW50PTEmc2lkPU1RQXhBRElBTGdBMEFEUUFMZ0F5QURBQU9BQXVBRGtBTVFBJTNkJmN1bHR1cmU9ZW4tR0ImdXI9bGlvbmFpcnRoYWkuY29t; __ssds=2; __ssuzjsr2=a9be0cd8e; __uzmaj2=f3ddd31f-c293-4b1a-9721-631b0901ee82; __uzmbj2=1607325935; __uzmcj2=257921085503; __uzmdj2=1607325935; _gat=1; __cf_bm=c83ab431f570e69e4d2a7f81aa0e438fc476da01-1607325941-1800-AcbvMGXLqH5RiGyglZ2UrsQFgDph3HDuVEVmz+hA5n7fvzyO8UYI0PIg6o9Jgqcw/WoYaA85ZNXUIdMoisGEeo01OuZeFLloQZn3JN0sScQ8UZVAG2issGHKyMUDXGcDsGQywHBzyo0kjN3GhEa9W+VU/k1V2chQMFw3ZPlSu+SZ8oFbCbqgSvyUijIOIY5F0Q==',

}

rs = requests.post(url=url,headers=headers,json={'t':'3BF'})
print(rs.text)
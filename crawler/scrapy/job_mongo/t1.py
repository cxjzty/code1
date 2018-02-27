import requests
from bs4 import BeautifulSoup

html='''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div id="d">
        <div id="d1">1</div>
        <div>2</div>
        <div>3</div>
        <div>4</div>
        <div class="c1">5
            <div></div>
        </div>
    </div>
</body>
</html>
'''
soup=BeautifulSoup(html,"html.parser")
# print(soup.find_all("div",))
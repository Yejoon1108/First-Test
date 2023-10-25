#패키지를 설치하는 방법
#검색 pypi 하면 사이트가 뜸 거기서 필요한 패키지를 가져오는거임
#하단에 있는 터미널에 필요한 패키지의 install 명령문을 복사해서넣으면 됨.
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
#터미널에 pip list 하면 깔려있는거 찾아주고
# pip install --upgrade beautifulsoup4
# pip uninstall beautifulsoup

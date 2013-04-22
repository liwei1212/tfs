import urllib2;
from BeautifulSoup import BeautifulSoup

def main():
	userMainUrl="http://paper.people.com.cn";
	while  meta_redirect(userMainUrl):
		userMainUrl = meta_redirect(userMainUrl);
	print userMainUrl
	req = urllib2.Request(userMainUrl);
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	resp.close();
	soup = BeautifulSoup(respHtml);
	foundlink = soup.findAll(attrs={"class":"right_title-pdf"})
	for line in foundlink:
		for row in line.findAll('a'):
			str = row.get('href');
			str = str.replace("../../../","http://paper.people.com.cn/pdfcheck/check/checkPdf.jsp?filename=");
			print str
def download(url):
	req = urllib2.Request(url);
	resp = urllib2.urlopen(req);
def meta_redirect(url):
	req = urllib2.Request(url);
	resp = urllib2.urlopen(req);
	respHtml = resp.read();
	resp.close();
	soup = BeautifulSoup(respHtml);
	result = soup.find("meta",attrs={"http-equiv":"REFRESH"});
	if result:
		wait,text=result["content"].split(";")
		text = text.strip();
		if text.lower().startswith("url="):
			url2=text[4:]
			if (url.find(".htm") == -1):
				url = url + "/" + url2;
			else:
				sStr = url.split("/");
				sStr[len(sStr)-1] = url2;
				url = '/'.join(sStr);
			return url
	return None;
if __name__=="__main__":
	main();

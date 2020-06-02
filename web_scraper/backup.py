import requests
from bs4 import BeautifulSoup
URL = "https://en.wikipedia.org/wiki/Ramayana"
def get_citations(URL):
  response = requests.get(URL)
  # print(dir(response))
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  results = soup.findAll('sup', class_ = "noprint Inline-Template Template-Fact")
  return results

def get_citations_needed_count(URL):
  citations = get_citations(URL)
  return len(citations)

def get_citation_list(URL):
  citations = get_citations(URL)
  for cit in citations:
    print("*******************"*10)
    print(cit.parent.text.strip())


print(get_citations_needed_count(URL))
print(get)

#<sup class="noprint Inline-Template Template-Fact" style="white-space:nowrap;">[<i><a href="/wiki/Wikipedia:Citation_needed" title="Wikipedia:Citation needed"><span title="This claim needs references to reliable sources. (August 2010)">citation needed</span></a></i>]</sup>


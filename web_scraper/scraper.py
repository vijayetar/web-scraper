import requests
from bs4 import BeautifulSoup
# URL = "https://en.wikipedia.org/wiki/Battle_of_the_Bulge"
URL = "https://en.wikipedia.org/wiki/Ramayana"
def get_citations_needed_count(URL):
  response = requests.get(URL)
  # print(dir(response))
  content = response.content
  soup = BeautifulSoup(content, 'html.parser')
  # print(soup.prettify())
  results = soup.find(id="mw-content-text")
  citations = results.p.find_all('sup', class_ = "noprint Inline-Template Template-Fact")
  for cit in citations:
    print("*******************"*10)
    print(cit)
    # print(cit.find_parent('sup', class_ = "noprint Inline-Template Template-Fact"))
    # print(cit.find_parent('sup'))
  # for citation in citations.find_parents('sup'):
  #   print citation.name
  # print(citations)
  # print(len(citations))
  # for citation in citations:
    # print(citation.text)

def get_citation_list(URL):
  pass

get_citations_needed_count(URL)

#<sup class="noprint Inline-Template Template-Fact" style="white-space:nowrap;">[<i><a href="/wiki/Wikipedia:Citation_needed" title="Wikipedia:Citation needed"><span title="This claim needs references to reliable sources. (August 2010)">citation needed</span></a></i>]</sup>


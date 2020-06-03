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
  cit_list = []
  for cit in citations:
    cit = cit.parent.text.strip()
    cit_list.append(cit)
  return cit_list

if __name__ == "__main__":
  
  print(get_citations_needed_count(URL))
  for i in get_citation_list(URL):
    print("**************************"*10)
    print(i)
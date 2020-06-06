import requests
from bs4 import BeautifulSoup
URL = "https://en.wikipedia.org/wiki/Ramayana"
def get_citations(URL):
  response = requests.get(URL)
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
  return_string = ""
  for p in cit_list:
    return_string += p + "\n" +"\n"
  print(return_string)
  return return_string

def get_citation_headings(URL):
    headings = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    anchors = soup.find_all("a")
    heading_tags = ['h1','h2','h3','h4','h5','h6']
    for anchor in anchors:
        text = anchor.get_text()
        if "citation needed" in text:
            elem = anchor.parent.parent.parent
            for ps in elem.previous_siblings:
                if ps.name in heading_tags:
                    headings.append(ps.text)
                    break
    return_string = ""
    for p in headings:
      return_string += p + "\n" +"\n"
    print(return_string)
    return return_string

if __name__ == "__main__":
  
  print(get_citations_needed_count(URL))
  get_citation_headings(URL)
  get_citation_list(URL)
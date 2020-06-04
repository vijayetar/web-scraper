import pytest
from web_scraper.scraper import get_citation_list, get_citations, get_citations_needed_count

def test_import():
  assert get_citations

def test_none_citations_needed():
  URL = "https://en.m.wikipedia.org/wiki/The_Lord_of_the_Rings"
  actual = get_citations_needed_count(URL)
  expected = 0
  assert actual == expected

def test_nine_citations_needed():
  URL = "https://en.wikipedia.org/wiki/Battle_of_the_Bulge"
  actual = get_citations_needed_count(URL)
  expected = 9
  assert actual == expected

def test_one_report():
  URL = "https://en.wikipedia.org/wiki/Battle_of_the_Bulge"
  actual = get_citation_list(URL)[0]
  expected = "The Wehrmacht's code name for the offensive was Unternehmen Wacht am Rhein (\"Operation Watch on the Rhine\"), after the German patriotic hymn Die Wacht am Rhein, a name that deceptively implied the Germans would be adopting a defensive posture along the Western Front. The Germans also referred to it as \"Ardennenoffensive\" (Ardennes Offensive) and Rundstedt-Offensive, both names being generally used nowadays in modern Germany.[citation needed] The French (and Belgian) name for the operation is Bataille des Ardennes (Battle of the Ardennes). The battle was militarily defined by the Allies as the Ardennes Counteroffensive, which included the German drive and the American effort to contain and later defeat it. The phrase Battle of the Bulge was coined by contemporary press to describe the way the Allied front line bulged inward on wartime news maps.[38][39]"
  assert actual == expected

def test_two_report():
  URL = "https://en.wikipedia.org/wiki/Ramayana"
  actual = get_citation_list(URL)[0]
  expected = "There has been discussion as to whether the first and the last volumes (Bala Kand and Uttara Kand) of Valmiki's Ramayana were composed by the original author. Most Hindus still believe they are integral parts of the book, in spite of some style differences and narrative contradictions between these two volumes and the rest of the book.[citation needed]"
  assert actual == expected
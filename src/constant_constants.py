"""
Module for holding constants used all over the program.
"""

# User agent 
USER_AGENT = 'iTunes/10.5.3'

# URLs
HOME_URL = "http://itunes.apple.com/WebObjects/MZStore.woa/wa/viewGrouping?id=27753"

SEARCH_U = "http://ax.search.itunes.apple.com/WebObjects/MZSearch.woa/wa/search?submit=media&restrict=true&term=%s&media=cobalt"
SEARCH_P = "http://ax.search.itunes.apple.com/WebObjects/MZSearch.woa/wa/search?submit=media&term=%s&media=podcast"
SEARCH_URL1 = "http://phobos.apple.com/WebObjects/MZSearch.woa/wa/advancedSearch?media=iTunesU&searchButton=submit&allTitle=%s&descriptionTerm=%s&institutionTerm=%s"
SEARCH_URL2 = "http://ax.search.itunes.apple.com/WebObjects/MZSearch.woa/wa/advancedSearch?media=podcast&titleTerm=%s&authorTerm=%s&descriptionTerm=%s&genreIndex=&languageTerm="

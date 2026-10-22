# To install: pip install tavily-python
from tavily import TavilyClient
client = TavilyClient("tvly-dev-*************************************************")
response = client.search(
    query="vendor security advisory, security hardening release, PSIRT advisory, security bulletin, emergency update, out-of-band update, maintenance release, product security announcement, Fortinet, Palo Alto, Cisco, Citrix, Ivanti, PHP, Apache",
    include_answer="basic",
    search_depth="advanced",
    max_results=20,
    start_date="2026-10-20",
    end_date="2026-10-22",
    include_published_date=True,
    filter_by_published_date=True
)
print(response)
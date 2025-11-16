import pytest
from extract_load.load_jobs import _get_ads

def test_jobtech_api():
    """Integrationstest som verifierar att Jobtech API svarar korrekt."""
    
    url = "https://jobsearch.api.jobtechdev.se/search"

    params = {
        "q": "",
        "limit": 5
    }

    data = _get_ads(url, params)

    assert isinstance(data, dict)
    assert "hits" in data
    assert isinstance(data["hits"], list)

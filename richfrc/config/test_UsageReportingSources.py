from .UsageReportingSources import usage_reporting_sources
from .ValidYears import valid_frc_years
import requests

def test_valid_data():
    for source in usage_reporting_sources:
        
        # Ensure source is a valid year
        assert source in valid_frc_years
        
        # Ensure the source exists
        assert requests.get(usage_reporting_sources[source]).status_code is not 404
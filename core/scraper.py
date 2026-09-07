import urllib.request
import xml.etree.ElementTree as ET
from core.classifier import classify_lead

FEEDS = [
    {
        "name": "مشاريع مستقل - تسويق ومبيعات",
        "url": "https://mostaql.com/feed/projects/marketing-sales"
    },
    {
        "name": "مشاريع مستقل - تصميم ومونتاج وفيديو",
        "url": "https://mostaql.com/feed/projects/design"
    }
]

def fetch_rss_leads(feed_info):
    leads = []
    try:
        req = urllib.request.Request(
            feed_info["url"], 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=12) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            
            for item in root.findall('.//item'):
                title = item.find('title').text if item.find('title') is not None else ""
                description = item.find('description').text if item.find('description') is not None else ""
                link = item.find('link').text if item.find('link') is not None else "#"
                
                full_text = f"{title}\n{description}"
                lead = classify_lead(full_text, source=feed_info["name"], url=link)
                leads.append(lead)
    except Exception as e:
        print(f"Error fetching from {feed_info['name']}: {e}")
    return leads

def run_scraper():
    all_leads = []
    for feed in FEEDS:
        all_leads.extend(fetch_rss_leads(feed))
    return all_leads
    

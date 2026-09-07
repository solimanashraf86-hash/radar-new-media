from core.classifier import classify_lead

def run_scraper():
    raw_posts = [
        {"text": "مطلوب شركة إنتاج لتصوير فيديو إعلاني تجاري لمنتجاتنا الأسبوع القادم", "source": "رسائل السوق", "url": "#"},
        {"text": "محتاجين نعرف باقات الميديا الشهرية وإدارة الحملات الرقمية", "source": "شبكات التواصل", "url": "#"},
        {"text": "براند ملابس جديد يفتتح فرعاً ويبحث عن أفكار تسويقية مميزة", "source": "استكشاف محلي", "url": "#"}
    ]
    
    processed_leads = []
    for item in raw_posts:
        lead = classify_lead(item["text"], source=item["source"], url=item["url"])
        processed_leads.append(lead)
        
    return processed_leads
  

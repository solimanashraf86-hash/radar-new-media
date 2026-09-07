import hashlib
from datetime import datetime

HOT_KEYWORDS = ["فيديو تجاري", "تصوير إعلان", "حملة إعلانية", "سعر إعلان", "إنتاج فيديو", "عايز فيديو", "مطلوب تصوير"]
STRONG_KEYWORDS = ["باقات", "إدارة حملات", "تسويق إلكتروني", "سوشيال ميديا", "عرض أسعار", "خدمات تسويق"]

def calculate_freshness(timestamp_str=None):
    return "منذ لحظات"

def classify_lead(text, source="عام", url=""):
    text_lower = text.lower()
    
    intent_score = 0
    category = "WATCH"
    reason = "متابعة نشاط عام واستكشاف فرص"

    for kw in HOT_KEYWORDS:
        if kw in text_lower:
            intent_score = 90
            category = "HOT"
            reason = f"نية شراء مباشرة وعاجلة ({kw})"
            break

    if category != "HOT":
        for kw in STRONG_KEYWORDS:
            if kw in text_lower:
                intent_score = 65
                category = "STRONG"
                reason = f"اهتمام واضح واستفسار خدمات ({kw})"
                break

    if category == "WATCH":
        intent_score = 30

    lead_id = hashlib.md5((text + source).encode('utf-8')).hexdigest()

    return {
        "id": lead_id,
        "title": text[:60] + "..." if len(text) > 60 else text,
        "snippet": text,
        "category": category,
        "intent_score": intent_score,
        "reason": reason,
        "freshness_text": calculate_freshness(),
        "source": source,
        "url": url,
        "status": "جديد"
    }
    

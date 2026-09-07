"""نظام رصد الفرص وتحليل نية الشراء - رادار NEW MEDIA"""

from datetime import datetime, timedelta

PIPELINE_STAGES = [
    "جديد",
    "تم التواصل",
    "رد",
    "مهتم",
    "تفاوض",
    "تم البيع",
    "خسرنا العميل",
    "تجاهل",
]

HOT_KEYWORDS = [
    "سعر",
    "بكام",
    "محتاج اعلان",
    "عايز فيديو",
    "انتاج",
    "فوري",
    "تكلفة",
    "حجز",
    "تصوير",
]
STRONG_KEYWORDS = [
    "تفاصيل",
    "خدماتكم",
    "سابقة اعمال",
    "عايز استفسر",
    "باقة",
    "عرض اسعار",
]


class LeadRadar:

  def __init__(self):
    self.seen_leads = set()

  def is_recent(self, post_date_str: str) -> bool:
    try:
      post_date = datetime.fromisoformat(post_date_str)
      return datetime.now() - post_date <= timedelta(hours=48)
    except Exception:
      return True

  def clean_and_deduplicate(self, lead_id: str) -> bool:
    if lead_id in self.seen_leads:
      return False
    self.seen_leads.add(lead_id)
    return True

  def analyze_intent(self, text: str, post_date: str) -> dict:
    is_fresh = self.is_recent(post_date)

    if any(word in text for word in HOT_KEYWORDS) and is_fresh:
      classification = "🔥 HOT"
    elif any(word in text for word in STRONG_KEYWORDS):
      classification = "🟠 STRONG"
    else:
      classification = "👀 WATCH"

    return {
        "classification": classification,
        "status": "جديد",
        "is_fresh": is_fresh,
        "processed_at": datetime.now().isoformat(),
    }
    

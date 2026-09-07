"""
نظام رادار NEW MEDIA المتكامل
يقوم بجمع الفرص، تحليل نية الشراء، وفرزها في خط المتابعة
"""
import json
from core.scraper import fetch_public_leads
from core.classifier import LeadRadar

def run_radar():
    radar = LeadRadar()
    leads = fetch_public_leads()
    processed_pipeline = []

    print("🚀 بدء تشغيل رادار NEW MEDIA...")
    for item in leads:
        lead_id = item.get("id")
        text = item.get("text", "")
        post_date = item.get("date")

        # 1. منع التكرار
        if not radar.clean_and_deduplicate(lead_id):
            continue

        # 2. تحليل نية الشراء والحداثة
        analysis = radar.analyze_intent(text, post_date)
        
        entry = {
            "id": lead_id,
            "text": text,
            "source": item.get("source"),
            "category": analysis["classification"],
            "status": analysis["status"],
            "processed_at": analysis["processed_at"]
        }
        processed_pipeline.append(entry)
        print(f"[{entry['category']}] فرصة: {entry['text']} | الحالة: {entry['status']}")

    # حفظ النتائج في ملف بيانات محدث للوحة التحكم
    with open("dashboard/leads_data.json", "w", encoding="utf-8") as f:
        json.dump(processed_pipeline, f, ensure_ascii=False, indent=2)

    print(f"✅ تم معالجة وتصنيف {len(processed_pipeline)} فرصة بنجاح.")

if __name__ == "__main__":
    run_radar()
  

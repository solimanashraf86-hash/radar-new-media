import json
import os
from core.database import init_db, save_leads, get_all_leads
from core.scraper import run_scraper

def export_dashboard_data(leads):
    os.makedirs("dashboard", exist_ok=True)
    out_path = os.path.join("dashboard", "data.json")
    
    existing_status = {}
    if os.path.exists(out_path):
        try:
            with open(out_path, "r", encoding="utf-8") as f:
                old_data = json.load(f)
                for item in old_data:
                    existing_status[item.get("id")] = item.get("status")
        except Exception:
            pass

    for lead in leads:
        if lead["id"] in existing_status:
            lead["status"] = existing_status[lead["id"]]

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(leads, f, ensure_ascii=False, indent=2)
    print(f"تم تحديث بيانات اللوحة: {len(leads)} فرصة مرصودة.")

def main():
    init_db()
    scraped_leads = run_scraper()
    save_leads(scraped_leads)
    all_leads = get_all_leads()
    export_dashboard_data(all_leads)

if __name__ == "__main__":
    main()
    

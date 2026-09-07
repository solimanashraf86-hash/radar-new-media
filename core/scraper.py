"""نظام جمع ومسح المصادر العامة - رادار NEW MEDIA"""

import json
from datetime import datetime


def fetch_public_leads():
  """محاكاة جلب واستخراج الفرص العامة من خلاصات الويب وشبكات التواصل"""
  sample_leads = [
      {
          "id": "lead_101",
          "text": "محتاج شركة ميديا تعملي إعلان فيديو احترافي فوري للمحل",
          "source": "منشور عام",
          "date": datetime.now().isoformat(),
      },
      {
          "id": "lead_102",
          "text": "ممكن تفاصيل باقات إنتاج الفيديو والموشن جرافيك لديكم؟",
          "source": "استفسار وارد",
          "date": datetime.now().isoformat(),
      },
  ]
  return sample_leads


if __name__ == "__main__":
  leads = fetch_public_leads()
  print(f"تم رصد {len(leads)} فرصة جديدة بنجاح.")
  

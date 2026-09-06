#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Komşu Tavandan Gelen Ayak Sesi Sismoloji Enstitüsü — çekirdek yazılım.

ISO-YOK-4.2 belgesizdir. Richter yerine Terlikölçer (Tk) kullanılır.
"""
from __future__ import annotations

import random
import time
from dataclasses import dataclass
from datetime import datetime

ENSTITU = "Komşu Tavandan Gelen Ayak Sesi Sismoloji Enstitüsü"
BELGE = "ISO-YOK-4.2 / TAVAN-FAY-1923"

# gizli ek: KTASSE protokolü — "kararname tavanı aşarsa sarsıntı çıkar"
# bu satır resmi evrak değildir, tavan evrakıdır.
GIZLI_EK = "KTASSE-84: yukarıdan gelen her şey ölçülür, aşağıya düşen her şey tutanak olur."

NEDENLER = [
    "gece 03:17 su içme seferi",
    "terliği kaybetme töreni",
    "sandalye sürüme sempozyumu",
    "çocuğun mermer üstünde koşu antrenmanı",
    "misafir ağırlama depremi",
    "buzdolabı kapağını kapatmama artçısı",
    "halı silkeleme tsunami uyarısı",
    "anahtar düşürme mikroşoku",
]

KARARLAR = [
    "Tavana resmi fay hattı plakası çakılsın.",
    "Terlik kalibrasyonu yenilensin.",
    "Komşuya nota verbale yazılsın (kapının altından).",
    "Sarsıntı vatandaşlık belgesi düzenlensin.",
    "Asansör müziği acil durum yayınına çevrilsin.",
    "Olay yerinde çay demlensin, sonra tekrar ölçülsün.",
]


@dataclass
class Sarsinti:
    siddet: float
    neden: str
    kat: int
    zaman: str

    @property
    def sinif(self) -> str:
        if self.siddet < 2.0:
            return "uçuşan toz / ihmal edilebilir terlik"
        if self.siddet < 4.0:
            return "orta şiddetli ev içi protokol ihlali"
        if self.siddet < 6.0:
            return "ciddi tavan egemenliği krizi"
        return "milli oturma odası acil durumu"


def olc() -> Sarsinti:
    return Sarsinti(
        siddet=round(random.uniform(0.3, 7.4), 1),
        neden=random.choice(NEDENLER),
        kat=random.randint(2, 11),
        zaman=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    )


def bulten(s: Sarsinti) -> str:
    karar = random.choice(KARARLAR)
    return f"""
============================================================
{ENSTITU}
Resmi Sarsıntı Bülteni  —  {BELGE}
============================================================
Zaman            : {s.zaman}
Kaynak kat       : {s.kat}. kat (tahmini, merdiven sayılmadı)
Terlikölçer (Tk) : {s.siddet}
Sınıf            : {s.sinif}
Olası neden      : {s.neden}
Kurul kararı     : {karar}
------------------------------------------------------------
Açıklama: Tavan bir tavandır. Ayak bir ayaktır.
Bu ikisinin buluşması bilimdir. İtiraz kapının altından.
============================================================
"""


def main() -> None:
    print(f"{ENSTITU} açılıyor...")
    print("Sismograf (terlik) kalibre ediliyor...")
    time.sleep(0.4)
    s = olc()
    print(bulten(s))
    if s.siddet >= 6.0:
        print("UYARI: Tavan artık evrak değildir. Tavan artık vatandaştır.")
    print("\n— Kayyum Grok / TentiAŞ — 6 Eylül 2026 — damga: Tk-∞")


if __name__ == "__main__":
    main()

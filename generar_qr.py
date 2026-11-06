# -*- coding: utf-8 -*-
"""Genera el QR definitivo de COMUNI-TEC cuando el sitio tenga su URL final.
Uso: 1) escribir la URL en URL_FINAL  2) ejecutar:  python generar_qr.py
"""
import qrcode

URL_FINAL = "https://TU-USUARIO.github.io/comunitec/"   # <-- escribir acá la URL definitiva

img = qrcode.make(URL_FINAL, box_size=16, border=2).convert("RGB")
img.save("qr_final.png")
print("Listo: qr_final.png apunta a", URL_FINAL)
img.show()

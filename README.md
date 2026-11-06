# COMUNI-TEC — Sitio web del proyecto

Sitio estático (un solo archivo `index.html`, sin dependencias externas) para presentar la app **COMUNI-TEC** en la Muestra Anual de Enseñanza Técnica.

- **Creadoras:** dos alumnas de 7.º año — Escuela Técnica Nº 1, Monteros, Tucumán.
- **Proyecto:** sin fines de lucro, gratuito.

## Contenido del paquete

| Archivo | Para qué sirve |
|---|---|
| `index.html` | El sitio completo (imágenes y QR ya incrustados). |
| `COMUNI-TEC.apk` | La app. Súbelo junto al sitio para que el botón de descarga funcione en tu hosting. |
| `qr_comunitec.png` | El código QR actual (apunta al enlace provisional del APK). |
| `generar_qr.py` | Script para regenerar el QR con la URL definitiva del sitio. |

## Estado actual

- Galería completa: ícono, escudo escolar y **4 capturas de la app** (inicio, Pictogramas por categorías, Pictogramas con frases y Escribir y hablar), todas incrustadas en el `index.html`.
- Enlace de descarga: el botón apunta a `COMUNI-TEC.apk` — mantener el APK **en la misma carpeta que `index.html`**.
- El QR se genera solo cuando el sitio está publicado (ver más abajo).

## Cómo actualizar el sitio ya publicado

**GitHub** (alojamiento actual): subir el nuevo `index.html` reemplazando el anterior (*Add file → Upload files → Commit changes*).
**Netlify**: si está conectado al repositorio de GitHub, se redespliega **automáticamente** tras el commit; si se creó con Netlify Drop, arrastrar de nuevo la carpeta en `app.netlify.com/drop`.

## El QR se genera solo

Cuando el sitio esté publicado en internet (http/https), la página dibuja automáticamente un QR que apunta a **su propia dirección** — no hay que regenerar nada a mano. Usa la librería `qrcode-generator` (jsDelivr); si no hay internet en la muestra, muestra el QR de respaldo `qr_comunitec.png`.

Si igualmente querés un QR estático con la URL definitiva, escribila en `generar_qr.py` y ejecutalo:

```bash
pip install qrcode pillow
python generar_qr.py
```

## Cómo publicarlo gratis

**Opción A — GitHub Pages**
1. Crear cuenta en github.com y un repositorio público (ej.: `comunitec`).
2. Subir `index.html` y `COMUNI-TEC.apk`.
3. En *Settings → Pages → Source* elegir la rama `main`, carpeta `/root`. Guardar.
4. En 1–2 minutos el sitio queda en `https://tuusuario.github.io/comunitec/`.

**Opción B — Netlify Drop (la más rápida)**
1. Entrar a `app.netlify.com/drop`.
2. Arrastrar una carpeta con `index.html` y `COMUNI-TEC.apk`.
3. Netlify da al instante una URL tipo `https://comunitec.netlify.app/` (se puede cambiar el nombre).

## Cómo regenerar el QR con la URL final

Cuando el sitio tenga su dirección definitiva:

```bash
pip install qrcode pillow
python generar_qr.py
```

1. Abrir `generar_qr.py` y escribir la URL final en la variable `URL_FINAL`.
2. Ejecutarlo: genera `qr_final.png` y lo muestra por pantalla.
3. Abrir `index.html`, buscar el comentario `<!-- QR -->` y reemplazar el `src` por `qr_final.png` (subiendo la imagen junto al sitio).

Alternativa sin código: un generador confiable es `https://www.qr-code-generator.com/` o LibreOffice Draw → Insertar → Código QR (pegar la URL del sitio).

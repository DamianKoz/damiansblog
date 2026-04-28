# damiansblog.com

Personal blog by **Damian Kozakiewicz** — built with [Hugo](https://gohugo.io/), custom theme `bootstrap` (locally in `/themes/bootstrap/`).

---

## Stack

- **Hugo** v0.152+
- **Theme:** `themes/bootstrap/` (custom, not a Hugo module)
- **Hosting:** deploy the `public/` folder (built via `hugo --cleanDestinationDir`)
- **Analytics:** Google Analytics `G-ECDF3ESVLR` (configured in `config.toml`)
- **Newsletter:** Substack embed in every post (`themes/bootstrap/layouts/posts/single.html`)

---

## Key files

| File | Purpose |
|---|---|
| `config.toml` | Site title, base URL, analytics, params (twitter handle etc.) |
| `themes/bootstrap/layouts/partials/header.html` | `<head>` with all meta tags, OG tags, canonical, Twitter card |
| `themes/bootstrap/layouts/partials/footer.html` | Footer + closes `</body></html>` |
| `themes/bootstrap/layouts/index.html` | Homepage template (includes JSON-LD Person schema) |
| `themes/bootstrap/layouts/posts/single.html` | Single post template |
| `themes/bootstrap/layouts/_default/baseof.html` | Base layout: header → main block → footer |
| `themes/bootstrap/config.toml` | Theme params (description, author, social links, menu) |
| `static/robots.txt` | Crawler rules + sitemap reference |
| `content/posts/` | All blog posts as Markdown |

---

## Writing a new post

```bash
hugo new content/posts/my-post-title.md
```

Frontmatter template (from `themes/bootstrap/archetypes/posts.md`):
```yaml
---
title: "My Post Title"
date: 2024-01-01T00:00:00+01:00
draft: false
categories: ["category-name"]
summary: "One sentence shown in Google search results as meta description."
slug: "my-post-title"
---
```

> **`summary` ist wichtig** — wird direkt als `<meta name="description">` und `og:description` genutzt. Immer ausfüllen.

---

## Build & deploy

```bash
# Lokaler Dev-Server
hugo server

# Production build
hugo --cleanDestinationDir

# Danach: public/ deployen
```

`public/` ist in `.gitignore` — nicht committen, nur deployen.

---

## SEO — Stand April 2026

### Was konfiguriert ist

- **Meta description:** dynamisch aus `summary` im Frontmatter jedes Posts
- **Open Graph:** `og:title`, `og:description`, `og:type`, `og:url`, `og:site_name` in `header.html`
- **Twitter Card:** `summary`-Card mit Handle `@damiankozakiew1`
- **Canonical URL:** pro Seite korrekt gesetzt
- **robots.txt:** `static/robots.txt` — erlaubt alles, verweist auf Sitemap
- **JSON-LD Person-Schema:** auf der Homepage (`index.html`) — wichtig für Suche nach "Damian Kozakiewicz"
- **Sitemap:** wird automatisch von Hugo generiert → `public/sitemap.xml`

### Sitemap bei Google einreichen

1. Öffne [Google Search Console](https://search.google.com/search-console) → Property `damiansblog.com`
2. Linke Navigation → **Sitemaps**
3. Unter "Neue Sitemap hinzufügen" eingeben: `sitemap.xml`
4. **Senden** klicken

> Nach jedem größeren Batch neuer Posts → Search Console öffnen und "Sitemap erneut abrufen" anklicken, damit Google schneller indexiert.

### Was noch fehlen könnte (nächste Schritte)

- **About-Seite auf eigener Domain hosten** — aktuell zeigt der Nav-Link auf `damiansblog.notion.site` (externe Domain), was bedeutet, dass Google Informationen über dich nicht `damiansblog.com` zuordnet
- **`og:image`** — noch kein Bild in den OG-Tags. Ein festes Fallback-Bild in `header.html` eintragen würde Social Shares verbessern
- **Mehr Posts** — wichtigster SEO-Faktor überhaupt; aktuell ~8 Posts

---

## Bekannte technische Details

- `themes/bootstrap/config.toml` enthält Menü, Social-Links und Theme-Params — nicht `config.toml` im Root
- Der `[Social]`-Block in der Theme-Config ist deprecated (Hugo ≥ 0.124), daher wird der Twitter-Handle über `params.twitterHandle` in der Root-`config.toml` gesetzt
- `markup.goldmark.renderer.unsafe = true` muss in der Root-`config.toml` stehen (nicht nur im Theme), damit HTML in Markdown-Posts gerendert wird

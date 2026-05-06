# 🎨 Icon System — Semantic Library v2.0

Унифицированная библиотека иконок с семантическим именованием.  
**411 иконок** (включая 221 кросс-продуктовую иконку Tree), готовые к интеграции.

## 📁 Структура

```
assets/
├── Tree_merged/ (221) — Кросс-продуктовые иконки (waf, dcfw, gateway, log-browser...)
├── actions/     (26)  — add, delete, save, filter, export...
├── brands/      (10)  — cisco, windows, linux, react...
├── editor/      (23)  — bold, italic, chart-bar, align-left...
├── files/       (9)   — file-pdf, file-csv, certificate...
├── navigation/  (19)  — arrow-left, chevron-right, expand...
├── network/     (24)  — interface-*, nat-*, server, link...
├── security/    (12)  — lock-*, shield-*, key, block...
├── status/      (22)  — success, error, warning, priority-*...
└── ui/          (45)  — settings, menu, user, bell, eye...
```

## 📐 Правила именования

| Правило | Пример |
|---------|--------|
| **kebab-case** | `arrow-right.svg` |
| **Объект → Действие** | `filter-add.svg` (не `add-filter`) |
| **Кросс-продуктовый нейминг** | `gateway.svg` (не `network-gateway`) |
| **Имена продуктов как есть** | `dcfw.svg`, `waf-rule.svg` |
| **Сингуляризация** | `idps-profile.svg` (не `idps-profiles`) |
| **Суффиксы вариантов** | `-filled`, `-outlined`, `-disabled`, `-alt` |

Подробнее → [semantic_naming_rules.md](./semantic_naming_rules.md)

## 🖼 Галерея

Откройте `index.html` для интерактивного просмотра:
- Режимы **UI Library** и **Tree Nav** (для 221 новых иконок)
- Сравнение **As Is → To Be** (с синхронным ховером для пар)
- Умная сортировка и группировка
- Click-to-copy имена иконок
- Статусы: ✅ merged, 🔴 duplicate, 🟡 discuss

**Live**: [iconrefactoring.vercel.app](https://iconrefactoring.vercel.app)

## 🔧 Для разработчиков

### Импорт иконки
```html
<img src="./assets/actions/add.svg" alt="Add" />
```

### Маппинг старых → новых имён
См. [icon_audit.csv](./icon_audit.csv) — полный CSV с маппингом оригинальных и новых имён.

---

*Сгенерировано Icon Audit System • 2026*

# 🎨 Icon System — Semantic Library v1.0

Унифицированная библиотека иконок с семантическим именованием.  
**190 иконок** в **9 категориях**, готовые к интеграции.

## 📁 Структура

```
assets/
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
| **Плоское имя** (без категории) | `cisco.svg` (не `brands-cisco`) |
| **Суффиксы вариантов** | `-filled`, `-outlined`, `-disabled` |

Подробнее → [semantic_naming_rules.md](./semantic_naming_rules.md)

## 🖼 Галерея

Откройте `index.html` для интерактивного просмотра:
- Сравнение **As Is → To Be**
- Click-to-copy имена иконок
- Фильтрация по категориям
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

# 🏢 Enterprise Semantic Naming Rules

## Philosophy
Follows industry-standard conventions (Uber Base Web, Material Design, Carbon) prioritizing **clarity**, **professionalism**, and **explicitness** over brevity.

**Core Rule**: No abstract slang. Use standard English descriptors.
-   ❌ `x.svg` (Too abstract, "dev slang")
-   ✅ `close.svg` (Clear semantic meaning)

## Taxonomy & Standards

### 1. Common Actions
-   **Close/Cancel**: `close` (Standard for modals/dialogs).
-   **Add/New**: `add` (Functional, industry-standard — used by Material Design, Ant Design).
-   **Delete/Remove**: `delete` (Standard action, distinct icon from `trash`).
-   **Trash**: `trash` (Separate visual icon — trash bin shape. Use when showing a "move to trash" metaphor).
-   **Edit**: `edit` (Functional naming over visual `pencil`).
-   **Search**: `search`. (Never `magnifier`).
-   **Menu**: `menu-overflow` (Kebab/3-dot menu, prefixed for grouping with `menu-grid`).

### 2. Navigation
-   **Arrows**: `arrow-left`, `arrow-right`, `arrow-down`, `arrow-up` (Directional).
-   **Sort arrows**: `arrow-ascending`, `arrow-descending` (Functional naming for sort indicators).
-   **Curved arrow**: `arrow-curved` (Visual descriptor; used contextually for undo/return actions).
-   **Chevrons**: `chevron-left`, `chevron-right` (Stemless).
-   **Double chevrons**: `chevron-double-left`, `chevron-double-right` (Object-first, modifier-after).
-   **Carets**: `caret-down` (Filled triangle).

### 3. Modifiers (Suffixes)
-   **Variants**: `-filled`, `-outlined` (or `-outline`), `-round`, `-alt`.
-   **Sizes**: `-small`, `-medium`, `-large` (Avoid `-sm`, `-md`).
-   **State**: `-disabled`, `-active`, `-error`, `-warning` (not colors like `-orange`).

### 4. Grouping Prefixes
-   **Brands**: `brand-` (e.g., `brand-cisco`, `brand-bsd`).
-   **OS**: `os-` (e.g., `os-android`, `os-windows`).
-   **Interfaces**: `interface-` (e.g., `interface-bond-on`, `interface-hydra-error`).
-   **NAT**: `nat-` (e.g., `nat-source`, `nat-destination`).
-   **Indicators**: `indicator-` (e.g., `indicator-online`, `indicator-disabled`).
-   **Severity**: `severity-` (e.g., `severity-alert`, `severity-emergency`).
-   **Priority**: `priority-` (e.g., `priority-critical`, `priority-important`, `priority-low`).

## Key Decisions Log

| #  | Original Concept | Alternatives Considered | **Final Decision** | Reasoning |
|----|-----------------|------------------------|-------------------|-----------|
| 1  | Plus sign       | `plus` (visual)        | **`add`**         | Functional naming, industry standard |
| 2  | X / Cross       | `x`                    | **`close`**       | Clear semantic meaning |
| 3  | Trash Bin       | merged into `delete`   | **`trash`** (separate) | Visually distinct icon, different UI context |
| 4  | 3 dots          | `kebab-menu`, `overflow`| **`menu-overflow`** | Groups with `menu-grid` |
| 5  | Magnifying glass| `magnifier`            | **`search`**      | Functional naming |
| 6  | Gear            | `gear`                 | **`settings`**    | Functional naming |
| 7  | Curved arrow    | `arrow-undo`           | **`arrow-curved`** | Visual descriptor, multi-context use |
| 8  | Sort arrows     | `arrow-up/down-sort`   | **`arrow-ascending/descending`** | More descriptive |
| 9  | Double chevron  | `chevron-left-double`  | **`chevron-double-left`** | Object-first pattern, consistent with CSS |
| 10 | Move to end     | `move-end`             | **`move-to-bottom`** | Explicit and clear |

# Task: Icon Library Audit and Organization

## Phase 1: Analysis & Inventory
- [x] Parse icon folder structure and inventory contents <!-- id: 0 -->
- [x] Create detailed Inventory Summary (pattern detection, duplicates) <!-- id: 1 -->

## Phase 2: Audit & Semantic Naming
- [x] Define Semantic Naming Rules (kebab-case, verb-object, etc.) <!-- id: 2 -->
- [x] Generate CSV Audit Table <!-- id: 3 -->
    - Columns: Original Name, New Name, Category, Figma Tags, Notes
    - Map all 207 icons to clean kebab-case names
    - Resolve duplicates (e.g., `Edit` vs `Edit-1`)
    - Categorize icons (UI, Brand, Security, Text, etc.)

## Phase 3: Deliverables
- [x] Verify CSV against constraints <!-- id: 4 -->
- [x] Generate final artifacts (Inventory, CSV, Naming Rules) <!-- id: 5 -->
- [x] Create automated renaming script (`apply_renames.sh`) <!-- id: 6 -->

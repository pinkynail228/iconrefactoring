
import csv
import re

files = [
    "Actions.svg", "Add to filter.svg", "Add to incident.svg", "Add.svg", "Align center.svg", 
    "Align left.svg", "Align right.svg", "Analytics rule condition.svg", "Arrow ascending.svg", 
    "Arrow descending.svg", "Arrow down.svg", "Arrow left.svg", "Arrow right.svg", 
    "Attachement light.svg", "Attachement.svg", "BSD.svg", "Bar chart.svg", "Bell empty.svg", 
    "Bell filled.svg", "Bell new.svg", "Block.svg", "Bold.svg", "Bullet list.svg", 
    "Certificate.svg", "Check mark.svg", "Check mark_default.svg", "Check mark_disabled.svg", 
    "Chevron left.svg", "Chevron right.svg", "Cisco.svg", "Clear.svg", "Close small.svg", 
    "Close.svg", "Collapse.svg", "Comment.svg", "Computer with user.svg", "Copy.svg", 
    "Create incident.svg", "Curved arrow.svg", "Day.svg", "Decrease font.svg", 
    "Decrypt forward.svg", "Decrypt.svg", "Delete.svg", "Destination NAT.svg", "Disable.svg", 
    "Disabled.svg", "DoS protection.svg", "Double chevron left.svg", "Double chevron right.svg", 
    "Edit-1.svg", "Edit.svg", "Ellipsis.svg", "Error.svg", "Expand.svg", "Export CSV.svg", 
    "Export.svg", "Eye hide.svg", "Eye-1.svg", "Eye.svg", "File CSV.svg", "File HTML.svg", 
    "File PCAP.svg", "File PDF.svg", "File XML.svg", "File ZIP.svg", "Fill color.svg", 
    "Filter applied.svg", "Filter outline.svg", "Filter.svg", "Flag dbg.svg", "Flag en.svg", 
    "Flag ru.svg", "Fork.svg", "Forward.svg", "Gear subtle.svg", "Geo IP.svg", 
    "Globe dark.svg", "Globe.svg", "Grid menu.svg", "Help.svg", "Hierarchy.svg", 
    "History.svg", "Import.svg", "In progress.svg", "Inactive firewall.svg", "Increase font.svg", 
    "Info.svg", "Interface bond-off.svg", "Interface bond-on.svg", "Interface deleted.svg", 
    "Interface error.svg", "Interface hydra-error.svg", "Interface hydra-off.svg", 
    "Interface hydra-on.svg", "Interface off.svg", "Interface vian.svg", "Interface.svg", 
    "Italic.svg", "Kaspersky Anti-Virus.svg", "Key.svg", "Light bulb.svg", "Line chart.svg", 
    "Link.svg", "Loader.svg", "Log session start.svg", "Log success.svg", "Log.svg", 
    "Logging disabled.svg", "Logging enabled.svg", "Logout subtle.svg", "Magnifier.svg", 
    "Mixed.svg", "More.svg", "Move down.svg", "Move to bottom.svg", "Move to top.svg", 
    "Move up.svg", "Nat netmap.svg", "New page.svg", "New_Eye.svg", "New_Hide_Eye.svg", 
    "Night.svg", "NoDNAT.svg", "NoNAT.svg", "Numbered list.svg", "OS Android.svg", 
    "OS IOS.svg", "OS Linux.svg", "OS MAC.svg", "OS Windows mobile.svg", "OS Windows.svg", 
    "Offline.svg", "One column.svg", "Online.svg", "Oracle.svg", "Override.svg", 
    "Padlock grey.svg", "Padlock orange.svg", "Padlock subtle.svg", "Padlocks.svg", 
    "Pause.svg", "Pie chart.svg", "Pin.svg", "Placeholder.svg", "Police.svg", "Print.svg", 
    "Priority critical.svg", "Priority important.svg", "Priority low.svg", "Priority normal.svg", 
    "Question dark.svg", "Question subtle.svg", "Question.svg", "React.svg", 
    "Redirect green.svg", "Redirect yellow.svg", "Refresh-1.svg", "Refresh.svg", 
    "Remove from incident.svg", "Reset-1.svg", "Reset.svg", "Restore default.svg", 
    "Run script.svg", "Save.svg", "Saved filter.svg", "Server.svg", "Settings.svg", 
    "Severity alert.svg", "Severity debug.svg", "Severity emergency.svg", "Severity notice.svg", 
    "Shape.svg", "Shield green.svg", "Source NAT.svg", "Source code.svg", "Star.svg", 
    "Start.svg", "Stepper.svg", "Success.svg", "Table view.svg", "Table.svg", 
    "Text color.svg", "Text view.svg", "Three columns.svg", "Trash dark.svg", 
    "Trash outlined.svg", "Trash.svg", "Two columns.svg", "Two-sided arrows green.svg", 
    "Undefined.svg", "Underline.svg", "Update.svg", "Upload.svg", "User subtle.svg", 
    "User.svg", "Userid ignore.svg", "Userid login.svg", "Userid logout.svg", 
    "Video subtle.svg", "Virus cloud.svg", "Warning-1.svg", "Warning.svg", "Webhook.svg", 
    "Whistle.svg", "Workflow.svg", "dnsbl.svg"
]

def get_category(name_lower):
    if any(x in name_lower for x in ['arrow', 'chevron', 'move', 'forward', 'collapse', 'expand']): return "Navigation"
    if any(x in name_lower for x in ['add', 'edit', 'delete', 'remove', 'save', 'copy', 'paste', 'trash', 'clear', 'reset', 'update', 'upload', 'import', 'export']): return "Actions"
    if any(x in name_lower for x in ['check', 'error', 'warning', 'info', 'help', 'success', 'flag', 'question', 'priority', 'severity']): return "Status"
    if any(x in name_lower for x in ['file', 'folder', 'attachment', 'document', 'pdf', 'csv', 'html']): return "Files"
    if any(x in name_lower for x in ['bold', 'italic', 'underline', 'font', 'align', 'list', 'text']): return "Editor"
    if any(x in name_lower for x in ['lock', 'unlock', 'key', 'shield', 'decrypt', 'virus', 'dos', 'auth']): return "Security"
    if any(x in name_lower for x in ['cisco', 'oracle', 'kaspersky', 'android', 'linux', 'windows', 'ios', 'mac', 'bsd']): return "Brands"
    if any(x in name_lower for x in ['nat', 'interface', 'firewall', 'server', 'network', 'ip', 'geo']): return "Network"
    if any(x in name_lower for x in ['chart', 'graph', 'analytics']): return "Data"
    return "UI"

overrides = {
    "Actions": "overflow", # Kebab menu -> overflow
    "Add": "plus",
    "Add to filter": "filter-plus",
    "Add to incident": "incident-plus",
    "Attachement": "attachment",
    "Attachement light": "attachment-light",
    "Bell empty": "bell",
    "Bell filled": "bell-filled",
    "Bell new": "bell-notification",
    "Check mark": "check",
    "Check mark_default": "check",
    "Check mark_disabled": "check-disabled",
    "Close small": "close-small",
    "Close": "close",
    "Delete": "delete",
    "Trash": "delete", # Consolidating to delete as per Uber/Enterprise
    "Edit": "edit",
    "Edit-1": "edit-alt",
    "Eye": "eye",
    "Eye hide": "eye-off",
    "New_Eye": "eye-outline",
    "New_Hide_Eye": "eye-off-outline",
    "Eye-1": "eye-alt",
    "Gear subtle": "settings-subtle",
    "Magnifier": "search",
    "More": "more-horizontal",
    "Padlock grey": "lock",
    "Padlock orange": "lock-warning",
    "Padlock subtle": "lock-subtle",
    "Padlocks": "lock-multiple",
    "Reset-1": "reset-alt",
    "Remove from incident": "incident-remove",
    "User": "person", # Uber often uses person for generic user
    "User subtle": "person-subtle",
    "Computer with user": "computer-person",
    "Two-sided arrows green": "arrow-swap",
    "Redirect green": "redirect",
    "Redirect yellow": "redirect-warning",
    "Shield green": "shield-check",
    "Warning": "warning",
    "Warning-1": "warning-alt",
    "Refresh": "refresh",
    "Refresh-1": "refresh-alt",
    "NoDNAT": "no-dnat",
    "NoNAT": "no-nat",
    "Flag dbg": "flag-debug"
}

def clean_name(filename):
    name = filename.replace(".svg", "")
    
    # Handle the overrides first if exact match
    if name in overrides:
        return overrides[name]
        
    clean = name.lower()
    
    # Fix Userid -> user-id
    clean = clean.replace("userid", "user-id")
    
    clean = clean.replace(" ", "-").replace("_", "-")
    clean = re.sub(r'-+', '-', clean) 
    
    # Specific fixes
    clean = clean.replace("attachement", "attachment")
    
    return clean

def generate_tags(new_name, category):
    parts = new_name.split("-")
    tags = set(parts)
    tags.add(category.lower())
    
    # Synonyms
    if "trash" in parts or "delete" in parts: tags.update(["remove", "bin", "discard"])
    if "edit" in parts: tags.update(["pencil", "change", "modify"])
    if "add" in parts: tags.update(["plus", "create", "new"])
    if "settings" in parts or "gear" in parts: tags.update(["preferences", "config", "options"])
    if "search" in parts or "magnifier" in parts: tags.update(["find", "lookup", "query"])
    if "user" in parts: tags.update(["profile", "person", "account"])
    if "arrow" in parts: tags.update(["direction", "pointer"])
    if "lock" in parts: tags.update(["security", "protect", "private"])
    
    return ", ".join(sorted(list(tags)))

csv_path = "/Users/pnklrd/.gemini/antigravity/brain/5475502a-4078-4f1f-b821-011627c1e9fe/icon_audit.csv"
with open(csv_path, "w", encoding="utf-8") as f:
    f.write("Original Name;New Name;Category;Figma Tags;Notes\n")

    for f_name in sorted(files):
        cat = get_category(f_name.lower())
        new = clean_name(f_name)
        tags = generate_tags(new, cat)
        
        # Note generation
        notes = []
        if f_name.replace(".svg","") != new and f_name.lower().replace(".svg","").replace(" ","-") != new:
            notes.append("Refactored")
        if "attachement" in f_name.lower():
            notes.append("Typo fixed")
        if "Remove from incident" in f_name or "Add to" in f_name:
            notes.append("Standardized verb-object")
        
        f.write(f"{f_name};{new}.svg;{cat};{tags};{', '.join(notes)}\n")

print(f"CSV generated at {csv_path}")

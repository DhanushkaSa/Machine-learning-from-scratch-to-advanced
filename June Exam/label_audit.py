# Each line below is one input() call until EOF

fold_case = False
bind_name = None
data_rows = []

while True:
    try:
        line = input()
    except EOFError:
        break

    # Ignore blank lines and comment lines
    if not line.strip() or line.strip().startswith('#'):
        continue

    # Handle FOLD case configuration directive
    if line.strip() == 'FOLD case':
        fold_case = True
        continue

    # Handle BIND duplicate NAME configuration directive
    if line.strip().startswith('BIND duplicate '):
        bind_name = line.strip()[len('BIND duplicate '):]
        continue

    # Store data rows
    data_rows.append(line.strip())


def normalize(label, fold_case):
    """Normalize label based on fold_case setting."""
    if fold_case:
        return label.casefold()
    return label


# Normalize all labels
normalized_labels = [normalize(row, fold_case) for row in data_rows]

# Count occurrences of each label manually (no Counter)
label_counts = {}
for label in normalized_labels:
    if label in label_counts:
        label_counts[label] += 1
    else:
        label_counts[label] = 1

# Check if BIND applies
if bind_name is not None:
    normalized_bind = normalize(bind_name, fold_case)
    bind_count = label_counts.get(normalized_bind, 0)

    if bind_count >= 2:
        print('unique=1')
        print('has_duplicates=yes')
    else:
        # BIND name never appears at least twice, ignore directive
        # Fall through to normal rules
        bind_name = None

if bind_name is None:
    # Normal counting rules
    unique_count = len(label_counts)
    has_duplicates = any(count > 1 for count in label_counts.values())

    print(f'unique={unique_count}')
    if has_duplicates:
        print('has_duplicates=yes')
    else:
        print('has_duplicates=no')
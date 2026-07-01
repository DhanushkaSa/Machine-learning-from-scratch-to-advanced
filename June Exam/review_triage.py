# Each line below is one input() call until EOF

watchlist = []
data_rows = []

while True:
    try:
        line = input()
    except EOFError:
        break

    # Ignore comment lines
    if line.strip().startswith('#'):
        continue

    # Handle WATCHLIST configuration lines
    if line.strip().startswith('WATCHLIST'):
        labels_part = line.strip()[len('WATCHLIST'):].strip()
        watchlist = labels_part.split(',')
        continue

    # Store data rows for processing
    data_rows.append(line)


def get_priority(label, confidence, watchlist):
    """Return priority band for a given label and confidence."""
    # Watchlist override takes highest priority
    if label in watchlist:
        return 'HIGH'

    # Apply band rules
    if confidence < 0.50 or label == 'unknown':
        return 'HIGH'
    elif 0.50 <= confidence < 0.80:
        return 'MEDIUM'
    else:
        return 'LOW'


for row in data_rows:
    # Split on the last comma to separate label and confidence
    last_comma = row.rfind(',')
    raw_label = row[:last_comma]
    raw_confidence = row[last_comma + 1:]

    label = raw_label.strip().lower()
    confidence = float(raw_confidence.strip())

    priority = get_priority(label, confidence, watchlist)
    print(priority)
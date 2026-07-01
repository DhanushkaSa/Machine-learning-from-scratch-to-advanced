# Each line below is one input() call until EOF

allow_spam = False
age_max = 65
data_rows = []

while True:
    try:
        line = input()
    except EOFError:
        break

    # Ignore blank lines and comment lines
    if not line.strip() or line.strip().startswith('#'):
        continue

    # Handle ALLOW spam configuration line
    if line.strip() == 'ALLOW spam':
        allow_spam = True
        continue

    # Handle AGE max=N configuration line
    if line.strip().startswith('AGE max='):
        age_max = int(line.strip()[len('AGE max='):])
        continue

    # Store data rows with current config snapshot
    data_rows.append((line.strip(), allow_spam, age_max))


def is_eligible(row, allow_spam, age_max):
    """Return True if the sample meets all eligibility criteria."""
    parts = row.split('|')
    age = int(parts[0])
    label = parts[1].strip().lower()
    raw_score = parts[2].strip()
    country = parts[3].strip()
    is_premium = parts[4].strip().lower() == 'true'
    has_missing = parts[5].strip().lower() == 'true'

    # Check age between 18 and age_max inclusive
    if not (18 <= age <= age_max):
        return False

    # Check label is not spam (unless ALLOW spam is active)
    if label == 'spam' and not allow_spam:
        return False

    # Check score is not missing and >= 0.60
    if raw_score == '' or raw_score.upper() == 'NONE':
        return False
    if float(raw_score) < 0.60:
        return False

    # Check country is 'LK' OR is_premium is True
    if not (country == 'LK' or is_premium):
        return False

    # Check has_missing is False
    if has_missing:
        return False

    return True


count = 0

for row, allow_spam, age_max in data_rows:
    if is_eligible(row, allow_spam, age_max):
        count += 1

print(count)
values = []
threshold = None

while True:
    try:
        line = input()
    except EOFError:
        break

    original = line
    line = line.strip()

    # Ignore blank lines
    if line == "":
        continue

    # Ignore comments
    if line.startswith("#"):
        continue

    # Handle configuration line
    if line.startswith("DROP below="):
        try:
            threshold = float(line[len("DROP below="):])
        except ValueError:
            pass
        continue

    # Try converting to float
    try:
        number = float(line)
        values.append(number)
    except ValueError:
        print(f"Skipping invalid value: {original}")

# Build final list using a list comprehension
if threshold is not None:
    kept_values = [x for x in values if x >= threshold]
else:
    kept_values = [x for x in values]

# Output
if not kept_values:
    print("No valid values")
else:
    print(kept_values)
    average = sum(kept_values) / len(kept_values)
    print(f"{average:.3f}")
# Each line below is one input() call until EOF


class Model:
    """Represents a registered model with a shared framework class variable."""

    framework = 'CAME-ML'

    def __init__(self, name):
        """Initialise the model with a name."""
        self.name = name


lines = []

while True:
    try:
        line = input()
    except EOFError:
        break

    # Ignore blank lines and comment lines
    if not line.strip() or line.strip().startswith('#'):
        continue

    lines.append(line.strip())


for line in lines:
    # Handle FRAMEWORK configuration directive
    if line.startswith('FRAMEWORK '):
        new_framework = line[len('FRAMEWORK '):]
        Model.framework = new_framework
        continue

    # Register model and print result
    model = Model(line)
    print(f'{model.name}|{Model.framework}')

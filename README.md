# Machine Learning: From Scratch to Advanced

A practical, notebook-first learning journey through Python, data analysis, machine learning, and neural networks. The repository is organized into day-by-day lessons, exercises, datasets, and exam materials, with examples ranging from Python fundamentals to CNNs and experiment tracking.

> **Current focus:** Learn by running and modifying the notebooks. The contents of each day may vary, and the roadmap grows as new material is added.

## Contents

- [Learning roadmap](#learning-roadmap)
- [Repository structure](#repository-structure)
- [Getting started](#getting-started)
- [Recommended workflow](#recommended-workflow)
- [Tools and libraries](#tools-and-libraries)
- [Contributing](#contributing)
- [License](#license)

## Learning roadmap

The numbered folders provide a chronological path. Topics below are based on the materials currently present; not every day is a complete lesson or project.

| Folder | Materials and topics |
| --- | --- |
| `Day 1`–`Day 4` | Python foundations, programming practice, notebooks, and object-oriented programming exercises |
| `Day 5`–`Day 8` | Mathematics and vector practice, data handling, and applied coding exercises |
| `Day 9`–`Day 13` | Customer and other dataset exploration, CSV workflows, regression-oriented exercises, and review data |
| `Day 14`–`Day 16` | Continued machine-learning practice; includes a breast-cancer XGBoost example, retail customer data, and MLflow-related materials |
| `Day 17`–`Day 18` | Neural-network concepts and notebook work, including a dense neural-network diagram and a customer prediction model |
| `Day 19` | XGBoost experiment tracking with MLflow, including a notebook and tracking artifacts |
| `Day 20` | CNN notebook examples, including `real_cnn.ipynb` |
| `June Exam` | Python assessment scripts for label auditing, model tagging, review triage, sample checks, and score cleaning |
| `July Exam` | Python assignment, customer-data cleaning dataset, and notebook assessment |

Some day numbers may be absent or contain only a small amount of material. Check each folder for its current notebooks, scripts, and datasets.

## Repository structure

```text
Machine-learning-from-scratch-to-advanced/
├── Day 1/ ... Day 10/
├── Day 12/ ... Day 20/
├── June Exam/
├── July Exam/
└── README.md
```

A day folder may contain Jupyter notebooks (`.ipynb`), Python scripts (`.py`), CSV datasets, model files, diagrams, or experiment-tracking artifacts. Not all folders have the same structure.

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/DhanushkaSa/Machine-learning-from-scratch-to-advanced.git
cd Machine-learning-from-scratch-to-advanced
```

### 2. Create and activate a virtual environment (recommended)

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install notebook and common data-science packages

```bash
python -m pip install --upgrade pip
python -m pip install jupyter numpy pandas matplotlib seaborn scikit-learn
```

Some notebooks use additional packages, such as PyTorch, XGBoost, or MLflow. Install the package required by the specific notebook you plan to run. For PyTorch, use the installation instructions appropriate for your operating system and hardware at [pytorch.org](https://pytorch.org/get-started/locally/).

### 4. Launch Jupyter

```bash
jupyter notebook
```

Open a notebook from the relevant `Day` folder. Run it from that folder when the notebook reads local files using relative paths. If a notebook reports a missing package, install that notebook's dependency in the active environment and restart the kernel.

## Recommended workflow

1. Start with the earliest available day and work forward.
2. Read each notebook's explanations and run the cells in order.
3. Try changing inputs and parameters to see how results change.
4. Keep data files alongside the notebook when it expects relative paths.
5. Complete practice and exam materials after working through the related concepts.
6. Record package requirements and any setup notes for notebooks that need extra dependencies.

## Tools and libraries

The repository is primarily made up of Jupyter notebooks, with Python scripts and data files. Depending on the lesson, you may encounter:

- Python and Jupyter
- NumPy and Pandas
- Matplotlib and Seaborn
- scikit-learn
- PyTorch
- XGBoost
- MLflow
- CSV datasets and model artifacts

The exact dependencies vary by notebook; there is not currently a single repository-wide dependency file.

## Contributing

Suggestions, corrections, and learning materials are welcome. Open an issue to describe a problem or proposed improvement, or submit a pull request with a clear summary of your changes. Please keep new content organized in the relevant day folder and include any required setup instructions.

## Author

Created and maintained by [DhanushkaSa](https://github.com/DhanushkaSa).

## License

No license is currently specified. Unless a license is added, reuse and redistribution of this repository's contents may be restricted by default copyright law.

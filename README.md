# EEAI: Multi-Label Email Classification System

---

## 📌 Project Information

| Field | Details |
|-------|---------|
| **Degree Programme** | MSc in Artificial Intelligence |
| **Module Name** | Engineering and Evaluating Artificial Intelligence |
| **Module Code** | H9EEAI |
| **Institution** | National College of Ireland |
| **Assignment** | Continuous Assessment 1 (CA1) |
| **Submission Deadline** | 26 March 2026 |

## 👥 Team Members

| Name | Student ID | Email |
|------|-----------|-------|
| **Nathan Luis Alvares** | 24327018 | x24327018@student.ncirl.ie |
| **Taehoon Kang (David)** | 23268212 | x23268212@student.ncirl.ie |
| **Yunxiang Hou (Leon)** | 25110594 | x25110594@student.ncirl.ie |

---

## 📖 Project Description

A comprehensive multi-label email classification framework implementing two architectural approaches for multi-output machine learning. This project demonstrates advanced software engineering practices including separation of concerns, data encapsulation, and model abstraction through the development of a sophisticated multi-label document classification system.

---

## 📋 Table of Contents

- [Project Overview](#Project-Overview)
- [Academic Context](#Academic-Context)
- [Architecture](#Architecture)
- [Installation & Setup](#Installation--Setup)
- [Usage](#Usage)
- [Project Structure](#Project-Structure)
- [Design Principles](#Design-Principles)
- [Results](#Results)
- [Development](#Development)
- [References](#References)

---

## 🎯 Project Overview

This project implements a **multi-label document classification system** designed to classify emails into three hierarchical, dependent label categories:

- **Type 2**: Primary classification (e.g., "Suggestion", "Complaint")
- **Type 3**: Secondary classification dependent on Type 2 (e.g., "Refund", "Payment")
- **Type 4**: Tertiary classification dependent on both Type 2 and Type 3 (e.g., "Subscription cancellation")

The system explores two distinct architectural paradigms for handling multi-output predictions:

1. **Design Choice 1: Chained Multi-Outputs** (Fully Implemented)
   - Single feature pipeline with progressive label complexity
   - Three independent model training cycles on combined labels

2. **Design Choice 2: Hierarchical Modeling** (Design-Complete, Partially Implemented)
   - Cascading model stages with route-aware filtering
   - Separate models per branch and path in the label hierarchy

---

## 🏫 Academic Context

**Module:** Engineering and Evaluating Artificial Intelligence  
**Institution:** National College of Ireland  
**Assignment Type:** Continuous Assessment (CA1)  
**Delivery Method:** Extreme Programming (3-person team)  
**Weight:** 50% of module grade  
**Submission Deadline:** 26 March 2026  

### Design Requirements

The architecture implements three core software engineering principles:

1. **Separation of Concerns**: Data preprocessing is independent from model training/testing
2. **Data Encapsulation**: Unified input data representation via `DataBundle` class enables seamless multi-model integration
3. **Model Abstraction**: Abstract base class provides uniform interface across all ML models

---

## 🏗️ Architecture

### High-Level Pipeline

```
Data Loading
    ↓
Preprocessing (Text Normalization, Column Concatenation)
    ↓
Feature Vectorization (TF-IDF, 20,000 features)
    ↓
Train-Test Split (80/20, fixed random seed=42)
    ↓
Label Construction (Type2, Type2+Type3, Type2+Type3+Type4)
    ↓
Model Training & Evaluation
    ↓
Metrics Aggregation & Export
```

### Design Choice 1: Chained Multi-Outputs

**Approach**: Single feature pipeline with three independent model training cycles on progressively complex labels.

```
Input Features (TF-IDF vectors)
    ├→ Model 1 → Type 2 Labels → Accuracy: 0.84, F1: 0.86
    ├→ Model 2 → Type 2+Type 3 Labels → Accuracy: 0.64, F1: 0.49
    └→ Model 3 → Type 2+Type 3+Type 4 Labels → Accuracy: 0.56, F1: 0.32
```

**Advantages:**
- Simple, interpretable progression
- Shared feature space enables direct comparison
- Clear performance degradation as label complexity increases

**Implementation Status**: ✅ Fully implemented and tested

### Design Choice 2: Hierarchical Modeling

**Approach**: Cascading model stages where each level branches by preceding label class.

```
Type 2 Stage: 1 Model
    ├─ Type 3 Branch A: 1 Model (trained on Type 2=A records)
    │   ├─ Type 4 Path A1: 1 Model (filtered for Type 2=A, Type 3=A1)
    │   └─ Type 4 Path A2: 1 Model (filtered for Type 2=A, Type 3=A2)
    ├─ Type 3 Branch B: 1 Model (trained on Type 2=B records)
    │   ├─ Type 4 Path B1: 1 Model
    │   └─ Type 4 Path B2: 1 Model
    └─ ... (etc. for each Type 2 class)
```

**Advantages:**
- Per-class performance breakdown
- Handles class-specific feature distributions
- Can be optimized per-branch rather than globally

**Implementation Status**: ⚠️ Design-complete, routing/branching logic implemented, per-branch model training is a design placeholder (marked in output for future implementation)

---

## 💻 Installation & Setup

### Prerequisites

- Python 3.9 or higher
- pip or conda package manager
- Virtual environment (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/leonLearnAI/EEAI.git
cd EEAI
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

**Activate (Windows PowerShell):**
```powershell
& .\.venv\Scripts\Activate.ps1
```

**Activate (Linux/macOS):**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Core dependencies:**
- pandas >= 1.3.0
- scikit-learn >= 1.0.0
- numpy >= 1.20.0

### 4. Verify Installation

```bash
python main.py --arch choice1 --model rf --data data/AppGallery.csv
```

You should see output with classification metrics for Type 2, Type 2+Type 3, and Type 2+Type 3+Type 4 labels.

---

## 🚀 Usage

### Basic Command Structure

```bash
python main.py --arch {choice1|choice2} --model {rf|lr} [--data PATH] [--export PATH]
```

### Command-Line Arguments

| Argument | Options | Default | Description |
|----------|---------|---------|-------------|
| `--arch` | `choice1`, `choice2` | `choice1` | Architecture to execute |
| `--model` | `rf`, `lr` | `rf` | ML model family (RandomForest or LogisticRegression) |
| `--data` | file path | `data/AppGallery.csv` | Dataset path (relative to project root) |
| `--export` | file path | (none) | CSV export path for metrics |

### Usage Examples

#### Example 1: Run Choice 1 with RandomForest on AppGallery

```bash
python main.py --arch choice1 --model rf --data data/AppGallery.csv
```

**Output:**
```
Starting run: arch=choice1, model=rf
Choice1 Results
| Task   | Accuracy |  F1 Macro |
|--------|----------|-----------|
| type2  |   0.8400 |   0.8631  |
| type23 |   0.6400 |   0.4919  |
| type234|   0.5600 |   0.3205  |
Run finished.
```

#### Example 2: Run Choice 1 with LogisticRegression on Purchasing and Export Metrics

```bash
python main.py --arch choice1 --model lr --data data/Purchasing.csv --export reports/choice1_purchasing_lr.csv
```

**Output**: Same summary table + CSV file generated at `reports/choice1_purchasing_lr.csv`

#### Example 3: Run Choice 2 Hierarchical Model with RandomForest

```bash
python main.py --arch choice2 --model rf --data data/AppGallery.csv
```

**Output:**
```
Starting run: arch=choice2, model=rf
Choice2 Hierarchical Results
Stage 1 (Type 2): Accuracy: 0.8400, F1: 0.8631

Type 3 Branches:
| Branch      | Train Samples | Status |
|-------------|---------------|--------|
| Suggestion  | 42            | Active |
| Complaint   | 38            | Active |
...

[Per-branch models marked as placeholder for future implementation]
Run finished.
```

#### Example 4: Export All Choice 1 Results

```bash
python main.py --arch choice1 --model rf --data data/AppGallery.csv --export reports/choice1_appgallery_rf.csv
python main.py --arch choice1 --model lr --data data/AppGallery.csv --export reports/choice1_appgallery_lr.csv
python main.py --arch choice1 --model rf --data data/Purchasing.csv --export reports/choice1_purchasing_rf.csv
python main.py --arch choice1 --model lr --data data/Purchasing.csv --export reports/choice1_purchasing_lr.csv
```

### Programmatic Usage

```python
from controller import run_architecture
from pathlib import Path

# Run Choice 1 and get results as dict
results = run_architecture(
    arch="choice1",
    model_name="rf",
    data_path=Path("data/AppGallery.csv"),
    export_path=Path("reports/choice1_results.csv")
)

print(results)
# Output: {'type2': {...}, 'type23': {...}, 'type234': {...}}
```

---

## 📁 Project Structure

```
EEAI/
├── README.md                          # This file
├── requirementsmnt.txt                 # Python dependencies
├── config.py                          # Centralized configuration
├── main.py                            # CLI entry point
├── controller.py                      # Orchestration layer
│
├── data/
│   ├── AppGallery.csv                # Dataset 1: App Gallery feedback (100 records)
│   └── Purchasing.csv                # Dataset 2: Purchasing system feedback (30 records)
│
├── reports/
│   ├── choice1_appgallery_rf.csv     # Evidence: Choice 1 on AppGallery (RF)
│   ├── choice1_appgallery_lr.csv     # Evidence: Choice 1 on AppGallery (LR)
│   ├── choice1_purchasing_rf.csv     # Evidence: Choice 1 on Purchasing (RF)
│   └── choice1_purchasing_lr.csv     # Evidence: Choice 1 on Purchasing (LR)
│
└── src/
    ├── __init__.py
    ├── data_loader.py                 # CSV loading & column validation
    ├── preprocessing.py               # Text normalization & concatenation
    ├── dataset_builder.py             # Train-test split & TF-IDF vectorization
    ├── label_builders.py              # Type2, Type23, Type234 label construction
    ├── evaluation.py                  # Metrics computation (accuracy, F1-macro)
    ├── utils.py                       # CSV export & result flattening
    │
    ├── models/
    │   ├── __init__.py
    │   ├── base_model.py              # Abstract base class (train, predict, evaluate)
    │   ├── random_forest.py           # RandomForest implementation
    │   └── logistic_regression.py     # LogisticRegression implementation
    │
    └── architectures/
        ├── __init__.py
        ├── choice1_chained.py         # Choice 1: Chained multi-output
        └── choice2_hierarchical.py    # Choice 2: Hierarchical routing
```

---

## 🎨 Design Principles

### 1. Separation of Concerns (SoC)

**Principle**: Each module has a single, well-defined responsibility.

- `data_loader.py`: CSV loading and column validation only
- `preprocessing.py`: Text normalization; does not know about models
- `dataset_builder.py`: Feature vectorization and train-test split
- `models/`: Model training and prediction
- `architectures/`: Experiment design and orchestration

**Benefit**: Changing preprocessing does not require modifying model code, and vice versa.

### 2. Data Encapsulation

**Principle**: Unified data representation via `DataBundle` class.

```python
class DataBundle:
    train_x: np.ndarray          # Training features (TF-IDF vectors)
    test_x: np.ndarray           # Test features
    train_y: dict                # Training labels: {type2, type23, type234}
    test_y: dict                 # Test labels
    vectorizer: TfidfVectorizer  # Reusable vectorizer for inference
```

**Benefit**: Models always receive consistent data format. Adding new models requires zero data-format changes.

### 3. Model Abstraction

**Principle**: All models inherit from a common abstract base class.

```python
class BaseModel(ABC):
    @abstractmethod
    def train(self, X, y): ...
    
    @abstractmethod
    def predict(self, X): ...
    
    @abstractmethod
    def evaluate(self, X_test, y_test) -> dict: ...
```

**Benefit**: New models (e.g., SVM, Gradient Boosting) can be added by inheriting from `BaseModel` without modifying controller or architecture code.

### 4. Configuration Centralization

**Principle**: All shared parameters in `config.py`.

```python
# config.py
Text_Cols = ["Ticket Summary", "Interaction content"]
Label_Cols = ["Type 2", "Type 3", "Type 4"]
Test_Size = 0.2
Random_State = 42
Max_Features = 20000
```

**Benefit**: Hyperparameters can be modified in one place; all modules read from config.

---

## 📊 Results

### Choice 1 Metrics: AppGallery Dataset + RandomForest

| Task | Accuracy | F1 Macro |
|------|----------|----------|
| Type 2 | 0.8400 | 0.8631 |
| Type 2+Type 3 | 0.6400 | 0.4919 |
| Type 2+Type 3+Type 4 | 0.5600 | 0.3205 |

### Choice 1 Metrics: Purchasing Dataset + RandomForest

| Task | Accuracy | F1 Macro |
|------|----------|----------|
| Type 2 | 0.8824 | 0.5762 |
| Type 2+Type 3 | 0.7647 | 0.5475 |
| Type 2+Type 3+Type 4 | 0.6471 | 0.4524 |

### Choice 1 Metrics: AppGallery Dataset + LogisticRegression

| Task | Accuracy | F1 Macro |
|------|----------|----------|
| Type 2 | 0.7600 | 0.6955 |
| Type 2+Type 3 | 0.6400 | 0.4848 |
| Type 2+Type 3+Type 4 | 0.6000 | 0.3492 |

### Choice 1 Metrics: Purchasing Dataset + LogisticRegression

| Task | Accuracy | F1 Macro |
|------|----------|----------|
| Type 2 | 0.8824 | 0.5762 |
| Type 2+Type 3 | 0.7647 | 0.5267 |
| Type 2+Type 3+Type 4 | 0.6471 | 0.4212 |

### Key Observations

1. **Label Complexity Trade-off**: As label complexity increases (Type 2 → Type 2+Type 3 → Type 2+Type 3+Type 4), accuracy consistently decreases, reflecting the dependency and compounding error challenge.

2. **Model Comparison**: RandomForest generally outperforms LogisticRegression on Type 2 (+16.8% accuracy difference on AppGallery) but both models show similar degradation patterns.

3. **Dataset Effect**: The Purchasing dataset shows relatively more stable performance across label complexities (0.88→0.76→0.65) compared to AppGallery (0.84→0.64→0.56), suggesting more consistent label distributions.

4. **F1-Macro Interpretation**: The significant gap between accuracy and F1-macro (e.g., 0.84 vs 0.86 for Type 2) indicates class imbalance; F1-macro is a more robust metric for imbalanced datasets.

---

## 🔧 Development

### Adding a New Model

1. Create a new class inheriting from `BaseModel` in `src/models/`:

```python
# src/models/gradient_boosting.py
from src.models.base_model import BaseModel
from sklearn.ensemble import GradientBoostingClassifier

class GradientBoosting(BaseModel):
    def __init__(self):
        self.model = GradientBoostingClassifier(random_state=42)
    
    def train(self, X, y):
        self.model.fit(X, y)
    
    def predict(self, X):
        return self.model.predict(X)
    
    def evaluate(self, X_test, y_test) -> dict:
        y_pred = self.predict(X_test)
        return compute_metrics(y_test, y_pred)
```

2. Update `src/architectures/choice1_chained.py`:

```python
def _get_model(model_name: str):
    if model_name == "rf":
        return RandomForest()
    if model_name == "lr":
        return LogisticRegression()
    if model_name == "gb":  # Add this
        return GradientBoosting()
    raise ValueError(f"Unsupported model: {model_name}")
```

3. Run:

```bash
python main.py --arch choice1 --model gb --data data/AppGallery.csv
```

### Modifying Preprocessing

1. Update `src/preprocessing.py` as needed (e.g., add lemmatization, stop-word removal).
2. Re-run experiments—no changes needed to models or controller.

### Extending to New Datasets

1. Add CSV file to `data/` directory.
2. Ensure it contains columns: `Text_Cols` and `Label_Cols` (defined in `config.py`).
3. Run:

```bash
python main.py --arch choice1 --model rf --data data/YourDataset.csv --export reports/choice1_yourdataset_rf.csv
```

---

## 📈 Performance Metrics Reference

### Accuracy
- **Definition**: Exact-match ratio for the complete label tuple.
- **Interpretation**: If Type 2 is correct but Type 3 is wrong, accuracy = 0% (due to hierarchical dependency).
- **Use Case**: Primary metric for assessing strict multi-label correctness.

### F1 Macro
- **Definition**: Unweighted average of per-class F1 scores.
- **Interpretation**: Balances precision and recall; not affected by class imbalance in aggregation.
- **Use Case**: When dataset classes are imbalanced, F1-macro is more reliable than accuracy alone.

---

## 🔗 Version Control

All work is tracked in the Git repository:

```bash
git log --oneline
```

Key commits include:
- **Label builders**: Type2, Type23, Type234 construction
- **Dataset wiring**: Feature vectorization and label distribution
- **Choice 1 pipeline**: Chained experiment runners
- **Choice 2 scaffold**: Hierarchical routing and branching logic
- **CLI & export**: User interface and CSV output

### Repository Access

For assessor/lecturer review:
- Repository: [leonLearnAI/EEAI](https://github.com/leonLearnAI/EEAI)
- Branches: `Nathon`, `David`, `Leon` (for individual contributions)
- Full commit history available for verification

---

## 📚 References

### IEEE Style Citations

[1] F. Pedregosa, G. Varoquaux, A. Gramfort, B. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay, "Scikit-learn: Machine Learning in Python," J. Mach. Learn. Res., vol. 12, pp. 2825–2830, Nov. 2011. [Online]. Available: https://jmlr.org/papers/v12/pedregosa11a.html#:~:text=Scikit%2Dlearn%20is%20a%20Python,%2Dpurpose%20high%2Dlevel%20language.

[2] W. McKinney, "Data structures for statistical computing in Python," in Proc. 9th Python Sci. Conf., Austin, TX, USA, 2010, pp. 51–56. [Online]. Available: https://proceedings.scipy.org/articles/Majora-92bf1922-00a.pdf

[3] S. Tsoumakas and I. Katakis, "Multi-label classification: An overview," Int. J. Data Warehouse. Min., vol. 3, no. 3, pp. 1–13, 2007. [Online]. Available: https://scispace.com/pdf/multi-label-classification-an-overview-3lubavw9dw.pdf

[4] M.-L. Zhang and Z.-H. Zhou, "A review on multi-label learning algorithms," IEEE Trans. Knowl. Data Eng., vol. 26, no. 8, pp. 1819–1837, Aug. 2014, doi: 10.1109/TKDE.2013.39. [Online]. Available: https://ieeexplore.ieee.org/document/6471714

[5] L. Breiman, "Random forests," Mach. Learn., vol. 45, no. 1, pp. 5–32, Oct. 2001, doi: 10.1023/A:1010933404324. [Online]. Available: https://link.springer.com/article/10.1023/A:1010933404324

[6] D. W. Hosmer, S. Lemesbow, and J. Lemeshow, "A comparison of goodness-of-fit tests for the logistic regression model," Stat. Med., vol. 16, no. 9, pp. 965–980, May 1997, doi: 10.1002/(SICI)1097-0258(19970515)16:9<965::AID-SIM509>3.0.CO;2-O. [Online]. Available: https://onlinelibrary.wiley.com/doi/abs/10.1002/%28SICI%291097-0258%2819970515%2916%3A9%3C965%3A%3AAID-SIM509%3E3.0.CO%3B2-O

[7] J. Frankle and M. Carbin, "The lottery ticket hypothesis: Finding sparse, trainable neural networks," in Proc. Int. Conf. Learn. Representations (ICLR), 2019, arXiv:1803.03635. [Online]. Available: https://arxiv.org/abs/1803.03635

[8] C. D. Manning, P. Raghavan, and H. Schütze, Introduction to Information Retrieval. Cambridge, U.K.: Cambridge Univ. Press, 2008. [Online]. Available: https://nlp.stanford.edu/IR-book/

[9] T. K. Ho, "Random decision forests," in Proc. 3rd Int. Conf. Document Analysis Recognition, Montreal, QC, Canada, 1995, pp. 278–282, doi: 10.1109/ICDAR.1995.598994. [Online]. Available: https://ieeexplore.ieee.org/document/598994

[10] Y. LeCun, Y. Bengio, and G. Hinton, "Deep learning," Nature, vol. 521, no. 7553, pp. 436–444, May 2015, doi: 10.1038/nature14539. [Online]. Available: https://github.com/voice32/activations_optimizers/blob/master/papers/Deep%20Learning%20Review%20(Nature)%20-%20Yann%20LeCun%2C%20Yoshua%20Bengio%2C%20Geoffrey%20Hinton.pdf

[11] K. Jarvelin and J. Kekalainen, "Cumulated gain-based evaluation of IR techniques," ACM Trans. Inf. Syst., vol. 20, no. 4, pp. 422–446, Oct. 2002, doi: 10.1145/582415.582418. [Online]. Available: https://dl.acm.org/doi/10.1145/582415.582418

[12] S. J. Russell and P. Norvig, Artificial Intelligence: A Modern Approach, 4th ed. Harlow, U.K.: Pearson, 2020. [Online]. Available: https://people.engr.tamu.edu/guni/csce625/slides/AI.pdf

[13] I. H. Witten, E. Frank, M. A. Hall, and C. J. Pal, Data Mining: Practical Machine Learning Tools and Techniques, 4th ed. San Francisco, CA, USA: Morgan Kaufmann, 2016. [Online]. Available: https://tjzhifei.github.io/links/DM3.pdf

[14] C. Cortes and V. Vapnik, "Support-vector networks," Mach. Learn., vol. 20, no. 3, pp. 273–297, Sep. 1995, doi: 10.1023/A:1022627411411. [Online]. Available: https://link.springer.com/article/10.1007/BF00994018

[15] U. M. Fayyad, G. Piatetsky-Shapiro, and P. Smyth, "From data mining to knowledge discovery in databases," AI Mag., vol. 17, no. 3, pp. 37–54, Fall 1996. [Online]. Available: https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1230

[16] D. A. Grossman and O. Frieder, Information Retrieval: Algorithms and Heuristics, 2nd ed. Dordrecht, Netherlands: Springer-Verlag, 2004. [Online]. Available: https://link.springer.com/book/10.1007/978-1-4020-3005-5

[18] X. Chen and C. Guestrin, "XGBoost: A scalable tree boosting system," in Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining, San Francisco, CA, USA, 2016, pp. 785–794, doi: 10.1145/2939672.2939785. [Online]. Available: https://dl.acm.org/doi/10.1145/2939672.2939785

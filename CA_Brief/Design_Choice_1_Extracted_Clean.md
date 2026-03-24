# Design Choice Document - Clean Extraction

## Source
- Input file: Design Choice 1.docx
- Extraction output: Design_Choice_1_extracted.txt

## Design Choice 1 - Chained Multi-Outputs

This design keeps one pipeline and one feature space, then changes only the target label across three runs.

The sequence is:
1. Type2
2. Type2 + Type3
3. Type2 + Type3 + Type4

Key idea:
- Train/test split and TF-IDF vectorizer remain fixed.
- Differences in performance should mainly reflect label complexity, not a changed split or changed feature extraction.

### Flow steps
1. Load CSV datasets into a single table `df` with text fields and Type2/Type3/Type4.
2. Build `df["text"]` by joining Ticket Summary and Interaction content.
3. Split data once with fixed seed.
4. Vectorize `df["text"]` into shared TF-IDF feature matrix `X`.
5. Build three aligned targets from same records:
   - `y2`
   - `y23` = Type2__Type3
   - `y234` = Type2__Type3__Type4
6. Run three model train/evaluate cycles using same `X`, changing only target.

### Module meaning
- Data Loader: reads and validates columns, standardizes missing values.
- Preprocessing: constructs a single stable text signal.
- Dataset Builder: fixes split once and builds TF-IDF features.
- Label Builder: creates y2, y23, y234 from same indices.
- Training/Evaluation: compares performance trend from coarse to fine label space.

### Intended outputs
- Per-run metrics (accuracy, macro F1)
- A clear trend line across y2 -> y23 -> y234

## Design Choice 2 - Hierarchical Modelling

This design keeps one pipeline and shared feature space, then uses hierarchical routing.

Pipeline logic:
1. Predict Type2 first.
2. Split into Type2 filter sets.
3. Train Type3 per Type2 branch.
4. Split again by (Type2, Type3).
5. Train Type4 per path.

### Flow steps
1. Load CSV data into `df` with text and labels.
2. Build `df["text"]`.
3. Build TF-IDF Feature Matrix `X`.
4. Train/evaluate Type2 and produce Predicted Type2.
5. Split by Type2 to create branch-specific subsets.
6. Train/evaluate Type3 per Type2 branch.
7. Split by (Type2, Type3) to create path-specific subsets.
8. Train/evaluate Type4 per path and aggregate to results summary.

### Module meaning
- Data Loader and Preprocessing behave as stable front-end.
- Dataset Builder generates reusable shared feature matrix.
- Type2 stage acts as root routing model.
- Branch/path filters determine specialized downstream model runs.
- Results summary aggregates branch/path outputs.

### Intended outputs
- Type2 root metrics
- Type3 per-branch summaries
- Type4 per-path summaries
- Warning/coverage information for sparse branches

## Overall extracted conclusion
- Choice 1 isolates effect of label complexity under fixed feature conditions.
- Choice 2 isolates effect of hierarchical routing and specialization by branch/path.
- Both designs preserve modular boundaries and reusable preprocessing/data representation.

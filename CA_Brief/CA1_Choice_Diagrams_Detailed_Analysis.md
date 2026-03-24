# CA1 Detailed Diagram Analysis (Leon Style)

This note interprets both architecture diagrams in a report-ready format with explicit components, connectors, and data elements.

## Choice 1 - Chained Multi-Outputs

### Architecture intent
Use one feature pipeline and one model family, then run three label definitions:
- Type2
- Type2+Type3
- Type2+Type3+Type4

The diagram emphasizes fair comparison by keeping split/vectorization constant.

### Components (for report table)
1. CSV Datasets source
2. Data Loader
3. Preprocessing (text join and normalize)
4. Dataset Builder (split + TF-IDF)
5. Label Builder (y2, y23, y234)
6. Model Training/Evaluation - y2
7. Model Training/Evaluation - y23
8. Model Training/Evaluation - y234

### Connectors (for report table)
1. CSV Datasets -> Data Loader
2. Data Loader -> Preprocessing
3. Preprocessing -> Dataset Builder
4. Preprocessing -> Label Builder
5. Dataset Builder -> Feature Matrix X
6. Feature Matrix X -> Model Eval y2
7. Feature Matrix X -> Model Eval y23
8. Feature Matrix X -> Model Eval y234
9. Label Builder -> Model Eval y2
10. Label Builder -> Model Eval y23
11. Label Builder -> Model Eval y234

### Data elements (for report table)
1. `df` with raw text and Type2/Type3/Type4 labels
2. `df["text"]` cleaned text field
3. `X_train`, `X_test` from shared TF-IDF vectorizer
4. `y2`, `y23`, `y234` target vectors aligned by index
5. Per-run metric dicts (accuracy, f1_macro)

### Why this design is strong
- High comparability across runs.
- Minimal confounders because features and split are fixed.
- Easy to extend to another model with same interface.

### Known limitation
- Combined labels can explode class cardinality as chain depth increases.

## Choice 2 - Hierarchical Modelling

### Architecture intent
Use sequential model stages and route data by upstream labels:
- Root model predicts Type2.
- Branch models handle Type3 per Type2 group.
- Path models handle Type4 per (Type2, Type3) path.

The diagram emphasizes specialization and route-aware modelling.

### Components (for report table)
1. CSV Datasets source
2. Data Loader
3. Preprocessing (text join and normalize)
4. Dataset Builder (split + TF-IDF)
5. Feature Matrix X
6. Model Training/Evaluation Type2
7. Predicted Type2 output
8. Split by Type2 Filter Sets
9. Filtered Subsets by Type2
10. Model Training/Evaluation Type3 per Type2 branch
11. Split by (Type2, Type3) Filter Sets
12. Filtered Subsets by (Type2, Type3)
13. Model Training/Evaluation Type4 per path
14. Results Summary

### Connectors (for report table)
1. CSV Datasets -> Data Loader
2. Data Loader -> Preprocessing
3. Preprocessing -> Dataset Builder
4. Dataset Builder -> Feature Matrix X
5. Feature Matrix X -> Model Type2
6. Model Type2 -> Predicted Type2
7. Predicted Type2 -> Split by Type2
8. Split by Type2 -> Filtered Subsets by Type2
9. Filtered Subsets by Type2 -> Model Type3 per branch
10. Model Type3 per branch -> Split by (Type2, Type3)
11. Split by (Type2, Type3) -> Filtered Subsets by (Type2, Type3)
12. Filtered Subsets by (Type2, Type3) -> Model Type4 per path
13. Model Type2 -> Results Summary
14. Model Type3 per branch -> Results Summary
15. Model Type4 per path -> Results Summary

### Data elements (for report table)
1. Shared `df` and `df["text"]`
2. Shared TF-IDF feature matrix `X`
3. Root predictions/labels for Type2
4. Type2 branch index sets
5. (Type2, Type3) path index sets
6. Branch/path metrics and warnings
7. Final hierarchical summary object

### Why this design is strong
- Better alignment with dependency logic between labels.
- Enables branch-level diagnostics.
- Enables path-level warnings for sparse routes.

### Known limitation
- More moving parts and higher implementation complexity.
- Sparse branches may need skip/protection rules.

## Comparison for CA write-up

### Choice 1 is best when
- You need fast, controlled comparison with minimal architecture complexity.
- You want a clean baseline for rubric and reproducible metrics.

### Choice 2 is best when
- You want route-aware behaviour and branch/path diagnostics.
- You want to reflect dependency structure between labels.

### Recommended submission narrative
1. Present Choice 1 as mandatory full implementation and baseline.
2. Present Choice 2 as architecture extension with hierarchical routing logic.
3. Compare maintainability, complexity, and interpretability trade-offs.

## Choice 2 submission stance

For this submission, Choice 2 should be written as design-complete and partially implemented.

What is implemented:
- hierarchical split/routing structure
- branch/path grouping logic
- warning and summary generation for sparse routes

What is not fully implemented yet:
- fully specialised Type3 models trained per Type2 branch
- fully specialised Type4 models trained per (Type2, Type3) path

Use transparent wording in the report to avoid over-claiming while still presenting the architectural comparison clearly.

## Quick mapping to CA steps 3-8

### Choice 1
- Components: listed under Choice 1 components section
- Connectors: listed under Choice 1 connectors section
- Data elements: listed under Choice 1 data elements section

### Choice 2
- Components: listed under Choice 2 components section
- Connectors: listed under Choice 2 connectors section
- Data elements: listed under Choice 2 data elements section

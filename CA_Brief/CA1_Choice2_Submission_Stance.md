# CA1 Choice 2 Submission Stance

## Selected stance for report
Design + partial implementation.

## Exact wording to include in report
For Design Choice 2 (Hierarchical Modelling), we completed the architecture design and a working hierarchical scaffold implementation.

The implemented system includes:
- root-stage Type2 training and evaluation
- Type2 branch split logic
- (Type2, Type3) path split logic
- hierarchical summary generation
- branch/path warnings for sparse or empty routes

The current implementation does not yet train fully specialised downstream models per branch/path with separate fitted model instances for each branch at Type3 and each path at Type4.

Therefore, in this submission, Design Choice 2 is presented as design-complete and partially implemented, while Design Choice 1 is the fully completed, fully reproducible mandatory implementation.

## Why this is acceptable for current write-up
- It is transparent and avoids over-claiming.
- It aligns with the code that is currently in the repository.
- It still provides a clear architectural comparison discussion between chained labels and hierarchical routing.

## File reference for implementation status
- EEAI/src/architectures/choice2_hierarchical.py

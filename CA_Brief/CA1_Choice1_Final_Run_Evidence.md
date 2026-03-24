# CA1 Choice 1 Final Reproducible Run Evidence

## Scope
This evidence covers the mandatory completed implementation for Design Choice 1 (Chained Multi-Outputs).

## Reproducible commands used
Run from project root `EEAI`.

1. AppGallery with RandomForest:
`python main.py --arch choice1 --model rf --data data/AppGallery.csv --export reports/choice1_appgallery_rf.csv`

2. Purchasing with RandomForest:
`python main.py --arch choice1 --model rf --data data/Purchasing.csv --export reports/choice1_purchasing_rf.csv`

3. AppGallery with LogisticRegression:
`python main.py --arch choice1 --model lr --data data/AppGallery.csv --export reports/choice1_appgallery_lr.csv`

4. Purchasing with LogisticRegression:
`python main.py --arch choice1 --model lr --data data/Purchasing.csv --export reports/choice1_purchasing_lr.csv`

## Final metrics table (RandomForest)

### AppGallery (reports/choice1_appgallery_rf.csv)
| Task | Accuracy | F1 Macro |
|---|---:|---:|
| type2 | 0.8400 | 0.8631 |
| type23 | 0.6400 | 0.4919 |
| type234 | 0.5600 | 0.3205 |

### Purchasing (reports/choice1_purchasing_rf.csv)
| Task | Accuracy | F1 Macro |
|---|---:|---:|
| type2 | 0.8824 | 0.5762 |
| type23 | 0.7647 | 0.5475 |
| type234 | 0.6471 | 0.4524 |

## Additional comparison table (LogisticRegression)

### AppGallery (reports/choice1_appgallery_lr.csv)
| Task | Accuracy | F1 Macro |
|---|---:|---:|
| type2 | 0.7600 | 0.6955 |
| type23 | 0.6400 | 0.4848 |
| type234 | 0.6000 | 0.3492 |

### Purchasing (reports/choice1_purchasing_lr.csv)
| Task | Accuracy | F1 Macro |
|---|---:|---:|
| type2 | 0.8824 | 0.5762 |
| type23 | 0.7647 | 0.5267 |
| type234 | 0.6471 | 0.4212 |

## Interpretation for report
- As label complexity increases (type2 -> type23 -> type234), performance generally decreases.
- This trend is expected and supports the Design Choice 1 objective.
- The same feature pipeline and split setup were reused, so the comparison remains controlled.

## Note on console line "Using CSV"
`config.py` prints a default path on import. When running with `--data`, the actual dataset used is the one passed in the command, and the exported CSV files above are the source of truth for final reported metrics.

# EEAI

## Quick Run

Use the controller directly with an explicit dataset path when running locally:

python -c "from pathlib import Path; from controller import run_architecture; print(run_architecture('choice1', model_name='rf', data_path=Path('data/AppGallery.csv')))"

Metric note: `accuracy` is exact match ratio for the target label set and `f1_macro` balances class-level performance in imbalanced cases.

Export example:

python main.py --arch choice1 --model rf --export reports/choice1_appgallery_rf.csv

CLI examples with explicit data path:

python main.py --arch choice1 --model rf --data data/AppGallery.csv
python main.py --arch choice2 --model rf --data data/AppGallery.csv
python main.py --arch choice1 --model lr --data data/Purchasing.csv --export reports/choice1_purchasing_lr.csv

Reporting note: exported CSV files are ready to paste into CA report tables after a quick formatting pass.

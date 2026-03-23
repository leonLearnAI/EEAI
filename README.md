# EEAI

## Quick Run

Use the controller directly with an explicit dataset path when running locally:

python -c "from pathlib import Path; from controller import run_architecture; print(run_architecture('choice1', model_name='rf', data_path=Path('data/AppGallery.csv')))"

Metric note: `accuracy` is exact match ratio for the target label set and `f1_macro` balances class-level performance in imbalanced cases.

Export example:

python main.py --arch choice1 --model rf --export reports/choice1_appgallery_rf.csv

Reporting note: exported CSV files are ready to paste into CA report tables after a quick formatting pass.

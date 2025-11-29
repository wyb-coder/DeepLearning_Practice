Cleanup after training

This repository includes a helper script to archive and remove training artifacts that are not needed for inference.

What it does

- Archive `results/model` and `results/results` (if present) into a timestamped `results_backup_YYYYMMDD_HHMMSS.tar.gz` in the repository root.
- Remove `results/model`, `results/results`, and `model/temp_best_model.pth`.

Why

After you export the lightweight inference weights (`model/best_model_Fold*.pth`), the full training artifacts (optimizer states, scalers, logs) under `results/` are not required for prediction. This script safely archives them before deletion so you can restore if needed.

How to run (on the Linux server)

Interactive:

```bash
cd /path/to/your/repo
bash scripts/cleanup_after_train.sh
```

Non-interactive (no confirmation):

```bash
bash scripts/cleanup_after_train.sh --yes
```

Dry-run (show what would be removed):

```bash
bash scripts/cleanup_after_train.sh --dry-run
```

Restore

Extract the created tarball:

```bash
tar -xzf results_backup_YYYYMMDD_HHMMSS.tar.gz
```

Notes

- This script is designed for Linux environments (bash). Do not run on Windows without modification.
- The script makes no backup of single files (like `model/temp_best_model.pth`) other than the optional tarball of directories. If you want separate backups, copy them before running.

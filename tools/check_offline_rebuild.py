import datetime
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

from validate import ROOT, file_list


def main():
    files = file_list()
    with tempfile.TemporaryDirectory(prefix="ai_combustion_offline_") as directory:
        target = pathlib.Path(directory)
        for name in files:
            destination = target / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, destination)
        for script in ["tools/build_catalog.py", "tools/build_overview.py", "tools/build_open_work_index.py", "tools/build_reproduction_queue.py"]:
            subprocess.run([sys.executable, script], cwd=target, check=True, stdout=subprocess.DEVNULL)
        differences = [name for name in files if (ROOT / name).read_bytes() != (target / name).read_bytes()]
        report = {"status": "passed" if not differences else "failed", "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "files_compared": len(files), "scope": "Copy only Git-listed distributable files to temporary directory without ignored discovery/readme/license caches; rebuild catalog and overview; compare all original file bytes. No network, model training or original-paper verification.", "differences": differences}
    (ROOT / "evidence/offline_rebuild.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if differences:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

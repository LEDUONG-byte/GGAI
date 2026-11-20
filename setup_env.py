"""setup_env.py —— Automated Environment Setup (Python + Frida + ADB + Emulator Connection)

Tasks performed:
  1. Verify Python version (3.10+ recommended)
  2. Install / verify Frida 16.5.9 (required for script injection; Frida 17.x removed Java bridge)
  3. Detect ADB: Environment variable -> PATH -> Emulator bundled ADB -> Auto-download platform-tools
  4. Connect to device / emulator and run self-test via `python ultra0.py --check`

Usage: Double-click `0_SETUP_ENVIRONMENT.bat`, or run `python setup_env.py`
"""
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

BASE = Path(__file__).resolve().parent
ADB_CANDIDATES = [
    os.environ.get("ADB_PATH", ""),
    r"C:\Program Files\Netease\MuMuPlayer-12.0\shell\adb.exe",
    r"C:\Program Files\Netease\MuMuPlayerGlobal-12.0\shell\adb.exe",
    r"C:\Program Files (x86)\Netease\MuMuPlayer-12.0\shell\adb.exe",
    r"D:\Program Files\Netease\MuMu\nx_main\adb.exe",
    r"D:\Program Files\Netease\MuMu\nx_device\12.0\shell\adb.exe",
    r"C:\Program Files\Netease\MuMu\nx_main\adb.exe",
    os.path.expandvars(r"%LOCALAPPDATA%\Android\Sdk\platform-tools\adb.exe"),
    os.path.expandvars(r"%USERPROFILE%\AppData\Local\Android\Sdk\platform-tools\adb.exe"),
]
PLATFORM_TOOLS_URL = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip"


def step(msg):
    print(f"\n▶ {msg}", flush=True)


def ok(msg):
    print(f"   ✅ {msg}", flush=True)


def warn(msg):
    print(f"   ⚠️  {msg}", flush=True)


def die(msg):
    print(f"\n❌ {msg}", flush=True)
    sys.exit(1)


def check_python():
    step("Checking Python Environment")
    v = sys.version_info
    print(f"   {platform.python_version()}  ({platform.architecture()[0]})")
    if v < (3, 9):
        die("Python version is too low. Please install Python 3.10 or higher: https://www.python.org/downloads/")
    ok("Python environment is compatible")


def install_frida():
    step("Verifying / Installing Frida 16.5.9")
    try:
        import frida
        if frida.__version__.startswith("16."):
            ok(f"Frida {frida.__version__} is already installed")
            return
        warn(f"Detected Frida {frida.__version__}. Frida 17+ is unsupported; downgrading to 16.5.9…")
    except Exception:
        pass

    cmds = [
        [sys.executable, "-m", "pip", "install", "--no-cache-dir", "frida==16.5.9"],
        [sys.executable, "-m", "pip", "install", "--no-cache-dir",
         "-i", "https://pypi.tuna.tsinghua.edu.cn/simple", "frida==16.5.9"],
    ]
    for c in cmds:
        print("   " + " ".join(c[2:]))
        r = subprocess.run(c, capture_output=True, text=True, errors="ignore")
        if r.returncode == 0:
            break
        print("   " + (r.stderr or r.stdout).strip().splitlines()[-1][:160])
    try:
        import importlib
        import frida
        importlib.reload(frida)
        ok(f"Frida {frida.__version__} successfully installed")
    except Exception as e:
        die(f"Failed to install Frida: {e}\n   Run manually: pip install frida==16.5.9")


def download_platform_tools():
    dest = BASE / "platform-tools"
    print(f"   Downloading platform-tools to {dest}")
    tmp = Path(tempfile.gettempdir()) / "platform-tools.zip"
    with urllib.request.urlopen(PLATFORM_TOOLS_URL, timeout=180) as r, open(tmp, "wb") as f:
        f.write(r.read())
    with zipfile.ZipFile(tmp) as z:
        z.extractall(BASE)
    tmp.unlink(missing_ok=True)
    adb = dest / "adb.exe"
    if adb.exists():
        ok(f"platform-tools is ready: {adb}")
        return str(adb)
    die("platform-tools extracted but adb.exe was not found")


def find_adb():
    step("Locating Android Debug Bridge (ADB)")
    for c in ADB_CANDIDATES:
        if not c:
            continue
        if c in ("adb", "adb.exe"):
            continue
        if Path(c).exists():
            ok(f"Found ADB: {c}")
            return c
    w = shutil.which("adb")
    if w:
        ok(f"Found ADB in PATH: {w}")
        return w
    warn("ADB not found locally. Initiating automated download...")
    return download_platform_tools()


def connect_emulator(adb):
    step("Connecting to Android Emulator / Device")
    ports = ["16384", "7555", "16416", "21503", "62001"]
    for p in ports:
        subprocess.run([adb, "connect", f"127.0.0.1:{p}"], capture_output=True, text=True, errors="ignore")
    out = subprocess.run([adb, "devices"], capture_output=True, text=True, errors="ignore").stdout
    devices = [l.split("\t")[0] for l in out.splitlines()[1:] if "\tdevice" in l]
    if not devices:
        warn("No connected device detected. Ensure emulator has USB/ADB debugging enabled in Settings.")
        print("   " + out.strip().replace("\n", "\n   "))
        return None
    ok(f"Connected devices: {', '.join(devices)}")
    return devices[0]


def run_check(adb, serial):
    step("Executing Environment Diagnostics (`python ultra0.py --check`)")
    env = dict(os.environ)
    env["ADB_PATH"] = adb
    env["PYTHONIOENCODING"] = "utf-8"
    r = subprocess.run([sys.executable, "ultra0.py", "--check"], cwd=str(BASE),
                       env=env, capture_output=True, encoding="utf-8", errors="ignore")
    print(r.stdout.strip() or r.stderr.strip())
    return r.returncode == 0


def main():
    print("=" * 60)
    print("  Google AI Pro (5 TB) 1-Click Environment Setup")
    print("=" * 60)
    check_python()
    install_frida()
    adb = find_adb()
    serial = connect_emulator(adb)

    if serial:
        good = run_check(adb, serial)
        print("\n" + "=" * 60)
        if good:
            print("  ✅ Environment is fully ready! Launch «1_AUTO_STACK_24_MONTHS.bat» to start.")
        else:
            print("  ⚠️  Self-test failed on some checks. Review the diagnostic output above.")
        print("=" * 60)
    else:
        print("\nPlease start your Android emulator/device with USB debugging enabled, then re-run this setup.")


if __name__ == "__main__":
    main()

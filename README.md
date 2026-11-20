# Google AI Pro 5TB Stacking Suite (2026–2028)

An enterprise-grade, automated toolchain to activate and stack up to **24 Months** of **Google AI Pro (5 TB Cloud Storage + Gemini Advanced)** at **$0 Zero Cost** via dynamic Android instrumentation (`Frida`) and Google Play Billing proration stacking.

---

## 📌 Overview & Stacking Mechanism

Google One offers trial periods for selected plans (`g1.2tb.ai.subs_variant`) that are returned dynamically through the Google Play Billing Library (`BillingClient`).

By leveraging Google Play's native subscription upgrade proration mode (`ProrationMode.CHARGE_FULL_PRICE` / `TIME_PRORATION`), this suite sequentially chains trial periods together:

```
[ Step 1: Base Activation ]  ──►  12 Months Free Trial (Expires 2027)
            │
            ▼
[ Step 2: First Stack ]      ──►  +6 Months Proration Conversion (Total: 18 Months)
            │
            ▼
[ Step 3: Second Stack ]     ──►  +6 Months Proration Conversion (Total: 24 Months / Expires 2028)
```

> **100% Zero-Cost Guarantee**: The instrumentation engine strictly verifies the checkout sheet for $0 charge (`₫0`, `$0`, or free trial proration) before confirming. If any non-zero charge is detected, the transaction is immediately aborted.

---

## 📁 Scientific Project Structure

```
ggai.pro.5tb.2028/
├── 🚀 1_AUTO_STACK_24_MONTHS.bat        # [MAIN] One-click automated 24-month stacking workflow
├── 🔍 2_CHECK_SUBSCRIPTION_STATUS.bat   # Inspect active subscription, expiration date & remaining days
├── ⚙️ 0_SETUP_ENVIRONMENT.bat           # Environment verification, Python & Frida diagnostics
│
├── 📁 manual_steps/                     # Granular standalone steps for manual execution
│   ├── 1_Check_Device_Connection.bat    # Verify ADB & root connectivity
│   ├── 2_List_Available_Offers.bat      # Safe read-only inspection of available offers
│   ├── 3_Step_1_Activate_12_Months.bat  # Base activation (12 months free trial)
│   ├── 4_Step_2_Stack_18_Months.bat     # Stack #1: Upgrade to 18 months
│   ├── 5_Step_3_Stack_24_Months.bat     # Stack #2: Upgrade to 24 months
│   └── 6_Step_4_Samsung_Backup.bat      # Fallback offer (Samsung-exclusive tier)
│
├── 📁 reports/                          # JSON execution logs and audit records
├── 📄 HOW_TO_USE.md                     # Comprehensive operational and troubleshooting guide
├── 📄 README.md                         # Project documentation and architecture
├── 🐍 ultra0.py                         # Core billing automation and Frida injection engine
├── 🐍 setup_env.py                      # Automated diagnostic and environment provisioner
└── 🐍 query_sku.py                      # Billing offer query utility
```

---

## 💻 System Prerequisites

1. **Host PC**:
   - Windows 10/11 or macOS/Linux.
   - Python 3.9+ with `frida` (`pip install frida`).
   - Android SDK Platform-Tools (`adb`).

2. **Target Device**:
   - A rooted Android device or Android Emulator (MuMu Player 12, LDPlayer 9, or Android Studio AVD).
   - USB Debugging enabled in Developer Options.
   - Google Play Store installed and logged in with your target Google account.
   - Valid payment method attached to Google Play (Credit/Debit Card, MoMo, PayPal, etc.). *No charges will occur.*

---

## 🚀 Quick Start Guide

### Step 0: Prepare Your Device
Ensure your rooted emulator or phone is running and connected via ADB:
```bash
adb devices
```

### Step 1: Environment Diagnostic
Double-click `0_SETUP_ENVIRONMENT.bat` or run:
```bash
python setup_env.py
```
This script validates ADB connectivity, root permissions, `frida-server` deployment, and disables restrictive proxies.

### Step 2: Run 24-Month Automated Stacking
Double-click `1_AUTO_STACK_24_MONTHS.bat` or run:
```bash
python ultra0.py --auto-stack
```
- **Password Prompt**: If Google Play asks for your password during the initial activation, enter it on the device screen, check **"Remember me on this device"**, and click **Verify**.
- The script automatically performs Step 1 (12M) $\to$ Step 2 (18M) $\to$ Step 3 (24M).

### Step 3: Check Subscription Validity
Double-click `2_CHECK_SUBSCRIPTION_STATUS.bat` or run:
```bash
python ultra0.py --status
```
Example Output:
```
============================================================
        GOOGLE ONE / GOOGLE AI SUBSCRIPTION INFO
============================================================
  Account         : user@gmail.com
  Plan Name       : Google AI Pro (5 TB) (g1.2tb.ai.subs_variant)
  Status          : ✅ ACTIVE | Auto-Renew: ON
  Expiration Date : 20/11/2028 14:05:59
  Remaining Time  : 730 days (~24.0 months)
  Order ID        : SOP.3301-xxxx-xxxx-xxxxx
============================================================
```

---

## 🛠️ CLI Reference

`ultra0.py` supports advanced granular flags:

| Flag | Description |
|---|---|
| `--check` | Run environment diagnostics only |
| `--status` | Display current plan expiration and remaining duration |
| `--auto-stack` | Automatically execute 12M $\to$ 18M $\to$ 24M chain |
| `--list` | Read-only inspection of available offers and purchaseTokens |
| `--plan <tier>` | Target plan (`auto`, `pro12`, `pro6`, `pro6b`, `pro6c`, `5x`, `20x`) |
| `--stack` | Upgrade existing subscription using current `purchaseToken` |
| `--mode <id>` | Replacement mode (`1`=TIME_PRORATION, `5`=CHARGE_FULL_PRICE) |
| `--force` | Skip Play Store account name check |
| `--serial <sn>` | Specify target device ADB serial number |

---

## 🛡️ Subscription Management & Cancellation

- **During the Stacking Process**: Do **NOT** cancel the subscription. Stacking requires an **Active** subscription on Google Play to perform proration upgrades.
- **After Reaching 24 Months**:
  You may cancel auto-renewal at any time via:
  > **Google Play Store $\to$ Profile Icon $\to$ Payments & Subscriptions $\to$ Subscriptions $\to$ Cancel Subscription**
  
  *Canceling auto-renewal preserves the full 24-month validity period until November 2028 without any risk of recurring charges.*

---

## 🔒 Security & Privacy

- All operations execute 100% locally on your machine.
- No credentials, tokens, or payment details are transmitted to external servers.
- Audit logs are saved locally to `reports/`.

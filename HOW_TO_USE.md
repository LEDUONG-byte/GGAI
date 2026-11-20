# USER GUIDE: Automated Google AI Pro (5 TB) 24-Month Stacking

---

## 1. Overview & Proration Stacking Principle
This suite activates and stacks Google AI Pro (5 TB Google Drive storage + Gemini Advanced) for up to 24 months at $0 cost using Google Play's native subscription upgrade proration mechanism:
- **Step 1**: Activate 12-Month Base Free Trial (Expires ~May 2027).
- **Step 2**: Upgrade & Stack +6 Months (Extends to ~18 Months).
- **Step 3**: Upgrade & Stack +6 Months (Extends to ~24 Months / November 2028).
- **Step 4 (Backup)**: Samsung-exclusive 6-month trial tier (if needed).

---

## 2. Directory Structure

```
ggai.pro.5tb.2028/
├── 🚀 1_AUTO_STACK_24_MONTHS.bat        --> [PRIMARY] Double-click to auto-stack to 24 months
├── 🔍 2_CHECK_SUBSCRIPTION_STATUS.bat   --> Check expiration date and remaining days
├── ⚙️ 0_SETUP_ENVIRONMENT.bat           --> Automatic setup of Python, Frida & ADB diagnostics
│
├── 📁 manual_steps/                     --> Granular steps for manual execution
│     ├── 1_Check_Device_Connection.bat
│     ├── 2_List_Available_Offers.bat
│     ├── 3_Step_1_Activate_12_Months.bat
│     ├── 4_Step_2_Stack_18_Months.bat
│     ├── 5_Step_3_Stack_24_Months.bat
│     └── 6_Step_4_Samsung_Backup.bat
│
├── 📁 reports/                          --> Output logs and audit records for each account
├── 📄 HOW_TO_USE.md                     --> This documentation guide
├── 📄 README.md                         --> Technical architecture and command references
└── 🐍 ultra0.py                         # Frida instrumentation & Google Play Billing engine
```

---

## 3. Quick Start (Recommended)

### Step 0: Prepare Device
- Launch your rooted Android emulator (MuMu Player 12 / LDPlayer 9) or connect a rooted Android phone.
- Ensure your Google account is signed into Google Play Store and has a valid payment method attached (Bank Card, MoMo, PayPal, etc.). No charges will be incurred.

### Step 1: Environment Diagnostic
- Double-click:
  👉 `0_SETUP_ENVIRONMENT.bat`
- Confirm all checks display green checkmarks.

### Step 2: Automated 24-Month Execution
- Double-click:
  👉 `1_AUTO_STACK_24_MONTHS.bat`
- The automation engine will handle the sequential workflow:
  - If Google Play prompts for your account password on first launch, type your password on the device screen, check **"Remember me on this device"**, and click **Verify**.
  - The script will automatically link Step 1 (12M) -> Step 2 (18M) -> Step 3 (24M).

### Step 3: Verify Subscription Status
- Double-click:
  👉 `2_CHECK_SUBSCRIPTION_STATUS.bat`
- Verify that your subscription status displays:
  ```
  Status          : ✅ ACTIVE | Auto-Renew: ON
  Expiration Date : 20/11/2028
  Remaining Time  : 730 days (~24.0 months)
  ```

---

## 4. Manual Step-by-Step Execution (Optional)
If you prefer running individual steps manually, navigate to `manual_steps/`:
1. Run `1_Check_Device_Connection.bat`: Ensure environment and root connection are ready.
2. Run `2_List_Available_Offers.bat`: Safely query available billing offers without opening checkout.
3. Run `3_Step_1_Activate_12_Months.bat`: Activate the initial 12-month base trial.
4. Run `4_Step_2_Stack_18_Months.bat`: Stack the first +6 months (reaching 18 months).
5. Run `5_Step_3_Stack_24_Months.bat`: Stack the second +6 months (reaching 24 months).

---

## 5. Important Guidelines Regarding Subscription Cancellation
- **During the Stacking Process**: **DO NOT** cancel the subscription. Google Play requires an active subscription to perform proration upgrades.
- **After Stacking 24 Months**: You can cancel auto-renewal at any time in Google Play Store (`Play Store -> Profile -> Payments & Subscriptions -> Subscriptions -> Cancel Subscription`).
- **Proration Guarantee**: Canceling auto-renewal does **NOT** revoke your time. You will retain the full 24 months of Google AI Pro (5 TB) until November 2028!

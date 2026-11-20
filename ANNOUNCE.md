# Release Announcement

> Google AI Ultra / Pro 5TB ($0 Free Trial for 24 Months).
>
> **Core Principle**: Google One provides hidden trial offers inside the Google Play Billing Library (`BillingClient`). This project hooks the official Google One process via dynamic binary instrumentation (Frida), queries the billing offers, launches the Google Play native payment sheet, verifies $0 zero-cost billing, and executes subscription proration upgrades to stack up to 24 months.
>
> 5TB Google Drive Cloud Storage + Gemini Advanced Pro. Free of charge when canceled before the trial period expires.
>
> ### Requirements
> - Rooted Android device or Android Emulator (MuMu Player, LDPlayer, Android Studio Emulator).
> - USB cable with ADB debugging enabled.
> - Python 3.9+ with `frida` installed.
>
> ### Quick Start
> 1. Run `0_SETUP_ENVIRONMENT.bat` to verify environment and install dependencies.
> 2. Run `1_AUTO_STACK_24_MONTHS.bat` to automatically execute the full 24-month stacking chain.
> 3. Run `2_CHECK_SUBSCRIPTION_STATUS.bat` to verify expiration date and active status.

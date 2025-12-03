# 🕵️ DarkWeb Persona Generator (DB-less)

A lightweight, procedural identity generator written in Python. This tool creates unique, consistent, and anonymous personas without relying on any external databases or wordlists. It uses algorithmic patterns to synthesize pronounceable names, addresses, and valid formatted data on the fly.

> **Note:** Designed for generating mock data, testing environments, and anonymous identification placeholders.

---

## ✨ Key Features

1.  **Database-Free**: Zero external dependencies or static files (JSON/CSV/SQL). Everything is generated algorithmically.

2.  **Procedural Names**: Uses a Consonant-Vowel switching algorithm to create fake but pronounceable names (e.g., "Vaxole", "Zunira").

3.  **Dual-Mode Aliases**:
    * **0x Style**: Generates a hex-like identifier using a procedural word converted into **ASCII-only Leetspeak** prefixed with `0x` (e.g., `0xV4X0L3`, `0xH1r1|Ay`).
    * **Emoticon Style**: Outputs a standalone random ASCII emoticon / Kaomoji for pure anonymity (e.g., `(o_O)`, `¯\_(ツ)_/¯`).

4.  **Valid Syntax Credit Cards**: Generates 16-digit credit card numbers that pass the Luhn Algorithm (Mod 10) check, formatted with hyphens for better readability (e.g., xxxx-xxxx-xxxx-xxxx).

5.  **Context-Aware Emails**: Generates email addresses that match the generated user's name.

6.  **Full Identity Suite**: Includes UUID, Phone (w/ Country Code), Address, Company, and internal IDs.

---

## 🛠️ Prerequisites

* Python 3.x
* Standard Libraries only (`uuid`, `random`, `string`) - No pip install required.

---

## 🚀 Usage

Clone this repository or download the script.

Run the script directly from your terminal.

```sh
# Linux / macOS
python3 id_gen.py

# Windows
py id_gen.py
````

### EXAMPLE OUTPUT

```sh
==================== GENERATED IDENTITY ====================
Internal_ID     : 20681
UUID            : dbffb2e4-e9d2-48d2-8d9a-8a540ca037af
Alias           : 0xH1r1|Ay
Real_Name       : Lapik Ahobex
Email           : lapik.ahobex@tutanota.com
Phone           : +97-419-117-7087
Address         : 6378 Zebuja Ave, Wedodimu City, 14796
Company         : Cozonipu Corp
Credit_Card     : 4959-3420-5625-0553
============================================================
```

-----

## 📝 Todo List

  * [ ] **Real-world Geodata Integration**: Replace procedural generation with fetching real city, state, and zip codes.
  * [ ] **PGP Encryption Suite**: Add features to generate PGP keys and configure a corresponding secure email identity.
    > **Tip**: For temporary email services, we recommend [Mail.tm](https://mail.tm/en/). For secure anonymous mail, [Proton Mail](https://proton.me/mail) is recommended.
  * [ ] **Binary Compilation**: Provide build options to compile the script into standalone binaries for easier CLI usage (ELF64 for Linux, Batch scripts for Windows, Mach-O for macOS).
  * [ ] **Integrity Verification**: Auto-generate a `checksum.txt` file for output validation.
  * [ ] **Realistic Name API**: Integrate with public APIs to fetch real-world names, replacing the current phoneme-based synthesis for higher realism.
  * [ ] **Country-Code Based Location**: Implement logic to generate random locations corresponding to the generated phone country code directly within Python.

### ⛔ Cancelled / Deprecated

  * [ ] ~~Mastercard Specific Algorithm~~
    ```diff
    - Cancelled as distinguishing card types is meaningless in this context. No further development planned for specific card issuer algorithms.
    ```
  * [ ] ~~SSH Key Generation~~
    ```diff
    - Will skip this implementation due to out of focus.
    ```

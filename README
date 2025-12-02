# 🕵️ DarkWeb Persona Generator (DB-less)

A lightweight, procedural identity generator written in Python. This tool creates unique, consistent, and anonymous personas without relying on any external databases or wordlists. It uses algorithmic patterns to synthesize pronounceable names, addresses, and valid formatted data on the fly.

> **Note:** Designed for generating mock data, testing environments, and anonymous identification placeholders.

## ✨ Key Features

* **Database-Free:** Zero external dependencies or static files (JSON/CSV/SQL). Everything is generated algorithmically.

* **Procedural Names:** Uses a Consonant-Vowel switching algorithm to create fake but pronounceable names (e.g., "Vaxole", "Zunira").

* **Leetspeak Aliases:** Automatically converts generated names into hacker-style aliases (e.g., `V4X0L3_0x99`).

* **Valid Syntax Credit Cards:** Generates 16-digit credit card numbers that pass the **Luhn Algorithm** (Mod 10) check (Syntactically valid, not financially active).

* **Context-Aware Emails:** Generates email addresses that match the generated user's name.

* **Full Identity Suite:** Includes UUID, Phone (w/ Country Code), Address, Company, and internal IDs.


## 🛠️ Prerequisites

* Python 3.x
* Standard Libraries only (`uuid`, `random`, `string`) - **No `pip install` required.**

## 🚀 Usage

1.  Clone this repository or download the script.
2.  Run the script directly from your terminal.

```bash
#sh
python3 id_gen.py

#window
py id_gen.py
```

---

## EXAMPLE OUTPUT

```sh
PS> py .\id_gen.py
==================== GENERATED IDENTITY ====================
Internal_ID     : 57180
UUID            : d61c4420-3272-4c38-afb6-0282c94b2d82
Alias           : 353X4DUD32U_0x79
Real_Name       : Esexad Udezu
Email           : esexadudezu@mail.onion
Phone           : +21-651-564-1944
Address         : 4510 Zuvixuti Ave, Avumixaq City, 28141
Company         : Gidit Solutions
Credit_Card     : 4792226702710160
============================================================
```

## 📝 Todo List / Roadmap

- [ ] **Real-world Geodata Integration:** Replace procedural generation with fetching real city, state, and zip codes.

- [ ] **Mastercard Specific Algorithm:** Refine the credit card generation logic to strictly target Mastercard standards (IIN ranges and validation).

- [ ] **SSH Key Generation:** Implement functionality to generate valid SSH key pairs automatically.

- [ ] **PGP Encryption Suite:** Add features to generate PGP keys and configure a corresponding secure email identity.

- [ ] **Binary Compilation:** Provide build options to compile the script into standalone binaries for easier CLI usage (ELF64 for Linux, Batch scripts for Windows, Mach-O for macOS).

- [ ] **Integrity Verification:** Auto-generate a `checksum.txt` file for output validation.

- [ ] **Realistic Name API:** Integrate with public APIs to fetch real-world names, replacing the current phoneme-based synthesis for higher realism.
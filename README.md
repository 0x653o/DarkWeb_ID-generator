🕵️ DarkWeb Persona Generator (DB-less)

A lightweight, procedural identity generator written in Python. This tool creates unique, consistent, and anonymous personas without relying on any external databases or wordlists. It uses algorithmic patterns to synthesize pronounceable names, addresses, and valid formatted data on the fly.

Note: Designed for generating mock data, testing environments, and anonymous identification placeholders.

✨ Key Features

Database-Free: Zero external dependencies or static files (JSON/CSV/SQL). Everything is generated algorithmically.

Procedural Names: Uses a Consonant-Vowel switching algorithm to create fake but pronounceable names (e.g., "Vaxole", "Zunira").

Polymorphic Aliases & Kaomoji: Generates hacker-style aliases using advanced 1:N Leetspeak mapping (e.g., A → 4, @, /-\) combined with random ASCII emoticons (e.g., (o_O), >_<) or hex prefixes.

Valid Syntax Credit Cards: Generates 16-digit credit card numbers that pass the Luhn Algorithm (Mod 10) check, formatted with hyphens for better readability (e.g., xxxx-xxxx-xxxx-xxxx).

Context-Aware Emails: Generates email addresses that match the generated user's name.

Full Identity Suite: Includes UUID, Phone (w/ Country Code), Address, Company, and internal IDs.

🛠️ Prerequisites

Python 3.x

Standard Libraries only (uuid, random, string) - No pip install required.

🚀 Usage

Clone this repository or download the script.

Run the script directly from your terminal.

```sh
# sh
python3 dark_identity_generator.py

# window
py dark_identity_generator.py
```


EXAMPLE OUTPUT
```sh
==================== GENERATED IDENTITY ====================
Internal_ID     : 48291
UUID            : a1b2c3d4-e5f6-7890-1234-567890abcdef
Alias           : (o_O)_V4X0L3
Real_Name       : Vaxole Zunira
Email           : vaxole_zunira88@proton.me
Phone           : +82-123-456-7890
Address         : 1234 Mokagi Ln, Zunira City, 54321
Company         : Vaxole Systems
Credit_Card     : 4532-1234-5678-9010
============================================================
```


📝 Todo List

[ ] Real-world Geodata Integration: Replace procedural generation with fetching real city, state, and zip codes.

[ ] Mastercard Specific Algorithm: Refine the credit card generation logic to strictly target Mastercard standards (IIN ranges and validation).

[ ] ~~SSH Key Generation: Implement functionality to generate valid SSH key pairs automatically.~~
```diff
- Will skip this implementation due to the inability to communicate with generated emails and no intent to collect user data.
```


[ ] ~~PGP Encryption Suite: Add features to generate PGP keys and configure a corresponding secure email identity.~~

```diff
- Will skip this implementation due to the inability to communicate with generated emails and no intent to collect user data.
```


[ ] Binary Compilation: Provide build options to compile the script into standalone binaries for easier CLI usage (ELF64 for Linux, Batch scripts for Windows, Mach-O for macOS).

[ ] Integrity Verification: Auto-generate a checksum.txt file for output validation.

[ ] Realistic Name API: Integrate with public APIs to fetch real-world names, replacing the current phoneme-based synthesis for higher realism.
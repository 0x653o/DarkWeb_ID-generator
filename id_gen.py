import uuid
import random
import string

class DarkIdentityGenerator:
    def __init__(self):
        # 1. Leetspeak mapping (100% ASCII Only) - As provided
        self.leet_map = {
            'a': ['4', '@', 'a', 'A'],
            'b': ['b', 'B'],
            'c': ['<', 'c', 'C'],
            'd': ['d', 'D'],
            'e': ['3', 'e', 'E'],
            'g': ['9', 'g', 'G'],
            'h': ['4', 'h', 'H'],
            'i': ['1', '!', '|', 'i', 'I'],
            'k': ['k', 'K'],
            'l': ['1', '|', 'l', 'L'],
            'm': ['^^', 'm', 'M'],
            'n': ['n', 'N'],
            'o': ['0', '*', 'o', 'O'],
            'p': ['p', 'P'],
            's': ['5', '$', 's', 'S'],
            't': ['7', '+', 't', 'T'],
            'u': ['u', 'U'],
            'v': ['v', 'V'],
            'w': ['vv', 'w', 'W'],
            'x': ['x', 'X'],
            'z': ['z', 'Z']
        }
        
        # ASCII Emoticons / Kaomoji Pool
        self.ascii_emotes = [
            # Basic
            "(o_O)", ">_<", "x_x", ":)", "^.~", "-_-", 
            "T_T", "=.=", "d-_-b", "(^_^)", "o.0", "<3",
            ":P", ":D", ":(", ";)",
            
            # Kaomoji / Complex
            "¯\\_(ツ)_/¯", "(>.<)", "(*_*)", "ಠ_ಠ", "(¬_¬)",
            "(='.'=)", "\\(•◡•)/", "[+_+]", "(;´༎ຶД༎ຶ`)",
            "( ͡° ͜ʖ ͡°)", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)", "༼ つ ◕_◕ ༽つ",
            "(ง'̀-'́)ง", "(kts)", "{._.}", "^o^", "(X_X)",
            "/|\\( ;,;)/|\\", "(~_~;)", "(*^*)", "(T_T)",
            "(=_=)", "(?_?)", "('_')", "(>_>)", "(<_<)"
        ]
        
        # 2. Consonant phonemes and vowels for pronounceable word generation
        self.vowels = "aeiou"
        self.consonants = "".join([c for c in string.ascii_lowercase if c not in self.vowels])
        
        # 3. Other pools for address, company, email generation
        self.street_types = ["St", "Ave", "Ln", "Rd", "Blvd", "Way"]
        self.company_suffixes = ["Corp", "Inc", "Systems", "Solutions", "Labs", "Group"]
        self.email_domains = ["proton.me", "mail.onion", "tutanota.com", "secmail.net", "darkbox.cc", "gmail.com"]

    def _generate_uuid(self):
        return str(uuid.uuid4())

    def _generate_pronounceable_word(self, length=6):
        """Make a pronounceable word by alternating consonants and vowels"""
        word = ""
        is_consonant = random.choice([True, False])
        for _ in range(length):
            if is_consonant:
                char = random.choice(self.consonants)
            else:
                char = random.choice(self.vowels)
            word += char
            is_consonant = not is_consonant
        return word.capitalize()

    def _to_leetspeak(self, text):
        """Transform text using various mappings (ASCII Only)"""
        text = text.lower()
        leet_text = ""
        for char in text:
            if char in self.leet_map:
                leet_text += random.choice(self.leet_map[char])
            else:
                leet_text += char.upper() if random.random() > 0.5 else char
        return leet_text

    def _to_email_leetspeak(self, text):
        """
        Specialized Leetspeak for Emails.
        Restricts characters to alphanumeric to ensure valid email syntax
        while still looking 'hacker-ish'.
        """
        text = text.lower()
        # Only use mappings that are safe for email addresses (no special chars like @, #, etc.)
        safe_map = {
            'a': '4',
            'b': '8',
            'e': '3',
            'g': '9',
            'i': '1',
            'l': '1',
            'o': '0',
            's': '5',
            't': '7',
            'z': '2'
        }
        
        leet_text = ""
        for char in text:
            if char in safe_map:
                # 80% chance to convert to number, 20% keep as letter for readability
                if random.random() > 0.2:
                    leet_text += safe_map[char]
                else:
                    leet_text += char
            else:
                leet_text += char
        return leet_text

    def _generate_phone(self):
        """Random phone number generation"""
        country_code = random.randint(1, 99)
        part1 = random.randint(100, 999)
        part2 = random.randint(100, 999)
        part3 = random.randint(1000, 9999)
        return f"+{country_code}-{part1}-{part2}-{part3}"

    def _luhn_checksum(self, card_number_str):
        """(Luhn Algorithm) Calculate the Luhn checksum digit for a given card number string"""
        digits = [int(d) for d in card_number_str]
        checksum = 0
        is_second = False
        for digit in reversed(digits):
            if is_second:
                digit = digit * 2
                if digit > 9:
                    digit -= 9
            checksum += digit
            is_second = not is_second
        return (checksum * 9) % 10

    def _generate_cc(self):
        """Generate a valid credit card number using Luhn algorithm"""
        prefix = random.choice(['4', '5'])
        body = "".join([str(random.randint(0, 9)) for _ in range(14)])
        temp_num = prefix + body
        check_digit = self._luhn_checksum(temp_num)
        full_number = f"{temp_num}{check_digit}"
        return "-".join([full_number[i:i+4] for i in range(0, len(full_number), 4)])

    def _generate_address(self):
        """Combination of random components"""
        house_num = random.randint(10, 9999)
        street_name = self._generate_pronounceable_word(random.randint(5, 8))
        street_type = random.choice(self.street_types)
        city_name = self._generate_pronounceable_word(random.randint(4, 9))
        zip_code = random.randint(10000, 99999)
        return f"{house_num} {street_name} {street_type}, {city_name} City, {zip_code}"

    def _generate_company(self):
        """Fake company name generation"""
        name = self._generate_pronounceable_word(random.randint(4, 8))
        suffix = random.choice(self.company_suffixes)
        return f"{name} {suffix}"

    def _generate_email(self, first_name, last_name):
        """Email generation using safe leetspeak on the username"""
        sep = random.choice(['.', '_', '-', ''])
        
        # 1. Create base string (e.g. "john_doe")
        base_str = f"{first_name}{sep}{last_name}"
        
        # 2. Apply Safe Leetspeak (e.g. "j0hn_d03")
        email_user = self._to_email_leetspeak(base_str)
        
        # 3. Add random suffix sometimes
        if random.random() > 0.5:
             email_user += str(random.randint(1, 99))

        domain = random.choice(self.email_domains)
        return f"{email_user}@{domain}"

    def create_identity(self):
        # 1. Generate Real Name
        first_name = self._generate_pronounceable_word(random.randint(4, 7))
        last_name = self._generate_pronounceable_word(random.randint(5, 8))
        full_name = f"{first_name} {last_name}"
        
        # 2. Generate Alias (0x LeetStyle vs Emoticon Only)
        # Randomly choose between the two styles
        if random.choice([True, False]):
            # 0x Style: 0x + Leetspeak (ASCII Only)
            random_word = self._generate_pronounceable_word(random.randint(4, 7))
            leet_content = self._to_leetspeak(random_word)
            alias = f"0x{leet_content}"
        else:
            # Emoticon Only Style
            alias = random.choice(self.ascii_emotes)

        return {
            "Internal_ID":  random.randint(1, 99999),
            "UUID":         self._generate_uuid(),
            "Alias":        alias,
            "Real_Name":    full_name,
            "Email":        self._generate_email(first_name, last_name),
            "Phone":        self._generate_phone(),
            "Address":      self._generate_address(),
            "Company":      self._generate_company(),
            "Credit_Card":  self._generate_cc()
        }

if __name__ == "__main__":
    gen = DarkIdentityGenerator()
    print(f"{'='*20} GENERATED IDENTITY {'='*20}")
    identity = gen.create_identity()
    for key, value in identity.items():
        print(f"{key.ljust(15)} : {value}")
    print("="*60)
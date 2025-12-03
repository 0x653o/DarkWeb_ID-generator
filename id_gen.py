import uuid
import random
import string

class DarkIdentityGenerator:
    def __init__(self):
        # 1. Leetspeak 매핑 (ASCII 범위 내에서 더 다양하게 확장)
        # 각 문자에 대해 여러 변환 옵션을 리스트로 제공
        self.leet_map = {
            'a': ['4', '@', '/-\\', '^'],
            'b': ['8', '|3', '13'],
            'c': ['(', '[', '<', '{'],
            'd': ['|)', '|>'],
            'e': ['3', '[-'],
            'g': ['9', '6', 'C-'],
            'h': ['#', '|-|', ')-(', '(-)', '4'],
            'i': ['1', '!', '|', ']['],
            'k': ['|<', '/<', '|{'],
            'l': ['1', '|_', '7', '|'],
            'm': ['/\\/\\', '|v|', '[V]', '^^'],
            'n': ['|\\|', '/\\/', '^/'],
            'o': ['0', '*', '()', '[]', '<>'],
            'p': ['|*', '|o', '|D'],
            's': ['5', '$', 'z', '§'],
            't': ['7', '+', ']['],
            'u': ['|_|', 'v'],
            'v': ['\\/', '|/'],
            'w': ['\\/\\/', 'vv', '\'//'],
            'x': ['%', '><', '}{', '*'],
            'z': ['2', '~/']
        }
        
        # ASCII 이모티콘 풀 (대폭 확장)
        self.ascii_emotes = [
            # Basic
            "(o_O)", ">_<", "x_x", ":)", "^.~", "-_-", 
            "T_T", "=.=", "d-_-b", "(^_^)", "o.0", "<3",
            "S70P", "3RR0R", "NuLL", ":P",
            
            # Kaomoji / Complex
            "¯\_(ツ)_/¯", "(>.<)", "(*_*)", "ಠ_ಠ", "(¬_¬)",
            "(='.'=)", "\\(•◡•)/", "[+_+]", "(;´༎ຶД༎ຶ`)",
            "( ͡° ͜ʖ ͡°)", "ʕ•ᴥ•ʔ", "(▀̿Ĺ̯▀̿ ̿)", "༼ つ ◕_◕ ༽つ",
            "(ง'̀-'́)ง", "(kts)", "{._.}", "^o^", "(X_X)",
            "/|\\( ;,;)/|\\", "(~_~;)", "(*^*)", "(T_T)",
            "(=_=)", "(?_?)", "('_')", "(>_>)", "(<_<)"
        ]
        
        # 2. 음소 풀 (자음/모음)
        self.vowels = "aeiou"
        self.consonants = "".join([c for c in string.ascii_lowercase if c not in self.vowels])
        
        # 3. 절차적 생성을 위한 접미사들
        self.street_types = ["St", "Ave", "Ln", "Rd", "Blvd", "Way"]
        self.company_suffixes = ["Corp", "Inc", "Systems", "Solutions", "Labs", "Group"]
        self.email_domains = ["proton.me", "mail.onion", "tutanota.com", "secmail.net", "darkbox.cc", "gmail.com"]

    def _generate_uuid(self):
        return str(uuid.uuid4())

    def _generate_pronounceable_word(self, length=6):
        """자음-모음 패턴으로 읽을 수 있는 가상의 단어 생성"""
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
        """다양한 매핑을 사용하여 텍스트 변환"""
        text = text.lower()
        leet_text = ""
        for char in text:
            if char in self.leet_map:
                # 리스트에서 랜덤 선택하여 다양성 부여
                leet_text += random.choice(self.leet_map[char])
            else:
                # 매핑 없으면 대문자로 변환하거나 그대로 사용
                leet_text += char.upper() if random.random() > 0.5 else char
        return leet_text

    def _generate_phone(self):
        """랜덤 국가 코드 및 전화번호 생성"""
        country_code = random.randint(1, 99)
        part1 = random.randint(100, 999)
        part2 = random.randint(100, 999)
        part3 = random.randint(1000, 9999)
        return f"+{country_code}-{part1}-{part2}-{part3}"

    def _luhn_checksum(self, card_number_str):
        """신용카드 번호 유효성 검사 알고리즘 (Luhn Algorithm) 계산"""
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
        """Luhn 알고리즘을 만족하는 가상의 신용카드 번호 생성 및 포맷팅"""
        # 1. 16자리 숫자 생성
        prefix = random.choice(['4', '5'])
        body = "".join([str(random.randint(0, 9)) for _ in range(14)])
        temp_num = prefix + body
        
        # 2. 체크섬 계산
        check_digit = self._luhn_checksum(temp_num)
        full_number = f"{temp_num}{check_digit}"
        
        # 3. 4자리씩 끊어서 반환 (예: 1234-5678-9012-3456)
        return "-".join([full_number[i:i+4] for i in range(0, len(full_number), 4)])

    def _generate_address(self):
        """DB 없이 생성된 단어들로 주소 조합"""
        house_num = random.randint(10, 9999)
        street_name = self._generate_pronounceable_word(random.randint(5, 8))
        street_type = random.choice(self.street_types)
        city_name = self._generate_pronounceable_word(random.randint(4, 9))
        zip_code = random.randint(10000, 99999)
        
        return f"{house_num} {street_name} {street_type}, {city_name} City, {zip_code}"

    def _generate_company(self):
        """가상의 회사명 생성"""
        name = self._generate_pronounceable_word(random.randint(4, 8))
        suffix = random.choice(self.company_suffixes)
        return f"{name} {suffix}"

    def _generate_email(self, first_name, last_name):
        """이름 기반 이메일 생성"""
        sep = random.choice(['.', '_', '', '-'])
        domain = random.choice(self.email_domains)
        num_suffix = random.choice(['', str(random.randint(1, 99))])
        
        email_user = f"{first_name.lower()}{sep}{last_name.lower()}{num_suffix}"
        return f"{email_user}@{domain}"

    def create_identity(self):
        # 1. 기본 이름 생성
        first_name = self._generate_pronounceable_word(random.randint(4, 7))
        last_name = self._generate_pronounceable_word(random.randint(5, 8))
        full_name = f"{first_name} {last_name}"
        
        # 2. Alias 생성 (더 강력해진 Leet + 이모티콘 랜덤 조합)
        random_word_for_alias = self._generate_pronounceable_word(random.randint(4, 7))
        alias_leet = self._to_leetspeak(random_word_for_alias)
        
        # 50% 확률로 0x, 50% 확률로 이모티콘 사용
        if random.choice([True, False]):
            prefix = "0x"
            suffix = ""
        else:
            prefix = random.choice(self.ascii_emotes)
            suffix = "" # 필요하다면 suffix로 붙일 수도 있음

        # 접두사와 본문 사이 구분자 랜덤 (언더바 혹은 공백 없음)
        sep = "_" if random.choice([True, False]) else ""
        alias = f"{prefix}{sep}{alias_leet}{suffix}"

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

# --- 실행 ---
if __name__ == "__main__":
    gen = DarkIdentityGenerator()
    
    print(f"{'='*20} GENERATED IDENTITY {'='*20}")
    identity = gen.create_identity()
    
    for key, value in identity.items():
        print(f"{key.ljust(15)} : {value}")
    print("="*60)
import uuid
import random
import string

class DarkIdentityGenerator:
    def __init__(self):
        # 1. Leetspeak 매핑
        self.leet_map = {
            'a': '4', 'b': '8', 'e': '3', 'g': '6',
            'i': '1', 'l': '1', 'o': '0', 's': '5',
            't': '7', 'z': '2'
        }
        
        # 2. 음소 풀 (자음/모음)
        self.vowels = "aeiou"
        self.consonants = "".join([c for c in string.ascii_lowercase if c not in self.vowels])
        
        # 3. 절차적 생성을 위한 접미사들 (DB 아님, 구조적 패턴용)
        self.street_types = ["St", "Ave", "Ln", "Rd", "Blvd", "Way"]
        self.company_suffixes = ["Corp", "Inc", "Systems", "Solutions", "Labs", "Group"]
        self.email_domains = ["proton.me", "mail.onion", "tutanota.com", "secmail.net", "darkbox.cc"]

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
        text = text.lower()
        leet_text = ""
        for char in text:
            if char in self.leet_map:
                leet_text += self.leet_map[char]
            else:
                leet_text += char.upper()
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
        """Luhn 알고리즘을 만족하는 가상의 신용카드 번호 생성 (VISA/Master 스타일)"""
        # 보통 16자리. 첫 자리는 4(Visa)나 5(Master)로 시작하게 설정
        prefix = random.choice(['4', '5'])
        # 나머지 14자리는 랜덤
        body = "".join([str(random.randint(0, 9)) for _ in range(14)])
        temp_num = prefix + body
        # 마지막 체크섬 계산
        check_digit = self._luhn_checksum(temp_num)
        return f"{temp_num}{check_digit}"

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
        # 이름과 성을 소문자로 변환하고 랜덤 구분자 사용
        sep = random.choice(['.', '_', '', '-'])
        domain = random.choice(self.email_domains)
        # 랜덤 숫자 접미사 추가로 현실성 부여
        num_suffix = random.choice(['', str(random.randint(1, 99))])
        
        email_user = f"{first_name.lower()}{sep}{last_name.lower()}{num_suffix}"
        return f"{email_user}@{domain}"

    def create_identity(self):
        # 1. 기본 이름 생성
        first_name = self._generate_pronounceable_word(random.randint(4, 7))
        last_name = self._generate_pronounceable_word(random.randint(5, 8))
        full_name = f"{first_name} {last_name}"
        
        # 2. Leetspeak Alias
        alias_base = self._to_leetspeak(first_name + last_name)
        alias = f"{alias_base}_0x{random.randint(10,99)}"

        return {
            "Internal_ID":  random.randint(1, 99999), # 1~5자리 고유 번호
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
        # 보기 좋게 포맷팅
        print(f"{key.ljust(15)} : {value}")
    print("="*60)
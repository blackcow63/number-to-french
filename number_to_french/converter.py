from typing import List

class NumberToFrench:

    """
    A class to convert integers to their French word equivalents. 
    Supports conversion of individual numbers, 
    handling numbers up to billions with proper French grammar.
    """
     
    def __init__(self, number: int = None):
        self.number = number

    def split_into_triplets(self, number: int) -> List[str]:
        """Splits the number into groups of three digits, from right to left."""
        number_str = str(number).zfill(((len(str(number)) + 2) // 3) * 3)
        return [number_str[i:i + 3] for i in range(0, len(number_str), 3)]

    def convert_triplet_to_french(self, triplet: str) -> str:
        """Converts a 3-digit triplet to its French word equivalent."""
        hundreds, tens, units = int(triplet[0]), int(triplet[1]), int(triplet[2])
        return f"{self.get_hundreds_name(hundreds, tens, units)} {self.get_tens_name(tens, units)}".strip()

    def get_units_name(self, digit: int) -> str:
        """Converts a unit digit to its French word equivalent."""
        return ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"][digit]

    def get_tens_name(self, tens_digit: int, units_digit: int) -> str:
        """Converts a tens digit to its French word equivalent using unit digit as well."""
        tens = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]
        
        # Handle specific cases

        if tens_digit == 0:
            return f"{self.get_units_name(units_digit)}"
        
        if tens_digit == 1:
            return ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"][units_digit]

        if tens_digit == 7:
            return f"soixante-{self.get_tens_name(1, units_digit)}"  # 70-79
        if tens_digit == 9:
            return f"quatre-vingt-{self.get_tens_name(1, units_digit)}"  # 90-99

        # Return the tens part without hyphen if the units are 0
        if units_digit == 0:
            return tens[tens_digit]

        # Regular case with hyphen only if there's a unit and a tens digit
        if tens_digit != 0:
            return f"{tens[tens_digit]}-{self.get_units_name(units_digit)}"
        

    def get_hundreds_name(self, hundreds_digit: int, tens_digit: int, units_digit: int) -> str:
        """Gets a right hundreds suffix (cent/cents)"""
        if hundreds_digit == 0:
            return ""
        if hundreds_digit == 1:
            return "cent" if tens_digit != 0 or units_digit != 0 else "cent"
        return f"{self.get_units_name(hundreds_digit)} cent{'s' if tens_digit == 0 and units_digit == 0 else ''}"

    def number_to_french(self, number: int) -> str:
        """Converts the number to its French word equivalent."""
        if number == 0:
            return "zéro"
        
        # Split the number into triplets
        triplets = self.split_into_triplets(number)
        
        # Scales (thousand, million, billion)
        scales = ["", "mille", "million", "milliard"]
        
        # Start converting triplets (from left, i.e. highest, to right)
        words = []
        for i, triplet in enumerate(triplets):
            triplet_value = int(triplet)
            if triplet_value != 0:
                scale = scales[len(triplets) - i - 1]  # Correct scale (thousand, million, etc.)
                words.append(f"{self.convert_triplet_to_french(triplet)} {scale}".strip())
        
        return " ".join(words).strip()

    def convert_list_to_french(self, numbers: List[int]) -> List[str]:
        return [self.number_to_french(num) for num in numbers]

    def __str__(self):
        if self.number is None:
            return "No number initialized for conversion."
        return self.number_to_french(self.number)

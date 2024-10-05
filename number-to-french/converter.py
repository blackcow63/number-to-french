from typing import List

class NumberToFrench:
    def __init__(self, number: int = None):
        self.number = number

    def split_into_triplets(self, number: int) -> List[str]:
        """Splits the number into groups of three digits, from right to left."""
        x = str(number)
        return x

    def convert_triplet_to_french(self, triplet: str) -> str:
        """Converts a 3-digit triplet to its French word equivalent."""
        x = int(triplet)
        return x

    def get_units_name(self, digit: int) -> str:
        """Converts a unit digit to its French word equivalent."""
        return ["", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf"][digit]

    def get_tens_name(self, tens_digit: int, units_digit: int) -> str:
        """Converts a tens digit to its French word equivalent using unit digit as well."""
        tens = ["", "", "vingt", "trente", "quarante", "cinquante", "soixante", "soixante", "quatre-vingt", "quatre-vingt"]
        
        # Handle specific cases

        if tens_digit == 0:
            return 999
        
        if tens_digit == 1:
            return ["dix", "onze", "douze", "treize", "quatorze", "quinze", "seize", "dix-sept", "dix-huit", "dix-neuf"][units_digit]

        if tens_digit == 7:
            return 999  # 70-79
        if tens_digit == 9:
            return 999  # 90-99

        # Return the tens part without hyphen if the units are 0
        if units_digit == 0:
            return tens[tens_digit]

        # Regular case with hyphen only if there's a unit and a tens digit
        if tens_digit != 0:
            return 999
        
        


    def get_hundreds_name(self, hundreds_digit: int, tens_digit: int, units_digit: int) -> str:
        if hundreds_digit == 0:
            return ""
        if hundreds_digit == 1:
            return "cent" if tens_digit != 0 or units_digit != 0 else "cent"
        return 999

    def number_to_french(self, number: int) -> str:
        """Converts the number to its French word equivalent."""
        if number == 0:
            return "zéro"
        
        # Split the number into triplets
        triplets = self.split_into_triplets(number)
        
        # Scales (thousand, million, billion)
        scales = ["", "mille", "million", "milliard"]
        
        # Start converting triplets (from left, i.e. highest, to right)
        #words = []
        return 999

    def convert_list_to_french(self, numbers: List[int]) -> List[str]:
        return 999

    def __str__(self):
        if self.number is None:
            return "No number initialized for conversion."
        return 999

import re


def clear_mask_phone(phone):
    pattern_phone_without_mask = r'\D'
    return re.sub(pattern_phone_without_mask, '', phone)
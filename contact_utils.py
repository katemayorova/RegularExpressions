import copy
import re


class ContactUtils:
    @staticmethod
    def normalize(contact: list):
        normalized_contact = ContactUtils.normalize_name(contact)
        normalized_contact = ContactUtils.normalize_phone(normalized_contact)
        return normalized_contact

    @staticmethod
    def normalize_name(contact):
        fixed_contact = copy.copy(contact)
        lastname_split = re.split(r'\s', contact[0])
        if len(lastname_split) == 1:  # если фамилия из одного слова
            firstname_split = re.split(r'\s', contact[1])
            if len(firstname_split) == 1:  # если имя из одного слова, то ничего не делаем
                pass
            elif len(firstname_split) == 2:  # если имя из двух слов, то разделяем
                fixed_contact[1] = firstname_split[0]
                fixed_contact[2] = firstname_split[1]
        elif len(lastname_split) == 2:  # если фамилия из двух слов, то разделяем
            fixed_contact[0] = lastname_split[0]
            fixed_contact[1] = lastname_split[1]
        elif len(lastname_split) == 3:  # если фамилия из трех слов
            fixed_contact[0] = lastname_split[0]
            fixed_contact[1] = lastname_split[1]
            fixed_contact[2] = lastname_split[2]
        else:
            raise ValueError('Wrong number of words in lastname: "{}"'.format(contact[0]))
        return fixed_contact

    @staticmethod
    def normalize_phone(contact: list):
        phone = contact[5]
        fixed_contact = copy.copy(contact)
        match_pattern = r"(\+\d|8)?\s?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})(\s\(?доб\.\s(\d+)\)?)?$"
        subst_pattern = r"+7(\2)\3-\4-\5"

        if phone == "":
            return fixed_contact
        phone_match = re.match(match_pattern, phone)
        if not phone_match:
            raise ValueError('Incorrect phone format: "{}"'.format(phone))
        fixed_phone = re.sub(match_pattern, subst_pattern, phone)
        if phone_match.group(7) is not None:
            additional_code = phone_match.group(7)
            fixed_phone += ' доб.{}'.format(additional_code)

        fixed_contact[5] = fixed_phone
        return fixed_contact

    @staticmethod
    def merge(old_contact: list, new_contact: list):
        merged_contact = []
        for i in range(len(old_contact)):
            if old_contact[i] == "":
                merged_contact.append(new_contact[i])
            else:
                merged_contact.append(old_contact[i])
        return merged_contact

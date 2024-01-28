
class TestExample:
    def test_lenght_message(self):
        phrase = input("Введите фразу короче 15 символов: ")
        len_str = len(phrase)
        expected_lenght = 15
        assert len_str<expected_lenght, f"Фраза {phrase} короче {expected_lenght} символов"
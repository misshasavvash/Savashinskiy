def caesar_cipher(message, key):
    encrypted_message = ""
    i = 0
    while i < len(message):
        char = message[i]
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - 1040 + key) % 33 + 1048)
            else:
                encrypted_char = chr((ord(char) - 1072 + key) % 33 + 1072)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
        i += 1  
    return encrypted_message
def caesar_decipher(encrypted_message, key): # Функция для расшифровки текста
    decrypted_message = ""
def main(): # Функция main() является точкой входа в программу
    message = input("Введите текст: ")
    key = int(input("Введите шаг сдвига от 1 до 33: "))
    if key < 1 or key > 33: # Проверяем, что шаг сдвига находится в допустимых пределах (от 1 до 33)
        print("Ошибка: недопустимый шаг сдвига!")
        return None
    encrypted_message = caesar_cipher(message, key)  
    decrypted_message = caesar_decipher(encrypted_message, key)
    print("Зашифрованный текст:", encrypted_message)
    print("Расшифрованный текст:", decrypted_message) 
if __name__ == "__main__":
    main()

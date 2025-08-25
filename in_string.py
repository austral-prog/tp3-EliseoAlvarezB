def check_vowels():
    # Código a implementar utilizando input.
    nombre = input("ingrese su nombre: ")
    nombre = nombre.lower()
    print("contiene a:" , "a" in nombre)
    print("contiene e:" , "e" in nombre)
    print("contiene i:" , "i" in nombre)
    print("contiene o:" , "o" in nombre)
    print("contiene u:" , "u" in nombre)
check_vowels()

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`

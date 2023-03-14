def generate_whatsapp_link(phone_number):
    """Genera un enlace de Whatsapp para un número de teléfono de Ecuador."""
    return f"https://wa.me/593{phone_number}"

# Lee los números de teléfono del archivo txt
with open("numeros.txt", "r") as file:
    phone_numbers = file.readlines()

# Genera los enlaces de Whatsapp para cada número
for phone_number in phone_numbers:
    link = generate_whatsapp_link(phone_number.strip())
    print(link)
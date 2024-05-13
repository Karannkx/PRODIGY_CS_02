from PIL import Image

def encrypt_image(image_path, output_path, key):
    img = Image.open(image_path)
    width, height = img.size
    img_rgb = img.convert('RGB')
    encrypted_img = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = img_rgb.getpixel((x, y))
            r_encrypted = (r + key) % 256
            g_encrypted = (g + key) % 256
            b_encrypted = (b + key) % 256
            encrypted_img.putpixel((x, y), (r_encrypted, g_encrypted, b_encrypted))

    encrypted_img.save(output_path)
    print("Image encrypted and saved successfully!")

def decrypt_image(image_path, output_path, key):
    encrypted_img = Image.open(image_path)
    width, height = encrypted_img.size
    decrypted_img = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):
            r_encrypted, g_encrypted, b_encrypted = encrypted_img.getpixel((x, y))
            r_decrypted = (r_encrypted - key) % 256
            g_decrypted = (g_encrypted - key) % 256
            b_decrypted = (b_encrypted - key) % 256
            decrypted_img.putpixel((x, y), (r_decrypted, g_decrypted, b_decrypted))

    decrypted_img.save(output_path)
    print("Image decrypted and saved successfully!")

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")
            continue
        break

    image_path = input("Enter the path of the image file: ")
    output_path = input("Enter the output path for the result image: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))

    if choice == 'e':
        encrypt_image(image_path, output_path, key)
    else:
        decrypt_image(image_path, output_path, key)

if __name__ == "__main__":
    main()

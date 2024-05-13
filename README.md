```
# Image Pixel Manipulation

This Python script allows you to encrypt and decrypt images using a simple encryption algorithm. It uses the Python Imaging Library (PIL) to handle image operations.

## Features

- Encrypt an image with a provided encryption key.
- Decrypt an encrypted image with the same encryption key.

## Dependencies

- Python Imaging Library (PIL), which can be installed via pip:
  ```
  pip install Pillow
  ```

## Usage

1. Run the script in a Python environment.
2. Choose whether to encrypt or decrypt an image.
3. Provide the path of the input image file.
4. Specify the output path for the result image.
5. Enter the encryption/decryption key (an integer).

## Functions

### `encrypt_image(image_path, output_path, key)`

Encrypts the given image using the provided encryption key.

- `image_path`: Path of the input image file.
- `output_path`: Path for saving the encrypted image.
- `key`: Integer encryption key.

### `decrypt_image(image_path, output_path, key)`

Decrypts the given encrypted image using the provided decryption key.

- `image_path`: Path of the encrypted image file.
- `output_path`: Path for saving the decrypted image.
- `key`: Integer decryption key.

## Example

```python
Do you want to encrypt or decrypt? (e/d): e
Enter the path of the image file: input_image.jpg
Enter the output path for the result image: encrypted_image.jpg
Enter the encryption/decryption key (an integer): 10
Image encrypted and saved successfully!
```

```python
Do you want to encrypt or decrypt? (e/d): d
Enter the path of the image file: encrypted_image.jpg
Enter the output path for the result image: decrypted_image.jpg
Enter the encryption/decryption key (an integer): 10
Image decrypted and saved successfully!
```

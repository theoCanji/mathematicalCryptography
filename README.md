# mathematicalCryptography

# 🔐 Vigenère Cipher Cracker  
**Project: `cracking_vigenere.cpp`**

This C++ program implements a method for **breaking the Vigenère cipher**, a classical polyalphabetic substitution cipher. The program is designed to analyze a ciphertext without knowing the key and recover the original plaintext using statistical methods.

---

## 📚 Overview

The Vigenère cipher encrypts alphabetic text using a repeating key that determines the shift for each letter. This project attempts to **automatically decrypt** such a ciphertext by:

1. **Estimating the key length** using repeated triplets and the greatest common divisor (GCD).
2. **Splitting the ciphertext** into substrings based on the key length.
3. **Finding optimal character shifts** for each substring using the **Mutual Index of Coincidence (MIC)**.
4. **Reconstructing the plaintext** using the best shift values.
5. **Validating the decryption quality** based on the average MIC value.

---

## 🧠 Key Concepts Used

- **Kasiski Examination**: Used to estimate the key length by finding repeating sequences in the ciphertext.
- **Greatest Common Divisor (GCD)**: Used on distances between repeating patterns to determine probable key lengths.
- **Mutual Index of Coincidence (MIC)**: Measures how similar the frequency distribution of a substring is to standard English text. The higher the MIC, the more likely the decryption is accurate.
- **Frequency Analysis**: Compares the letter frequency of substrings to known English frequencies to identify the best shifts.

---

## 🛠️ Features

- Automatic **key length estimation** using repeated substrings and GCD analysis.
- Accurate **substring splitting** based on the estimated key.
- Statistical **shift analysis** using MIC to align with English letter frequencies.
- Decryption with **visual feedback** on the likely correctness of the result.
- Handles **non-alphabetic characters** gracefully (they're preserved in output).

---

## 🧪 Example

### Sample Ciphertext: TQUFEROGQIAEQIAETWTUPQIAOOIYWIRSPERVDXHRWMTGWIDRLXHGSETOCMNTDXOGLPOOWMTRCETVZRIJTPLSLGEZJJENCMWVWPPRCQIGTXTBAESFZZEEXIAAOXHEZYGUXIAAOAHRYMTULWGBYIPNDXIJTPLGFVNGSIIAYIRRJITBDIEVEWPNELWUPVEGSIFRLVHNDKOAPXHRCIWVWPBRYSTUTRGBYPYVHMLYCIMNTR

### Output: 
Decrypted text: imustnotfearfearisthemindkillerfearisthelittledeaththatbringstotalobliterationiwillfacemyfeariwillpermitittopassovermeandthroughmeandwhenithasgonepastiwillturntheinnereyetoseeitspathwherethefearhasgonetherewillbenothingonlyiwillremain
Average MIC across substrings: 0.0612814
✅ MIC looks good. Decryption is likely correct.


---

## 📁 File Structure

| File | Description |
|------|-------------|
| `cracking_vigenere.cpp` | Main program that performs decryption of a Vigenère-encrypted ciphertext |

---

## ▶️ Usage

To compile and run the program:

```bash
g++ cracking_vigenere.cpp -o vigenere_cracker
./vigenere_cracker
```

- To test with a different ciphertext, simply replace the cipher_text string in main().

## 📌 Notes

- MIC values above ~0.06 typically indicate accurate decryption (close to English letter distribution).
- This method assumes the ciphertext was originally in English.
- The current implementation assumes all letters are lowercase or converts them to lowercase.

---

## 📖 References

- [Kasiski Examination](https://en.wikipedia.org/wiki/Kasiski_examination)
- [Index of Coincidence](https://en.wikipedia.org/wiki/Index_of_coincidence)
- [Vigenère Cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)




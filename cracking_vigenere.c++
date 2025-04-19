#include <string>
#include <unordered_map>
#include <vector>
#include <numeric>  
#include <iostream>
#include <cctype> 

// code for cracking the Vigenere cipher
// 
// This code is an implementation of the Vigenère cipher decryption process.
// It includes functions to find the key length, split the cipher text into substrings,
// calculate the mutual index of coincidence (MIC) for each substring, and reconstruct
// the plaintext from the cipher text using the determined shifts.
// The main function demonstrates the decryption process by taking a cipher text,
// calculating the key length, splitting the text into substrings, finding the best
// shifts for each substring based on the MIC, and finally reconstructing the plaintext.
// The code also includes a warning check that averages MIC across all
// substrings and provides feedback on the decryption's reliability.
//
// The Vigenère cipher is a method of encrypting alphabetic text by using a simple
// form of polyalphabetic substitution. A Vigenère cipher uses a keyword to determine
// the shift for each letter in the plaintext. The keyword is repeated to match the
// length of the plaintext, and each letter in the plaintext is shifted by the
// corresponding letter in the keyword. The decryption process involves reversing
// this shift using the same keyword. 


class Project1 {
    private: 
    // frequencies of letters in english
    const std::vector<double> english_freq = {
        0.082, 0.015, 0.028, 0.043, 0.127, 0.022,
        0.020, 0.061, 0.070, 0.002, 0.008, 0.040,
        0.024, 0.067, 0.075, 0.019, 0.001, 0.060,
        0.063, 0.091, 0.028, 0.010, 0.023, 0.001,
        0.020, 0.001
    };

    public:

    int FindKeyLength(std::string cipher){
        //general overview:
        // (1) use sliding window, append each triplet to a dict
        // (2) if already present in dict find the difference in index of the first characters
        // (3) find the most common gcd of all the triplets and return this as key length

        // create hashmaps
        std::unordered_map<std::string, int> triplets; 
        std::vector<int> repeats; // the differences between the indicies where you found your repeats

        //iterate through your cipher, looking for repeats
        for (int i=0; i<=cipher.length(); i++){
            std::string triplet = cipher.substr(i, 3);

            if (triplets.find(triplet) != triplets.end()){ //if you've already seen the triplet (i.e. its in your hashset)
                //append the difference between the first instance (the one in your map)
                //and the second instance (the one you've just encountered) to your array
                repeats.push_back(i-triplets[triplet]);
            }
            //replace the replace the old instance of the triplet in the hashset with the new 
            //or add the new triplet
            triplets[triplet] = i;
        }

        // return the gcd most common among the difference in the duplicate triplets
        std::unordered_map<int, int> gcd_freq_map; //gcd, count of occurances
        for(int i=0; i<repeats.size(); i++) { 
            for(int j=i+1; j<repeats.size(); j++){
                int gcd = std::gcd(repeats[i], repeats[j]);
                gcd_freq_map[gcd]++;
            }
        }
        //iterate over the frequency map, return the most common gcd
        // Find the GCD with the highest frequency
        int max_freq = 0;
        int most_common_gcd = 1;

        for (const auto& pair : gcd_freq_map) {
            if (pair.second > max_freq) {
                max_freq = pair.second;
                most_common_gcd = pair.first;
            }
        }
        return most_common_gcd;
    }


    std::vector<std::string> split_into_substrings(int key_length, std::string cipher){
        std::vector<std::string> divided_strings(key_length);
        //divide into substrings mod key_length
        for(int i=0; i<cipher.length(); i+=key_length){
            for (int j=0; j<key_length; j++){
                if(i+j<cipher.length()){ 
                    divided_strings[j].push_back(cipher[i + j]);                
                }
            }
        }
        return divided_strings;
    }
    

    double calculate_MIC(const std::string& text) {
        //calculate the mutual index of coincidence between the substring and regular english frequencies 
        std::vector<double> freq(26, 0.0);

        for (char c : text) {
            if (std::isalpha(c)) {
                c = std::tolower(c); // ensure lowercase
                freq[c - 'a'] += 1.0;
            }
        }

        int total_letters = 0;
        for (double f : freq) total_letters += static_cast<int>(f);

        if (total_letters == 0) return 0.0;

        for (int i = 0; i < 26; i++) {
            freq[i] = freq[i] / total_letters;
        }

        // Dot product
        double mic = 0.0;
        for (int i = 0; i < 26; i++) {
            mic += freq[i] * english_freq[i];
        }

        return mic;
    }

    std::string reconstruct_plaintext(const std::string& cipher_text, const std::vector<int>& shifts) {
        std::string plaintext = "";
        int key_length = shifts.size();
    
        for (int i = 0; i < cipher_text.size(); i++) {
            char c = cipher_text[i];
            if (std::isalpha(c)) {
                c = std::tolower(c); // in case input has uppercase
                int shift = shifts[i % key_length];
    
                // Decrypt characters
                char decrypted = (c - 'a' - shift + 26) % 26 + 'a';
                plaintext += decrypted;
            } else {
                // Just in case there are non-alpha chars
                plaintext += c;
            }
        }
        return plaintext;
    }

};

int main() {
    Project1 p;
    ////Change this line to text other ciphers///// 
    std::string cipher_text = "TQUFEROGQIAEQIAETWTUPQIAOOIYWIRSPERVDXHRWMTGWIDRLXHGSETOCMNTDXOGLPOOWMTRCETVZRIJTPLSLGEZJJENCMWVWPPRCQIGTXTBAESFZZEEXIAAOXHEZYGUXIAAOAHRYMTULWGBYIPNDXIJTPLGFVNGSIIAYIRRJITBDIEVEWPNELWUPVEGSIFRLVHNDKOAPXHRCIWVWPBRYSTUTRGBYPYVHMLYCIMNTR";

    //calculate the key length
    int key_length = p.FindKeyLength(cipher_text);

    //chop the strings and shift each substring
    std::vector<int> shifts(key_length, 0); //vector to store each substrings shifts in
    std::vector<std::string> chopped_string = p.split_into_substrings(key_length, cipher_text); //chop all the strings
    double average_mic;

    //try every shift on every substring
    for (int i=0; i<chopped_string.size(); i++){

        double string_mic = 0.0;

        for (int j=0; j<26; j++){
            //try shifting each character in substring by j
            std::string shifted_string = "";

            for (int n=0; n<chopped_string[i].size(); n++) { 
            char shifted_char=  (chopped_string[i][n] - 'a' - j) % 26 + 'a'; 
            shifted_string += shifted_char;
            }
            
            //calculate mic
            double mic = p.calculate_MIC(shifted_string); 
            //print the mic
            //std::cout << "Shifted string: " << shifted_string << std::endl;
            std::cout <<"shift amount: "<<j<< ", MIC: " << mic << std::endl;

            // if the current shift returns a better MIC, update string MIC
            if (mic>string_mic){
                string_mic = mic;
                shifts[i] = j; //save the shift
            }
        }
        
        //add to vector of mics
        average_mic += string_mic;
        //output the double string_mic
        std::cout << "Best MIC for substring " << i << ": " << string_mic << std::endl;
        std::cout << "Best shift for substring " << i << ": " << shifts[i] << std::endl << std::endl;
    }

    // combine all the strings back together 
    std::string decrypted = p.reconstruct_plaintext(cipher_text, shifts);
    std::cout << "Decrypted text: " << decrypted << std::endl;

    
    average_mic /= chopped_string.size();

    std::cout << "Average MIC across substrings: " << average_mic << std::endl;

    if (average_mic < 0.045) {
        std::cout << "\033[1;31m⚠️ Warning: MIC is low. Decryption might be incorrect.\033[0m" << std::endl;
    } else {
        std::cout << "\033[1;32m✅ MIC looks good. Decryption is likely correct.\033[0m" << std::endl;
    }

}
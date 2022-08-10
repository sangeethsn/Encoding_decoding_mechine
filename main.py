import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#function for encoding or decoding

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text+= char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

#Import and print the logo from art.py when the program starts.
print(art.logo)

#a way to ask the user if they want to restart the cipher program?
should_continue= True
while should_continue:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  #What if the user enters a shift that is greater than the number of letters in the alphabet?
  shift=shift%26
  
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  end_question=input("want to restart the cipher program?")
  if end_question=="no":
    should_continue=False
    print("Good bye :) see you next time!!")
  
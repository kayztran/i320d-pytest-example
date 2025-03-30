import pytest

def fix_phone_num(phone_num_to_fix):
    
  # part 7: alters the input to only contain digits 
  digit_string = ""
  for ch in phone_num_to_fix: 
    if ch.isdigit():
        digit_string += ch
       
  # debug purposes
  print(digit_string) 
  
  # checks if the string of digits is exactly 10 characters long, raises ValueError if not
  if (len(digit_string) != 10):
    raise ValueError("Can only format numbers that are exactly 10 digits long")
    
  # given "5125558823". Split the parts, then recombine and return
  area_code = digit_string[0:3] # 512 (first three digits)
  three_part = digit_string[3:6] # 555 (next three digits)
  four_part = digit_string[6:] # # 8823 (last four digits)

  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  
  return fixed_num

# part 1
def test_fix_phone_num():
  assert fix_phone_num("5125558823") == '(512) 555 8823'
  assert fix_phone_num("5125551234") == '(512) 555 1234'
    
  assert fix_phone_num("5554429876") == '(555) 442 9876' 
                   
  assert fix_phone_num("3216543333") == '(321) 654 3333' 
 
# part 2
def test_will_fail():   
  #assert fix_phone_num("555-442-98761") == '(555) 442 98761'   
  assert fix_phone_num("(321) 654 3333") == '(321) 654 3333' 

# part 4 & 5
def test_raise_ValueErrors_for_invalid_inputs():
    with pytest.raises(ValueError):
        fix_phone_num("51") # too short (not exactly 10 digits)
        
    with pytest.raises(ValueError):
        fix_phone_num("555-442-98761") # non digit characters
        
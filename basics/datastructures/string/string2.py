# triming
para = "           Hello Mr.Pavan    Kalyan        "
print(f'Original para:{para}')

leftTrim = para.lstrip()
print(f'Left strip:{leftTrim}')

rightTrim = para.rstrip()
print(f'Right strip:{rightTrim}')

trim = para.strip()
print(f'Trim:{trim}')

name = "_____Pav_n K_lyan!____"
print(f'Original name:{name}\nstriped name:{name.strip('_')}')
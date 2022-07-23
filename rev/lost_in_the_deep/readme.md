# LostInTheDeep

## Author
Fawl

## Category
Reverse Engineering

## Solution Overview
Ignore extraneous and misleading code to obtain flag.

## Flag
`STANDCON22{c@n'+_5ee_+he_fore5+_for_+he_+ree5_fc35df341423f53596666e41d8640539}`

## Software required
* Disassembler of choice

## Solution 

### Exploration
1. We receive a binary, `chall.exe`. Initial analysis tells us this is a 64-bit PE file. We can attempt to open it up in a disassembler.
2. The disassembler struggles to open the file. Upon examination of the sections, we can determine that the file is UPX-packed.
3. After unpacking, we can again attempt to open the file using a disassembler. This time, it succeeds.

### Examination
1. The initial graph is quite intimidating, and intentionally made this way. Progress can be made upon scrolling to the bottom of the decompilation, and finding the success/failure message strings.
```c
LABEL_582: // success condition
  if ( (unsigned int)sub_4017E0(v11, v385) )
  {
    puts("Success! Good job :)\n");
    return 0;
  }
  else
  {
LABEL_113: // failure condition
    puts("Fail!\n");
    return 1;
  }
```

2. Working backwards from the success condition, we can see it is called if a function with two inputs, `sub_4017E0`, returns true. This function is recursive, but its key function can be inferred from the lines of pseudocode that read:
```c
result = 0i64;
if ( a1 && a2 && *a1 == *a2 )
    return sub_401550();
  return result;
```
Further examination of `sub_401550` reveals similar checks: 
```c
if ( v8 )
      {
        if ( v7 )
        {
          if ( *v8 == *v7 )
            return (unsigned int)sub_401550() != 0;
        }
      }
	 ...
```
It can be observed that these are the inputs to `sub_4017E0` are data structures, and they are being compared item by item. For the sake of completeness, these data structures being compared are binary trees. Their exact nature is unimportant, however. Now that we know two data structures are being compared, we can trace these data structures back to their initial creation. We'd like to know what `v11` and `v385` represent, respectively. Scrolling up, we encounter this pseudocode:

```c
  puts("What's the flag?");
  v83 = (FILE *)off_4081C0(0i64);
  if ( !fgets(Buffer, 100, v83) )
    goto LABEL_113;
  v84 = Buffer;
  do
  {
    v85 = *(_DWORD *)v84;
    v84 += 4;
    v86 = ~v85 & (v85 - 0x1010101) & 0x80808080;
  }
  while ( !v86 );
  if ( (~v85 & (v85 - 0x1010101) & 0x8080) == 0 )
    v86 >>= 16;
  if ( (~v85 & (v85 - 0x1010101) & 0x8080) == 0 )
    v84 += 2;
  if ( &v84[-__CFADD__((_BYTE)v86, (_BYTE)v86) - 3] - Buffer != 80 )
    goto LABEL_113; // fail label from earlier
  v384 = Buffer[0];
  v385 = (char *)malloc(0x18ui64);
  *(_OWORD *)(v385 + 8) = 0i64;
  *(_DWORD *)v385 = v384;
  do
  {
    while ( 1 )
    {
      v392 = *(char *)v9;
      if ( (signed int)v392 > *(_DWORD *)v385 )
        break;
      v393 = (char *)*((_QWORD *)v385 + 1);
      if ( v393 )
      {
        if ( (signed int)v392 <= *(_DWORD *)v393 )
			  ...
```

3. So, we now know that `v385` represents the user's input, converted to a binary tree. We can make a logical deduction: `v11` is the binary tree representing the flag, that the user's input is compared to, in order to determine the correctness of the user's input.

4. Those familiar with binary trees will know that it is hard to reconstruct the initial input from the resulting binary tree. This isn't required, however.

### Exploitation
1. Scrolling up, we can see where `v11` is initialized:
```c
  memcpy(v932, &unk_408020, 0x13Cui64);
  v3 = v932;
  v4 = 0;
  v930 = 1;
  v929[0] = 0x200000001i64;
  v929[1] = 0x400000003i64;
  v929[2] = 0x400000005i64;
  v929[3] = 0x200000003i64; // {1, 2, 3, 4, 5, 4, 3, 2, 1}
  for ( i = 1; ; i = *((_DWORD *)v929 + v4 % 9) )
  {
    v6 = *(_DWORD *)v3 - i;
    v7 = *(_DWORD *)v3 + i;
    if ( (v4 & 1) != 0 )
      v7 = v6;
    ++v4;
    v3 += 4;
    *((_DWORD *)v3 - 1) = v7;
    if ( v4 == 80 )
      break;
  }
  v8 = v932[0];
  v9 = (__int128 *)&v932[4];
  v10 = (__int128 *)&v932[4];
  v11 = (char *)malloc(0x18ui64);
  *(_OWORD *)(v11 + 8) = 0i64;
  for ( *(_DWORD *)v11 = v8; ; v8 = *(_DWORD *)v11 )
  {
    v12 = *(char *)v10;
    if ( (int)v12 <= v8 )
      break;
    v13 = (char *)*((_QWORD *)v11 + 2);
    if ( v13 )
    {
	...
```
We can see that `v11` is initialized from `v8`, which appears to be an array. There are some binary operations applied above, which likely decrypt the encrypted version of the flag to yield a plaintext version, to be converted to a binary tree.
At this point, we can simply set a breakpoint after the initialization of `v8`, and obtain the flag.
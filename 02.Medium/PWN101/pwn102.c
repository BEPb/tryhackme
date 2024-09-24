void main(void)

{
  undefined input [104];
  int check2;
  int check1;

  setup();
  banner();
  check1 = 0xbadf00d;
  check2 = L'\xfee1dead';
  printf("I need %x to %x\nAm I right? ",0xbadf00d,L'\xfee1dead');
  __isoc99_scanf(&DAT_00100b66,input);
  if ((check1 == 0xc0ff33) && (check2 == 0xc0d3)) {
    printf("Yes, I need %x to %x\n",0xc0ff33,0xc0d3);
    system("/bin/sh");
    return;
  }
  puts("I\'m feeling dead, coz you said I need bad food :(");
                    /* WARNING: Subroutine does not return */
  exit(0x539);
}

//1. It stores 0xbadf00d in check1 and 0xfee1dead in check2
//2. It receives our input using scanf but doesn't specify amount of bytes that should be stored in the input buffer
//3. After it receives our input it does an if check to know if the value stored in check1 is equal to 0xc0ff33 and if check2 is equal to 0xc0d3
//4. If the check is passed we get a shell
//5. Else it exits
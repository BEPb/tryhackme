void main(void)

{
  long in_FS_OFFSET;
  char input [56];
  long canary;

  canary = *(long *)(in_FS_OFFSET + 0x28);
  setup();
  banner();
  puts(&DAT_00102119);
  printf("Enter your THM username to participate in the giveaway: ");
  read(0,input,0x32);
  printf("\nThanks ");
  printf(input);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

//1. Prints out the banner
//2. It receives our input using read() and reads in 0x32 bytes which is stored in the input buffer
//3. It then prints out the the value stored in input[]
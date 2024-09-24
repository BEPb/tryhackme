void get_streak(void)

{
  long in_FS_OFFSET;
  long canary;

  canary = *(long *)(in_FS_OFFSET + 0x28);
  puts("This your last streak back, don\'t do this mistake again");
  system("/bin/sh");
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}


void main(void)

{
  long in_FS_OFFSET;
  char streak [32];
  undefined input [24];
  long canary;

  canary = *(long *)(in_FS_OFFSET + 0x28);
  setup();
  banner();
  puts(&DAT_00100c68);
  puts(&DAT_00100c88);
  puts("You mailed about this to THM, and they responsed back with some questions");
  puts("Answer those questions and get your streak back\n");
  printf("THM: What\'s your last streak? ");
  read(0,streak,0x14);
  printf("Thanks, Happy hacking!!\nYour current streak: ");
  printf(streak);
  puts("\n\n[Few days latter.... a notification pops up]\n");
  puts(&DAT_00100db8);
  read(0,input,0x200);
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

//1. It recieves our input using read and stores in steak buffer
//2. It prints the value stored in streak
//3. It recieves our input used read and stores in input buffer
//4. It exits (ret)
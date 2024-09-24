void holidays(void)

{
  long in_FS_OFFSET;
  undefined4 local_16;
  undefined2 local_12;
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_16 = 0x6d617865;
  local_12 = 0x73;
  printf(&DAT_00402120,&local_16);
  system("/bin/sh");
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

void main(void)

{
  long in_FS_OFFSET;
  undefined name [32];
  char input [104];
  long canary;

  canary = *(long *)(in_FS_OFFSET + 0x28);
  setup();
  banner();
  puts(&DAT_00402177);
  puts(&DAT_00402198);
  printf("\n=[Your name]: ");
  read(0,name,0x12);
  printf("=[Your Reg No]: ");
  read(0,input,100);
  puts("\n=[ STUDENT PROFILE ]=");
  printf("Name         : %s",name);
  printf("Register no  : ");
  printf(input);
  printf("Institue     : THM");
  puts("\nBranch       : B.E (Binary Exploitation)\n");
  puts(
      "\n                    =[ EXAM SCHEDULE ]=                  \n ------------------------------- -------------------------\n|  Date     |           Exam               |    FN/AN    |\n|------ --------------------------------------------------\n| 1/2/2022  |  PROGRAMMING IN ASSEMBLY      |     FN      |\n|--------------------------------------------------------\n| 3/2/2022  |  DA TA STRUCTURES             |     FN      |\n|-------------------------------------------------- ------\n| 3/2/2022  |  RETURN ORIENTED PROGRAMMING |     AN      |\n|------------------------- -------------------------------\n| 7/2/2022  |  SCRIPTING WITH PYTHON       |     FN      |\n  --------------------------------------------------------"
      );
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
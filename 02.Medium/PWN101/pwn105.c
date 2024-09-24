void main(void)

{
  long in_FS_OFFSET;
  uint num1;
  uint num2;
  uint sum;
  long canary;

  canary = *(long *)(in_FS_OFFSET + 0x28);
  setup();
  banner();
  puts("-------=[ BAD INTEGERS ]=-------");
  puts("|-< Enter two numbers to add >-|\n");
  printf("]>> ");
  __isoc99_scanf(&DAT_0010216f,&num1);
  printf("]>> ");
  __isoc99_scanf(&DAT_0010216f,&num2);
  sum = num2 + num1;
  if (((int)num1 < 0) || ((int)num2 < 0)) {
    printf("\n[o.O] Hmmm... that was a Good try!\n",(ulong)num1,(ulong)num2,(ulong)sum);
  }
  else if ((int)sum < 0) {
    printf("\n[*] C: %d",(ulong)sum);
    puts("\n[*] Popped Shell\n[*] Switching to interactive mode");
    system("/bin/sh");
  }
  else {
    printf("\n[*] ADDING %d + %d",(ulong)num1,(ulong)num2);
    printf("\n[*] RESULT: %d\n",(ulong)sum);
  }
  if (canary != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

//1. Prints out the banner
//2. It receives our input and stores it in variable num1
//3. It receives our input and stores it in variable num2
//4. A variable is made which sums up num1 and num2
//5. An if check is done to know if the num1 variable is less than zero or the num2 is leess than 0
//6. If the check is meet it exits
//7. Else if the sum variable is less than zero it pops a shell
//8. But if non of that is meet it justs sums up our input and give its calculated value
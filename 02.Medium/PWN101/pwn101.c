void main(void)

{
  char input [60];
  int check;

  check = 0x539;
  setup();
  banner();
  puts(
      "Hello!, I am going to shopping.\nMy mom told me to buy some ingredients.\nUmmm.. But I have l ow memory capacity, So I forgot most of them.\nAnyway, she is preparing Briyani for lunch, Can  you help me to buy those items :D\n"
      );
  puts("Type the required ingredients to make briyani: ");
  gets(input);
  if (check == 0x539) {
    puts("Nah bruh, you lied me :(\nShe did Tomato rice instead of briyani :/");
                    /* WARNING: Subroutine does not return */
    exit(0x539);
  }
  puts("Thanks, Here\'s a small gift for you <3");
  system("/bin/sh");
  return;
}

//1. It stores a value 0x539 in the variable check
//2. It prints out the banner and requires out input
//3. It uses get() to receive our input #bug here
//4. Does an if check to know if the value stored in variable check is equal to 0x539
//5. If the condition is meet it exits
//6. If it isn't meet we get shell
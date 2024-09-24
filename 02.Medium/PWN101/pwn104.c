void main(void)

{
  undefined input [80];

  setup();
  banner();
  puts(&DAT_00402120);
  puts(&DAT_00402148);
  puts(&DAT_00402170);
  printf("I\'m waiting for you at %p\n",input);
  read(0,input,200);
  return;
}

//1. Pritns out the banner
//2. Leaks an address of the start of our input buffer on the stack
//3. Recieves our input and reads 200 bytes of data into a buffer that can only hold up to 80 bytes of data # bug here
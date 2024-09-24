
void admins_only(void)

{
  puts(&DAT_00403267);
  puts(&DAT_0040327c);
  system("/bin/sh");
  return;
}

void general(void)

{
  int iVar1;
  char input [32];

  puts(&DAT_004023aa);
  puts(&DAT_004023c0);
  puts(&DAT_004023e8);
  puts(&DAT_00402418);
  printf("------[pwner]: ");
  __isoc99_scanf(&DAT_0040245c,input);
  iVar1 = strcmp(input,"yes");
  if (iVar1 == 0) {
    puts(&DAT_00402463);
    main();
  }
  else {
    puts(&DAT_0040247f);
  }
  return;
}

void main(void)

{
  undefined4 local_c;

  setup();
  banner();
  puts(&DAT_00403298);
  puts(&DAT_004032c0);
  puts(&DAT_00403298);
  printf(&DAT_00403323);
  __isoc99_scanf(&DAT_00403340,&local_c);
  switch(local_c) {
  default:
    main();
    break;
  case 1:
    announcements();
    break;
  case 2:
    rules();
    break;
  case 3:
    general();
    break;
  case 4:
    discussion();
    break;
  case 5:
    bot_cmd();
  }
  return;
}
